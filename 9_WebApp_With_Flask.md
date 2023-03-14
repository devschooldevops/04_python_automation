## Flask intro
In order to create lightweight web applications with python we could use Flask. This framework offers
useful tools and feature to build a web app.
Between the most important characteristics we can enumerate: 
 - Flexibility - you can develop a web application within one python file
 - Extensibility - it's not imposing certain directory structure and is not requiring complicated boilerplate code
 - Usage of Jinja templates - uses jinja template engine to render dynamically HTML pages, making use of python concepts like loops, lists, and so on. 

## Install Flask 

```bash
$ pip3 install flask
```

To check the version we can run the following command 

```bash
python3 -c "import flask; print(flask.__version__)"
```

## Hello world application with Flask

Let's start by creating a simple python program that uses Flask

Step 1. Create a python file

```bash
touch hello.py
```

Step 2. Add the hello world function 

```python3
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'
```

Step 3. Run the application 
In order to run the python file, we need first to specify Flask where should find the application.

```commandline
export FLASK_APP=hello
```

As we are running the application locally we need to specify to Flask also that should run it in development mode. 

```commandline
export FLASK_ENV=development
```

To finally run it, we execute the following command 

```commandline
flask run
```

## Using HTML templates

As we already mentioned Flask is using Jinja templates engine to render HTML pages. 

How is doing this ? 

You can use render_template() function in order to render the pages composing your application like in the below example.

Step 1. Let's create a new python file

Step 2. Add the following function 

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
```

If we just run it now, it will generate an error, because of missing templates

Step 3. Add template file 

templates folder will be looked as default location for html file

```commandline
mkdir templates
cd templates
vi index.html
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>FlaskIntro</title>
</head>
<body>
   <h1>Welcome to FlaskIntro</h1>
</body>
</html>
```

## Creating a RESTful endpoint with Flask 

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    { 'name': 'John', 'age': 19 }
]


@app.route('/students')
def get_students():
    return jsonify(students)


@app.route('/students', methods=['POST'])
def add_student():
    students.append(request.get_json())
    return '', 204
```

## Adding a database for data persistance

In order to persist data we need files, or a database. In our example we will use SQLite as it's already 
part of python3 

The first step in order to connect our application to a database is to create a database 

```sqlite
DROP TABLE IF EXISTS students;

CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    age INTEGER NOT NULL,
    name text NOT NULL
);
```

Then we need to initiate database connection

```python
import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO students (age, name) VALUES (?, ?)",
            ('21', 'Marie')
            )

cur.execute("INSERT INTO students (age, name) VALUES (?, ?)",
            ('22', 'Jay')
            )
connection.commit()
connection.close()
```

How we can see the elements in the database

```python
import sqlite3
from flask import Flask, render_template

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn
    
@app.route('/')
def index():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students').fetchall()
    conn.close()
    return render_template('index.html', students=students)

```


```html
{% extends 'base.html' %}

{% block content %}
<h1>{% block title %} Welcome to FlaskIntro {% endblock %}</h1>
{% for student in students %}
<a href="#">
  <h2>{{ student['name'] }}</h2>
</a>
<span class="badge badge-primary">{{ student['age'] }}</span>
<hr>
{% endfor %}
{% endblock %}
```
