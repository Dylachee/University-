run:
	python3 manage.py runserver
migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

kill:
	sudo fuser -k 8000/tcp

craete:
	python3 manage.py createsuperuser