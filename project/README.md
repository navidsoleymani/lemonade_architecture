# website-backend

# Add Translator
python manage.py makemessages --all --ignore=env


pip uninstall gando -y && pip install gando && pip freeze > requirements.txt  && python manage.py makemigrations && python manage.py migrate && python manage.py makemessages --all --ignore=env && python manage.py compilemessages --ignore=env 
