# Documentation for SingHeath Retail Management Webapp Backend (C1G4)

## Running locally for dev: localhost:8000

Step 1: Clone the repo

Step 2: Install and activate your venv for python

Run the following command

```
>>pip install -r requirements.txt
```

Step 3: Install posgress, create a database and modify the database section in settings.py

Step 4: run the following commands in venv and the project dir

```
>>python manage.py makemigrations
>>python manage.py migrate
>>python manage.py runserver
```

Step 5: go to browser : localhost:8000/api/

