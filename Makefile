dev-install:
	pip install -r tradi/requirements.txt
	pip install -r tradi/requirements-dev.txt

fmt:
	isort .
	black .

lint:
	flake8 .
	mypy .

tag:
	git for-each-ref --sort=-creatordate --format '%(refname:short)' refs/tags | head -n 1
	@read -p "Enter tag name: " tag_name; \
	git tag -a "v$$tag_name" -m "v$$tag_name" && git push origin "v$$tag_name"

runserver:
	python tradi/manage.py runserver

makemigrations:
	python tradi/manage.py makemigrations

migrate:
	python tradi/manage.py migrate

shell:
	python tradi/manage.py shell
