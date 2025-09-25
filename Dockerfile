FROM python:alpine

WORKDIR /doses-drug-imc

COPY . /doses-drug-imc/

RUN pip install --no-cache-dir --upgrade -r /doses-drug-imc/requirements-docker.txt \
    && apk add git make zsh \
    && sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
    




#CMD ["0.0.0.0", "--port", "8000"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

