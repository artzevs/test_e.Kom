import requests


url = 'http://127.0.0.1:8000' 
end_point = "/get_form"

data = [
    "f_email=anyuser@user.com",
    "field_email=user@mail.su",
    "field_phone=+7 999 444 55 66&field_email=user@mail.su",
    "field_phone=+7 999 444 55 66&f_email=anyuser@user.com",
    "fieldEmail=user@mail.su&fieldPhone=+7 999 444 55 66&fieldDate=2000-12-31",
    "fieldEmail=user@mail.su&fieldPhone=+7 999 444 55 66&fieldDate=2000-13-31",
]

for item in data:
    r = requests.post(url+end_point, data=item)    
    print(r.json())