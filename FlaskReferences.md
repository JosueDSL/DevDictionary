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

**Install WTF Forms**
`pip3 install flask-wtf`

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
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{{DB_NAME}}'
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

### Model Column Types
We use the following column types:

* String(N), where N is the maximum number of characters
* Integer, representing a whole number

Column can take some other parameters:

* unique: when True, the values in the column must be unique
* index: when True, the column is searchable by its values
* primary_key: when True, the column serves as the primary key

### Model One to Many
We declare a one-to-many relationship between Book and Review by creating the following field in the Book model:
```python
class Book(db.Model):
    reviews = db.relationship('Review', backref='book', lazy='dynamic')
class Reader(db.Model):
    reviews = db.relationship('Review', backref='reviewer', lazy = 'dynamic')
```
where
* the first argument denotes which model is to be on the ‘many’ side of the relationship: `Review.`
`backref = 'book'` establishes a book attribute in the related class (in our case, class Review) which will serve to refer back to the related `Book` object. `*lazy = dynamic` makes related objects load as SQLAlchemy’s query objects.
Here 'Review' is linking to its table, extracting that field

But that does not completely specify our one-to-many relationship. We additionally have to specify what the foreign keys are for the model on the ‘many’ side of the relationship. 
```python
class Review(db.Model):
    ...
    #Note the lower case here: 'book.id' instead of 'Book.id'
    book_id = db.Column(db.Integer, db.ForeignKey('book.id')) #foreign key column

    reviewer_id = db.Column(db.Integer, db.ForeignKey('reader.id'))
    #get a printout for Review objects
    def __repr__(self):
        return "Review: {} stars: {}".format(self.text, self.stars)
```
```SQL
CREATE TABLE review (
        id INTEGER NOT NULL, 
        stars INTEGER, 
        text VARCHAR(200), 
        book_id INTEGER, 
        reviewer_id INTEGER, 
        PRIMARY KEY (id), 
        FOREIGN KEY(book_id) REFERENCES book (id), 
        FOREIGN KEY(reviewer_id) REFERENCES reader (id)
);
```

### initializing the database
```shell
$ python3
>>> from app import db
>>> db.create_all()
```
Or:
From within the application file.

After all the models have been specified the database is initialized by adding db.create_all() to the main program. The command is written after all the defined models.
### Model Entries for relationships
```python
rev1 = Review(id = 435, text = 'This book is amazing...', stars = 5, reviewer_id = r1.id, book_id = b1.id)
```
reference the variable inside the

# Forms - WTF Forms
First install WTF Froms library by running:
`pip install flask-wtf`

Import the package:
```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
```

### Form format:
```python
lass RegistrationForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Register')
```
### Form methods
```python
# registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
  form = RegistrationForm(csrf_enabled=False)
  if form.validate_on_submit():
    # define user with data from form here:
    user = User(username=form.username.data, email=form.email.data)
    # set user's password here:
    user.set_password(form.password.data)
    db.session.add(user)
    db.session.commit()
  return render_template('register.html', title='Register', form=form)
```

# Glossary

## Blueprints
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

## FULL INIT FILE
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# Initialize the database
db = SQLAlchemy()
DB_NAME = "database_name.db"

def create_app():
    # Initialize the Flask app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'rootadmin1234' # Change
    
    # Set the database URI
    basedir = path.abspath(path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + path.join(basedir, DB_NAME)
    db.init_app(app)
    
    # Include MVT components and auth
    from .views import views
    from .auth import auth

    # Register the blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Create database and intialize models
    from .models import User
    
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Database Successfully Initialized!')
```

## FULL MODELS FILE
```python
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
```

## Libraries, Dependencies, Packages
The most commonly used Classes, Functions and packages:
```python
from datetime import datetime
# Flask
from flask import Flask, render_template, request, redirect, url_for, flash
# SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
# Flask-Login
from flask_login import UserMixin, LoginManager, login_required, login_user, current_user
# Flask-WTForms
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo
# Password check and hashing
from werkzeug.security import generate_password_hash, check_password_hash
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
# ├── config.py
├── requirements.txt
└── run.py     # (app.py)
```
