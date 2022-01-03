'''
DECORAOTRS
def div(a, b):
    print(a/b)


def smart_div(func):

    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)

    return inner


div1 = smart_div(div)
div1(2, 4)
'''

'''
__name__ is a special variable only used to denote the name of module
When the file is currently run __name__ is __main__
However if it is imported in some other file and then that file is imported as module, __name__ is the module name
It can be used to check if it is the first file that is being currently executed - 
if __name__ == "__main__":
    main()
'''

'''
Classes and Objects
Classes are blueprints for Objects
Objects have Attributes(variables) and Behaviour(methods[functions])

class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is ", self.cpu, self.ram)

com1 = Computer("i5", 16)
com2 = Computer("Ryzen", 8)
# __init__ function called by default at the time of Object Creation
# com1 passed as paramter also automatically

Computer.config(com1)
Computer.config(com2)

OR

com1.config()
com2.config()
# In above line com1 gets passed as a parameter to self automatically
'''

'''
Also called “formatted string literals,” f-strings are string literals that have an f at the beginning and curly braces containing expressions that will be replaced with their values.
The expressions are evaluated at runtime and then formatted using the __format__ protocol.
name = "Eric"
age = 74
f"Hello, {name}. You are {age}."
'Hello, Eric. You are 74.'
'''

'''
SQLAlchemy is an ORM - Object Relational Mapper which allows us to access the database in an easy to use object
oriented manner. It also allows to use different databases without changing the Python code. So if you want to use
SQLite Database for testing and Postgres database for production then all you need to do is pass in a different 
database URL for SQLAlchemy to connect to, but all the code to create the database will be the same.
'''

'''
The following can be run in the command line for testing the database and running some queries 

$python
Python 3.7.4 (default, Aug 13 2019, 20:35:49) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from flaskblog import db 
/home/subham/anaconda3/lib/python3.7/site-packages/flask_sqlalchemy/__init__.py:835: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
  'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
>>> db.create_all()
>>> from flaskblog import User, Post
>>> user_1 = User(username='Subham',email='subham@demo.com',password='password')
>>> db.session.add(user_1)
>>> user_2 = User(username='JohnDoe',email='jd@demo.com',password='password')
>>> db.session.add(user_2)
>>> db.session.commit()
>>> User.query.all()
[User('Subham','subham@demo.com','default.jpg'), User('JohnDoe','jd@demo.com','default.jpg')]
>>> User.query.first()
User('Subham','subham@demo.com','default.jpg')
>>> User.query.filter_by(username='Subham').all()
[User('Subham','subham@demo.com','default.jpg')]
>>> User.query.filter_by(username='Subham').first()
User('Subham','subham@demo.com','default.jpg')
>>> user = User.query.filter_by(username='Subham').first()
>>> user
User('Subham','subham@demo.com','default.jpg')
>>> user.id
1
>>> user = User.query.get(1)
>>> user
User('Subham','subham@demo.com','default.jpg')
>>> user.posts
[]
>>> user.id
1
>>> posts_1 = Post(title='Blog 1',content='First Post Content!',user_id=user.id)
>>> posts_2 = Post(title='Blog 2',content='Second Post Content!',user_id=user.id)
>>> db.session.add(posts_1)
>>> db.session.add(posts_2)
>>> db.session.commit()
>>> user.posts
[User('Blog 1','2020-03-14 06:45:03.904100'), User('Blog 2','2020-03-14 06:45:03.906327')]
>>> for post in user.posts:
...     print(post.title)
... 
Blog 1
Blog 2
>>> post = Post.query.first()
>>> post
User('Blog 1','2020-03-14 06:45:03.904100')
>>> post.user_id
1
>>> post.author
User('Subham','subham@demo.com','default.jpg')
>>> db.drop_all() #This was used to delete all table and all rows
>>> db.create_all() #This would have created the table structure as original
'''

'''
So why does it fail and give ImportError on User import if you are NOT putting the line "from models import User, Post" below "db = SQLAlchemy(app)??
So here there is problem of Circular Imports
So it sees flaskblog file and import User from models module
NOTE: ANYTIME PYTHON IMPORTS SOMETHING FROM MODULE, IT STILL RUNS THE ENTIRE MODULE!!!
So when it tries to run the entire models module, then it tries to perform its imports, so it then it goes to that line which says from flaskblog import db
but db variable has still not been declared, so it should fail on the db import but it doesn't do that it fails on the User import
So what's happening here is when we are running the script from command line using Python, Python calls the name of the script __main__ which we have specified at the bottom.
So now it goes and runs, encounters from models... statement and then in models file it encounter from flaskblog, but PYTHON HASN'T SEEN FLASKBLOG STILL AS IT HAS NAMED IT __main__.
So it runs the flaskblog for a 2nd time from the beginning, so it comes and redoes all of the stuff, thus it says that I have seen the models module but I don't know what the User class is bcoz it is below in the models module.


So the above problem could be fixed by putting the line "from models import User, Post" below "db = SQLAlchemy(app)"
But this does not allow the creation of database using db.create_all()

So the universal solution to this is to set up our code such that we are not running flaskblog directly.
To do this we need to convert our application into package, which can be done by creating a __init__ file.

The __init__ file is where we will initialize our application and bring together different components.

When you are working with packages, that is going to import from __init__.py file within that package, so that app VARIABLE MUST HAVE TO EXIST WITHIN THE __init__.py file 
When importing use package_name.module_name for importing from specific modules
'''

'''
For Hashing passwords a package called flask-bcrypt is used
>>> from flask_bcrypt import Bcrypt
>>> bcrypt = Bcrypt()
>>> bcrypt.generate_password_hash('testing')
b'$2b$12$Qd6aS30Lz6oToARXtTAUg.Y0cWJ6Qmfyhw9ujK4QTrivZTouG7/5m'

#Everytime decoding gives a different hash value
>>> bcrypt.generate_password_hash('testing').decode('utf-8')
'$2b$12$eK5drSUeTyz2LaEU1avkiuaSVJXULqF/wRVDQ380o/B0YudQnSo1W'
>>> bcrypt.generate_password_hash('testing').decode('utf-8')
'$2b$12$Kdni//ilJcVfJMkJIgT.wOzfHFdcCa31uxS07EiLe9IfPeUipgu8.'
>>> bcrypt.generate_password_hash('testing').decode('utf-8')
'$2b$12$du1CuqprEVQX4/lfJlLfPuravXwbfJ6TGVx0OvAA3ClLuJmPDdPSW'

#Thus passwords are checked using check_password_hash() method
>>> hashed_pw = bcrypt.generate_password_hash('testing').decode('utf-8')
>>> bcrypt.check_password_hash(hashed_pw, 'password')
False
>>> bcrypt.check_password_hash(hashed_pw, 'testing')
True
'''

'''
How validate_username() and validate_email() are being called, these functions are called with the FlaskForm class that our RegistrationForm class inherited from. 
If you look at the definition for validate_on_submit(), and from there, the definition for validate(), that validate function contains the following line:
inline = getattr(self.__class__, 'validate_%s' % name, None)
There is a lot going on in the background, but from what I can tell, Flask is checking for extra functions created with the naming pattern: "validate_(field name)", and later calling those extra functions.
'''

'''
So why does a message like "Confirm Resubmission" pop up in your browser??
Because your browser is telling that you are about to run another POST request when you reload your page,
so us redirecting causes the browser to send a GET request and then we don't get that
'''

'''
If you just want to throw away a variable in Python then use the _ as a variable
'''
