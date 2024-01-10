from datetime import datetime

def convert_date(timestamp):
    timestamp = str(timestamp)
    timestamp = timestamp.split('+')[0]
    dt_object = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
    return dt_object
