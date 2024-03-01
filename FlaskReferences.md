# Flask - References, Guide

# Virtual Enviroment
Also reference: PythonReferences.md
**Create the Virtual Environment:** Run:
`python -m venv myenv` 
(Where "myenv" is the enviroment name)
**Activate the Virtual Environment:** 
- macOS/Linux:
`source myenv/bin/activate`
- Windows
`myenv\Scripts\activate`

**Install Dependencies:** Inside the virtual environment, install dependencies using `pip`:
`pip install -r requirements.txt`
or `pip install package_name`
**Deactivate the Virtual Environment:** To exit the virtual environment, use:
`deactivate`
 
# Flask Setup

**Install flask:**
`pip3 install flask`

**Install Flask Login**
`pip3 install flask-login`

**Install SQLAlchemy**
`pip3 install Flask-SQLAlchemy`

# Flask Initialization
1.Follow the setup, create a venv at the project level and finish the setup
2.Create a website folder, which will be out python package
3.At the project level create the app.py file
4.Reference the file structure

### __init__.py
Inside the website folder create the __init__.py file and enter the following code:
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "devflask123"
    #include new modules in the __init__ file
    from .views import views

    app.register_blueprint(views, url_prefix="/")
    # Register the new blueprints

    return app
```

### app.py
The app.py file is our main project file, it will be located in main outside any folder.
Enter the following code:
```python
from website import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
```

### views.py
Will have all the view-related application. What the user can see, view
Insert the following
```python
from flask import Blueprint

views = Blueprint("views", __name__)

@views.route("/home")
def home():
    return "Home"
```

### Add new routes to __init_
Always when making any new routes add them to __init__ 
```python
    # make their relative import
    from .views import views

    # Register the new blueprint
    app.register_blueprint(views, url_prefix="/")
```
### auth.py
A different file to set all the routes authentication-related, reference Blueprints at the glossary.
```python
from flask import Blueprint

auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    return "login"
```

# Forms - methods
By default the routes state is set to GET, specify for both or POST only.
Example:
```python
@views.route("/home") # GET by default
def home():
    return "Home"
# Both
@views.route("/home", methods=["GET", "POST"])
def home():
    return "Home"
```
### Method isolation
Remember to be explicit when dealing with POST and GET methods
```python
if request.method == "POST":
    username = request.form.get("username")
    # content
#Get
else:
    pass
# Or just any code outside will be get too.
render_template(request, "index.html")
```

# Models - Database

### Database Setup
At the top of our __init__ file, right bellow the function imports include:
```python
db = SQLAlchemy()
DB_NAME = "database.db"
```
bellow the "`app.config['SECRET_KEY'] = "devflask123"`" include:
```python
app.config['SECRET_KEY'] = "devflask123"
# Include
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)
```

**Reference the "FULL INIT FILE"**

**create_database function:**
```python
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')
```
and include the new function inside the create_app function:
```python
create_database(app)
```

### Models.py
Inside out website/ dir, create models.py. In this file we will place all the models for our application.

**Creating the user model**
Include:
```python
# Include: 
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    ...
```
Stop for a second to consider the information we need from the user.
Also **Reference FULL MODEL FILE** for a full example.

Include the functions to the init file and also include the login_manager.
```python
    app.register_blueprint(auth, url_prefix="/")

    from .models import User

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
```
### IF NOT MODELS - Relational Databases
include directly to the __init__ file the database path as follows:
```python
# include database
import sqlite3

app = Flask(__name__)

db = SQL("sqlite:///database_name.db")
```
Then just by referencing the db. we can perform queries as:
```python
db.execute("DELETE FROM registrants WHERE id = ?", id)
db.execute("INSERT INTO registrants (name, sport) VALUES(?, ?)", name, sport)
...
```







# Glossary

# Blueprints
Allows modularity within our code by seting up different routes for their different purpouses.
In this way we can have a file for our views, nother one for related authentication, etc.
Example: 
```python
@auth.routes("/login")
def login:
    return "login"
@views.routes("/home")
def home():
    return "Home"
```
Every time you create a new blueprint you need to added to the __init__ module.
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from os import path
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "devflask123"

    from .views import views
    from .auth import auth
    # Here you would need to include the module

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    # Register the new blueprint copy same strucuture

    return app
```

### FULL INIT FILE
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "helloworld"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{{DB_NAME}}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')
```

### FULL MODELS FILE
```python
from . import db
from flask_login import UserMixin
from sql_alchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
```

### request.args
is only used when request method is GET, is a dictionary that contains all your key: value pairs

## request.from
When using post you must use request.form

## flash()
Flash takes a string as a parameter and an optional category argument.
The for categories available are:
1.'info'
2.'sucess'
3.'warning'
4.'error'
**Template usage:**
```HTML
{% with messages = get_flashed_messages(with_categories=true) %}
  {% if messages %}
    <ul class=flashes>
    {% for category, message in messages %}
      <li class="{{ category }}">{{ message }}</li>
    {% endfor %}
    </ul>
  {% endif %}
{% endwith %} 
```

## Default Route Methods
by default the `@app.route()` is set to GET
```python
# Default
@app.route("/example") #methods=["GET"] 
```

For POST request you must explecitly declare the method as follows
```python
@app.route("/example", methods=["POST"])  
```


## File Structure

```bash
project/
├── venv/
│   ├── bin/
│   ├── include/
│   ├── lib/
│   └── ...
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   └── templates/
│       └── index.html
├── config.py
├── requirements.txt
└── run.py
```
