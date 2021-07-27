************************************
            test for e.Kom
************************************

searching in databse by POST request


************************************
************************************
main.py is FastApi app
request.py is a script to test app
templastes.json is a database file for TinyDB
pip_requirments.txt is packeges to install 
************************************



1. clone repository


2. create env: 
"python3 -m venv env" 

and activate it: 
"source ./env/bin/activate"

3. install modules from pip_requirements.txt:
"pip install -r pip_requirements.txt"


4. run uvicorn on 0.0.0.0
"uvicorn main:app --reload --host 0.0.0.0"

uvicorn listening to port 8000


5. set url in request.py like:
url = "http://127.0.0.1:8000"

request.py is a script to test app

6. run request.py script
