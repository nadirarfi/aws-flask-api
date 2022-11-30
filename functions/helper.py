import datetime

def handle_datetime_values(obj:dict):
    for k, v in obj.items():
        if type(v) == datetime.datetime:
            obj.update({k: v.strftime("%m/%d/%Y, %H:%M:%S")}) 
    return obj