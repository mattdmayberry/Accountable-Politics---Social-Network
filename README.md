## Accountable Politics
[http://accountable-politics.herokuapp.com/](http://accountable-politics.herokuapp.com/)

### Setup

This assumes you're running OSX and already have [Homebrew](http://brew.sh/) installed as well as an [ssh key added to your github account](https://help.github.com/articles/generating-an-ssh-key/).

	brew install python3
	xcode-select --install
	git clone git@github.com:mattdmayberry/accountable.git
	cd accountable
	pyvenv env
	source env/bin/activate
	pip install -r requirements.txt

This installs python3, xcode, and clones the app repository. It also sets up a virtual environment for the app, and installs all the python dependencies into the virtual environment.	

### Dependencies
	alembic==0.8.6
    bcrypt==2.0.0
    cffi==1.6.0
    Flask==0.10.1
    Flask-Bcrypt==0.7.1
    Flask-Login==0.3.2
    Flask-Migrate==1.8.0
    Flask-Script==2.0.5
    Flask-SQLAlchemy==2.1
    Flask-WTF==0.12
    gunicorn==19.5.0
    heroku==0.1.4
    itsdangerous==0.24
    Jinja2==2.8
    Mako==1.0.4
    MarkupSafe==0.23
    peewee==2.8.1
    postgresql==9.5.3 // Not included in Requirements.txt but may be needed for Windows OS users
    psycopg2==2.6.1
    pycparser==2.14
    python-dateutil==1.5
    python-editor==1.0
    requests==2.10.0
    six==1.10.0
    SQLAlchemy==1.0.13
    urlparse3==1.0.8
    Werkzeug==0.11.9
    WTForms==2.1


### Running Tests
There are three unit test files provided in the project directory: test_app.py, test_models.py, and test_forms.py. To run the tests on the command line, the format is: `python test_models.py`
Example output from test_models.py:

	```
	$ python3 test_models.py
	Initializing Test Instances...
	> Creating Users: User1 created, User2 created
	> Creating Posts: post1 created, post2 created
	> Creating Relationship: User1 following User2
	..................Deleting Test Instances
	
	----------------------------------------------------------------------
	Ran 18 tests in 1.639s
	
	OK
	```

For more detail on each test that is running add `-v` for verbose output: `python test_app.py -v`.
	
	```
	$ python3 test_models.py -v
	Initializing Test Instances...
	> Creating Users: User1 created, User2 created
	> Creating Posts: post1 created, post2 created
	> Creating Relationship: User1 following User2
	test_post_content (__main__.Test_Models) ... ok
	test_post_created (__main__.Test_Models) ... ok
	test_post_timestamp (__main__.Test_Models) ... ok
	test_relationship_created (__main__.Test_Models) ... ok
	test_relationship_from_user (__main__.Test_Models) ... ok
	test_relationship_to_user (__main__.Test_Models) ... ok
	test_user_attribute_admin (__main__.Test_Models) ... ok
	test_user_attribute_email (__main__.Test_Models) ... ok
	test_user_attribute_joined_at (__main__.Test_Models) ... ok
	test_user_attribute_password (__main__.Test_Models) ... ok
	test_user_attribute_username (__main__.Test_Models) ... ok
	test_user_created (__main__.Test_Models) ... ok
	test_user_duplicate_email (__main__.Test_Models) ... ok
	test_user_duplicate_username (__main__.Test_Models) ... ok
	test_user_followers (__main__.Test_Models) ... ok
	test_user_following (__main__.Test_Models) ... ok
	test_user_get_posts (__main__.Test_Models) ... ok
	test_user_get_stream (__main__.Test_Models) ... ok
	Deleting Test Instances
	
	----------------------------------------------------------------------
	Ran 18 tests in 1.594s
	
	OK
	```
	
Ensure that the test_*.py file is in the same directory as the corresponding python file to be tested.

### Running Locally

Run `python app.py` from the project directory to run locally.

This will run the project on [port 5000](http://localhost:5000/).

### Setting up PyCharm

[PyCharm](https://www.jetbrains.com/pycharm/) is an IDE from Jetbrains for python. It can be installed by running `brew cask install pycharm`.

Open pycharm, input a license, and select to install the command line tool. Then, open the project in pycharm by running `charm` . from the project directory. Wait for pycharm to load it, and then you're good to go! Jetbrains offers [free licences](https://www.jetbrains.com/student/) to all of their products for academic users.


### Using Git

See [Github's documentation](https://help.github.com/). The project team prefers to commit directly to master, with small-ish commits. that always have passing tests. 
