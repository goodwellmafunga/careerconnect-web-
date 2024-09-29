# CAREERCONNECT

CAREERCONNECT is a premier institution dedicated to providing top-notch education and career development opportunities. This web application is built using Flask and deployed on Render.

## Features

- **Home Page**: Overview of CAREERCONNECT
- **News**: Latest news and updates
- **Courses**: List of available courses
- **Events**: Upcoming events
- **About**: Information about CAREERCONNECT
- **Contact**: Contact information
- **User Authentication**: User registration and login
- **Admin Portal**: Manage students, payments, courses, staff, notes, and question papers

## Technologies Used

- **Frontend**: HTML, CSS, Bootstrap
- **Backend**: Flask, SQLAlchemy
- **Deployment**: Render

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/goodwellmafunga/careerconnect-web-.git
    cd careerconnect-web-
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```bash
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```

5. Run the application:
    ```bash
    python run.py
    ```

## Deployment on Render

1. Create a new Web Service on Render.
2. Connect your GitHub repository.
3. Set the Build Command to:
    ```plaintext
    pip install -r requirements.txt
    ```
4. Set the Start Command to:
    ```plaintext
    ./start.sh
    ```
5. Set the Publish Directory to:
    ```plaintext
    ./
    ```



