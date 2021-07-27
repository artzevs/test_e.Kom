from fastapi import FastAPI, Request
import json

from starlette.responses import Response
import db
from validate import get_type

def get_fields(dict : dict):
    return list(dict.keys())

app = FastAPI()


def check_data_type(req_dict:dict, db_dict):
    for key, value in req_dict.items():
        if get_type(value) != db_dict[key]:
            return False
    return True


@app.post("/get_form")
async def root(item : Request):
    args_binary = await item.body() 
    try:
        req = args_binary.decode().replace('=', '&').split('&')
        req_dict = {req[i]: req[i+1] for i in range(0, len(req), 2)}
        field_keys = list(req_dict.keys())

        res = db.dbSearch(field_keys)
        if (res and check_data_type(req_dict, res[0])):
            response = json.dumps({"name" : res[0]['name']})
        else:
            response= json.dumps({key : get_type(value) for key , value in req_dict.items()})
    except Exception:
        response = "something went wrong"
    
    return Response(response)