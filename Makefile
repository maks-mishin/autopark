MANAGE := python manage.py

run:
	@$(MANAGE) runserver

setup: db-clean migrate

migrate:
	@$(MANAGE) makemigrations
	@$(MANAGE) migrate

install:
	pip install -r requirements.txt

db-clean:
	@rm db.sqlite3 || true

shell:
	@$(MANAGE) shell_plus --ipython

lint:
	isort motor_pool vehicle
	flake8 motor_pool vehicle

super:
	@$(MANAGE) createsuperuser

data:
	@$(MANAGE) generate_data 1 10 5