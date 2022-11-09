# Todo list API

This is a Todo list API implemented using the Django and Django Rest Framework (DRF)


### How to setup locally
#### Requirements

- Python3.7
- pip3
- virtualenv


#### setup instructions

- pull the project using git
cmd
   git clone https://github.com/Maveronic/djangotodorestapi.git
   
### For Windows users, open cmd, to the directory where you want to start the project
- create   a virtualenv using python -m venv {filename}
- activate it 
with
   {filename}\Scripts\activate

- install dependencies from the requirements.txt file
cmd
   pip install -r requirements.txt
   

- migrate the database tables
cmd
   python manage.py migrate
   
- start a development server using 
cmd
   python manage.py runserver
   
# djangoresttodoo