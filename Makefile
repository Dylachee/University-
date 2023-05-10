run:
	venv/bin/python manage.py runserver

migrate:
	venv/bin/python manage.py makemigrations
	venv/bin/python manage.py migrate

kill:
	sudo fuser -k 8000/tcp

create:
	venv/bin/python manage.py createsuperuser --username admin --email admin@admin.com
