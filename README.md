## Hosted

https://shishaa.pythonanywhere.com/

## Screenshots

![home](https://user-images.githubusercontent.com/39271713/89833776-4b9fc680-db6a-11ea-8690-10784192e198.png)

![order](https://user-images.githubusercontent.com/39271713/89833883-80138280-db6a-11ea-8654-eb67f450448e.p

![checkout](https://user-images.githubusercontent.com/39271713/89833978-a20d0500-db6a-11ea-8933-1df6b8637b8e.png)



# fashion_web

**fashion_web** is a E-commerce system written in Python 3 and using Django framework.
The application has the following functionalities.
1. Register new users.
2. Log in registered users.
3. Logged in users can order products and checkout
4. Admin is able to add Products.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See installing instructions for notes on how to deploy the project on a live system.


### In development features

* Payment intergration

### Prerequisites
You will find hereafter what I use to develop and to run the project
* Python 3
* Django 4.0.2
* pipenv (not mandatory but highly recommended).  Instructions on how to get pipenv [here](https://pypi.org/project/pipenv/)


### Installation

Get a local copy of the project directory by cloning "opportunity-management" from github.

```bash
git clone https://github.com/BabGee/fashion_web.git
```

cd into the folder

```bash
cd fashion_web
```

I use pipenv for developing this project so I recommend you to create a virtual environment and activate it.

```bash
python3 -m pipenv shell
```

Install the requirements

```bash
python3 -m pip install -r requirements.txt
```

Then follow these steps:
1. Move to root folder 

```bash
cd django_angular
```
2. Create a `.env` file in the root folder, provide the required database information  to the `.env` file (.env.example file is provided to help set this information)

3. Create the tables with the django command 

```bash
python manage.py makemigrations
```
then migrate the changes
 
```bash
python manage.py migrate
```

Create an admin using command below and enter your preferred username, email and password.(You will use this to login django admin and create products etc)
 
```bash
python3 manage.py createsuperuser
```

4. Finally, run the django server

```bash
python manage.py runserver
```


5. Access the django admin by adding ' /admin' to the url and login to create products.

## Built With

* [Python 3](https://www.python.org/downloads/) - Programming language
* [Django](https://www.djangoproject.com/) - Web framework 


## Versioning
I use exclusively Github

## License

This is an open source project not under any particular license.
However framework, packages and libraries used are on their own licenses. Be aware of this if you intend to use part of this project for your own project.
