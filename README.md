# RANGE MYSOCIAL

## Simple instagram clone

### Starting the project:

1. Create a **virtual environment** with venv (install virtualenv, if its not installed).

    ```
    virtualenv venv
    ```

2. Clone the project in the virtual environment directory.

    ```
    git clone https://github.com/darkdeathgunn/range-mysocial.git
    ```

3. Activate the virtual environemnt.

    #### For Linux/Mac OSX   
    ```
    source bin/activate
    ```

    #### For Windows
    ```
    .\Scripts\activate
    ```

4. Install the requirements.

    ```
    cd mysocial
    pip install -r requirements.txt
    ```
 5. This project uses Postgresql for databse, so install it if you don't have it.Create a database in Postgresql. And go to:
    ```
    mysocial/settings.py
    ```
 6. Update setting.py with your database details
    ```
    DATABASE
    ```

 8. Run the Migrations
    ```
    python manage.py makemigrations
    
    python manage.py migrate
    ```
8. Run the development server
    ```
    python manage.py runserver
    ```
9. Head to server http://127.0.0.1:8000

HAVE FUN!!!!!

## For contributors

Range blogger uses the following technologies:

+ HTML/CSS/JavaScript
+ Pyhton(Django)
