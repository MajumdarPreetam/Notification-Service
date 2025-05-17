Notification Service Project

1. Overview
This is a simple Flask-based **Notification Service** that allows sending and retrieving notifications for users. The notifications can be of three types:

Email
SMS
In-app

Notifications are initially marked as `pending` and change to `sent` when processed.


2.  Folder Structure
```
notification_service/
├── static/
│   └── style.css            # Stylesheet for the web interface
├── templates/
│   └── index.html           # HTML UI using Jinja2
├── app.py                   # Main Flask application
└── README.md                # Project documentation
```


3.  Setup Instructions
(a) Prerequisites
(b) Python 3.x
(c) Flask (install via pip)


4. Installation Steps
a) Clone the repository:

```bash
git clone https://github.com/MajumdarPreetam/Notification-Service.git
cd Notification-Service
```
b) Install dependencies:

```bash
pip install flask
```

c) **Run the application:

```bash
python app.py
```

d) **Open in browser:
   Visit `http://127.0.0.1:5000` in your browser.


5.  Features
a) Send notifications via Email, SMS, or In-app type.
b) View all notifications for a given user.
c) Process queued notifications with a click (status changes from `pending` to `sent`).
d) Simple and responsive frontend using HTML + CSS.


6.  API Endpoints
a) `POST /send-form`: Sends a notification.
b) `GET /get-notifications?userId=<user_id>`: Retrieves notifications for the given user.
c) `POST /process`: Processes all pending notifications.


7.  Assumptions Made
a) Actual sending of emails/SMS is not implemented (this is a simulation).
b) User ID is treated as a string (e.g., `user123`).
c) Queue processing is simulated within the application logic.

