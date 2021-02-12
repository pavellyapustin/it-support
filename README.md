# IT Support

IT Support is a webapp using (Django and Python 3.9) to register the IT technician's jobs (logs) of his activities at the company.

The IT manager can use it to track and maintain their employees activities.

Remember for more user control access the <b>/admin</b> module.

## Running The Application

```bash
# Installing Virtualenv
$ pip install Virtualenv

# Creating virtual environment
$ Virtualenv .env

# Activating
> .env\Scripts\activate # On Windows
$ source ./.env/Scripts/activate # On Linux

# Installing requirements
$ pip install -r requirements.txt

# Make migrations and migrate
$ python manage.py makemigrations
$ python manage.py migrate

# Creating a superuser
$ python manage.py createsuperuser

# Running
$ python manage.py runserver
```

## Screens

Main screen

![Alt text](print_screens/01.png)

Login

![Alt text](print_screens/02.png)

Profile

![Alt text](print_screens/03.png)
