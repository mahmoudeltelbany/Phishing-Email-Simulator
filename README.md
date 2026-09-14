# Phishing Email Simulator

A simple phishing email simulation project built with **Python and Flask** for educational and cybersecurity training purposes.

The project simulates a login page that communicates with a Flask backend and demonstrates how login credentials can be submitted through HTTP requests.

## Features

* Simulated login page
* Flask backend
* REST API for login authentication
* HTTP `POST` request handling
* JSON request/response handling
* Session-based authentication
* Login and logout endpoints
* Request inspection and logging
* Simple demo user authentication

## Technologies

* Python
* Flask
* HTML
* CSS
* JavaScript
* REST API
* HTTP

## Project Structure

```text
phishing-email-simulator/
│
├── app.py
├── templates/
│   └── login.html
│
└── README.md
```

## Installation

Clone the repository:

```bash
git clone <YOUR-REPOSITORY-URL>
cd phishing-email-simulator
```

Install Flask:

```bash
py -m pip install Flask
```

## Running the Project

Start the Flask application:

```bash
py app.py
```

The application will run locally on:

```text
http://127.0.0.1:5050
```

Open the URL in your browser to access the simulated login page.

## Demo Account

The project includes a test account for local development:

```text
Email: demo@mystory.com
Password: password123
```

## How It Works

The user interacts with the simulated login page.

The frontend sends the login information to the Flask backend using a `POST` request:

```text
POST /api/login
```

The Flask application processes the request and validates the test account.

A successful authentication creates a session and allows access to protected API endpoints.

## Disclaimer

This project is intended **for educational purposes and authorized security testing only**.

Do not use it to collect credentials from users without their explicit permission. Use only test accounts and controlled environments.

GitHub: [mahmoudeltelbany](https://github.com/mahmoudeltelbany)
