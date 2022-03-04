import os,datetime
def get_creationtime(file):
    time_c = os.path.getctime(file)
    return time_c
def get_creationtime_as_datetime(timestamp):
    date = datetime.datetime.fromtimestamp(timestamp)
    formated_date = date.strftime(r"%d.%m.%Y %H:%M:%S")
    return (date,formated_date)