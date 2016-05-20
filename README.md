## Accountable Politics
[https://accountable-politics.herokuapp.com/](https://accountable-politics.herokuapp.com/)

### Setup

This assumes you're running OSX and already have [Homebrew](http://brew.sh/) installed as well as an [ssh key added to your github account](https://help.github.com/articles/generating-an-ssh-key/).

	brew install python3
	pip install invoke
	xcode-select --install
	git clone git@github.com:mattdmayberry/accountable-politics.git
	cd accountable_politics
	pyvenv env
	source env/bin/activate
	invoke install

This installs python3, the [invoke utility](https://github.com/pyinvoke/invoke), xcode, and clones the app repository. It also sets up a virtual environment for the app, and installs all the python dependencies into the virtual environment.	

### Dependencies

	bcrypt==2.0.0
	cffi==1.6.0
	Flask==0.10.1
	Flask-Bcrypt==0.7.1
	Flask-Login==0.3.2
	Flask-WTF==0.12
	gunicorn==19.5.0
	heroku==0.1.4
	itsdangerous==0.24
	Jinja2==2.8
	MarkupSafe==0.23
	peewee==2.8.1
	pycparser==2.14
	python-dateutil==1.5
	requests==2.10.0
	six==1.10.0
	Werkzeug==0.11.9
	WTForms==2.1

### Running Tests
!! NEED TO UPDATE THIS SECTION WITH TESTING INFO !!
First, install PhantomJS (`brew install phantomjs`).

Run `invoke test` from the project directory will run every test.

### Running Locally

Run `invoke serve` from the project directory to run locally.

This will run the project on [port 8000](http://localhost:8000/).

### Setting up PyCharm

[PyCharm](https://www.jetbrains.com/pycharm/) is an IDE from Jetbrains for python. It can be installed by running `brew cask install pycharm`.

Open pycharm, input a license, and select to install the command line tool. Then, open the project in pycharm by running `charm` . from the project directory. Wait for pycharm to load it, and then you're good to go! Jetbrains offers [free licences](https://www.jetbrains.com/student/) to students for all of their products.

Make sure to change the python tests configuration for nosetests (Edit Configurations -> Python Tests -> Nosetests) so that the working directory is the project directory (not the test directory!)

You may need to ensure that phantomjs is in your PyCharm PATH. One way to do this is to symlink it into the project's env/bin folder (for example `ln -s /usr/local/bin/phantomjs env/bin`)

### Using Git

See [Github's documentation](https://help.github.com/). The project team prefers to commit directly to master, with small-ish commits. that always have passing tests.
