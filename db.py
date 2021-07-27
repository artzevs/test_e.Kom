from tinydb import TinyDB
from tinydb.queries import Query, where


db = TinyDB('templates.json')

def dbSearch(field_names : list):
    res = ""
    for field in field_names:
        if res:
            res+=" & "
        res += f"where('{field}').exists()"
    return db.search(eval(res))

# item1 = {
#     "name" : "template1",
#     "fieldEmail" : "email",
#     "fieldPhone" : "phone",
#     "fieldDate" : "date"
# }

# item2 = {
#     "name" : "template2",
#     "field_email" : "email",
#     "field_phone" : "phone",
#     "field_date" : "date",
#     "field_text" : "text"
# }

# item3 = {
#     "name" : "Form template 3",
#     "f_email" : "email",
# }


# def insert():
#     db.insert(item1)
#     db.insert(item2)
#     db.insert(item3)
