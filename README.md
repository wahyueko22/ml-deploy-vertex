

Getting started
Requirements
Python 3.10 or latest
How to run locally
setup virtual environemnt

 python -m venv env
activate virtual environment

Windows

./env/Scripts/activate
Mac / Linux

source ./env/bin/activate
install required dependencies

 pip install -r requirements.txt


 uvicorn main:app --reload