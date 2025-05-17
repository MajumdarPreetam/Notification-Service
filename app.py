from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

notification_queue = []
user_notifications = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send-form', methods=['POST'])
def send_form():
    user_id = request.form['userId']
    type_ = request.form['type']
    message = request.form['message']
    
    notification = {
        'type': type_,
        'message': message,
        'status': 'pending'
    }

    if user_id not in user_notifications:
        user_notifications[user_id] = []
    
    user_notifications[user_id].append(notification)
    notification_queue.append((user_id, notification))
    
    return redirect(url_for('home'))

@app.route('/get-notifications')
def get_notifications():
    user_id = request.args.get('userId')
    notifications = user_notifications.get(user_id, [])
    return render_template('index.html', notifications=notifications, userId=user_id)

@app.route('/process', methods=['POST'])
def process_queue():
    for user_id, notification in notification_queue:
        if notification['status'] == 'pending':
            notification['status'] = 'sent'
    notification_queue.clear()
    return redirect(url_for('get_notifications', userId=request.form['userId']))

if __name__ == '__main__':
    app.run(debug=True)
