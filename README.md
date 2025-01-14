# Django Signup Form

This project is a Django-based application that provides a signup and login system for different types of users: Patients and Doctors. Upon successful signup, users are redirected to a success page and can log in to access their respective dashboards.

## Project Structure

- **accounts**: Contains the main logic for user signup and login.
- **templates/accounts**: Contains HTML templates for signup, login, and dashboards.
- **static**: Contains static files like CSS and images.

## Features

- **Signup**: Users can sign up as either a Patient or Doctor.
- **Login**: Users can log in using their credentials.
- **Dashboard**: After login, users are redirected to their respective dashboards.
- **Validation**: Ensures that passwords match and meet the necessary criteria.

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/Poorani-27/Django_signup_form.git
    cd Django_signup_form
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

7. Open your web browser and go to `http://127.0.0.1:8000/accounts/signup/` to use the application.

## Usage

1. **Signup**:
    - Go to the signup page and fill in the required details.
    - Choose whether you are a Patient or a Doctor.
    - After filling in the form, click the signup button to create your account.

2. **Login**:
    - After account creation, you will be redirected to a success page.
    - Click on the login link to go to the login page.
    - Enter your username and password to log in.

3. **Dashboard**:
    - Upon successful login, you will be redirected to your respective dashboard.
    - The dashboard will display a welcome message and provide options to log out and sign up.

## Technologies Used

- **Django**: Web framework
- **HTML/CSS**: For frontend design
- **SQLite**: Default database for development

- **Vercel CLI**  for deployment



![](img/Untitled.png)


![](img/Untitle2.png)


![](img/Untitled3.png)


![](img/Untitled4.png)


![](img/Untitled5.png)


![](img/Untitled7.png)


![](img/Untitled8.png)
