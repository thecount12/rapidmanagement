# Rapid Management

Software for Think Tank Workspaces LLC

We needed our own internal scrum, agile, kanban whatever. As much as I love Jira. I will make my own.

### Setup

1. First clone repo git clone https://github.com/thecount12/rapidmanagement.git
2. go to that directory and run 
3. virtualenv -p /usr/local/bin/python3.7 ~/.rapidmanagement
3. source ~/.rapidmanagement/bin/activate
4. pip install -r requirements.txt

### First Steps

python manage.py makemigrations

python manage.py migrate

python manage.py makemigrations

hopefully no bugs other then getboostrap templates

python manage.py createsuperuser
follow: prompts

### setup basic project

1. create some test users
2. Go to member section and create resources
    * resources do not need start and stop date
3.  create member packages
4. create memberships. 