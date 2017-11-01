
https://superset.incubator.apache.org/installation.html#getting-started



sudo apt-get install build-essential libssl-dev libffi-dev python-dev python-pip libsasl2-dev libldap2-dev


pip install virtualenv

virtualenv venv
. ./venv/bin/activate


pip install --upgrade setuptools pip



# Install superset
pip install superset

# Create an admin user (you will be prompted to set username, first and last name before setting a password)
fabmanager create-admin --app superset

# Initialize the database
superset db upgrade

# Load some data to play with
superset load_examples

# Create default roles and permissions
superset init

# Start the web server on port 8088, use -p to bind to another port
superset runserver

# To start a development web server, use the -d switch
# superset runserver -d



