header:
	@echo "work with doses-drug-imc"

install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt
install-aws:
	pip install --upgrade pip &&\
	pip install -r requirements-aws.txt
install-gcloud:
	pip install --upgrade pip &&\
	pip install -r requirements-gcloud.txt
install-azure:
	pip install --upgrade pip &&\
	pip install -r requirements-azure.txt
install-space:
	pip install --upgrade pip &&\
	pip install -r requirements-space.txt
format:
	black *.py

lint:
	pylint --disable=R,C main.py

test:
	python -m pytest -vv --cov=main test_main.py

all: install lint test right

build:
	docker build . -t doses-drug-imc 

run:
	#docker run -it -p 127.0.0.1:8000:8000 --name doses-drug-imc doses-drug-imc sh 
	docker run -p 127.0.0.1:8000:8000 --name doses-drug-imc doses-drug-imc
	
start:
	docker start doses-drug-imc

exe:
	docker exec -it doses-drug-imc sh
right:
	@echo "Hello, All right" 