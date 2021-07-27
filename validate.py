""""valid phone : '+7 999 777 33 44' """
""""valid date : 'DD.MM.YYYY' or 'YYYY-MM-DD' """
"""valid email:  'user@user.com' """
import re

def valid_phone(phone):
    r = re.compile(r"^(\+[7])[ ]([0-9]{3})[ ]([0-9]{3})[ ]([0-9]{2})[ ]([0-9]{2})$")
    if r.search(phone):
        return True
    return False

def valid_email(email):
    r = re.compile(r"^[a-zA-Z0-9]{1,100}[@][a-z]{1,7}\.[a-z]{2,5}$")
    if r.search(email):
        return True
    return False

def valid_date(date):
    r1 = re.compile(r"^(0[1-9]|1[0-9]|2[0-9]|3[01]).(0[1-9]|1[012]).[0-9]{4}$")
    r2 = re.compile(r"^[0-9]{4}-(0[1-9]|1[012])-(0[1-9]|1[0-9]|2[0-9]|3[01])$")
    if r1.search(date) or r2.search(date):
        return True
    return False  

def get_type(data):
    if valid_date(data):
        return 'date'
    elif valid_phone(data):
        return 'phone'
    elif valid_email(data):
        return 'email'
    else:
        return 'text'
