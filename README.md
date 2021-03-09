
This website is built using Django Rest framework in the backend and HTML, CSS and Javascript on the frontend.

# XMEME

**Users will post Memes by providing these inputs**

- Name of the person posting the meme

- Caption for the Meme

- URL of the Meme image
---
The memes are displayed in the reverse chronological order i.e. last created/updated one first.


![Form](https://github.com/jainsras/django-rest-xmeme/blob/master/assets/Screenshot%20(415).png)

![Frontend](https://github.com/jainsras/django-rest-xmeme/blob/master/assets/Screenshot%20(416).png)

![Frontend](https://github.com/jainsras/django-rest-xmeme/blob/master/assets/Screenshot%20(417).png)

![Backend](https://github.com/jainsras/django-rest-xmeme/blob/master/assets/Screenshot%20(419).png)

![Backend](https://github.com/jainsras/django-rest-xmeme/blob/master/assets/Screenshot%20(420).png)


--- 

- Install Python Latest Version
 [ https://www.python.org/downloads/ ]

- Install Pip (Package Manager)
[ https://pip.pypa.io/en/stable/installing/ ]

### Installation
**Create a Folder where you want to save the project**

**Create a Virtual Environment and Activate**

Install Virtual Environment First
```
$  pip install virtualenv
```

Create Virtual Environment

For Windows
```
$  python -m venv venv
```
For Mac
```
$  python3 -m venv venv
```

Activate Virtual Environment


## HOW TO RUN THIS PROJECT

```
$ pip install -r requirements.txt
```
```
$ python manage.py makemigrations
```
```
$ python manage.py migrate
```
```
$ python manage.py runserver
```
**Login Credentials**

Create Super User 
```
$  python manage.py createsuperuser
```
Then Add Email, Username and Password

**or Use Default Credentials**


Email: admin@gmail.com

username: admin

Password: admin


- Now enter following URL in your browser installed in your pc
```
http://127.0.0.1:8081/
```
The posted meme inputs from the frontend and store them in a database.

You can fetch the list of memes from the database using the url-
HTTP Method - GET, POST
```
http://127.0.0.1:8081/meme/
```
Json Body contains these inputs - name, url, caption, created_date

Endpoint to specify a particular id (identifying the meme) to fetch, Edit or Delete a single Meme-

HTTP Method - GET, PUT, DELETE

```
http://127.0.0.1:8081/meme/{id}
```
Documented apis using swagger- [ http://localhost:8081/swagger-ui/ ]

Publicly hosted Url-  [ https://xmeme-creation.herokuapp.com/ ]

