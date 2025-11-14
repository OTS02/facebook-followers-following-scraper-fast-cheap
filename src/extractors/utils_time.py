thonfrom datetime import datetime

def timestamp_now():
    return datetime.utcnow().isoformat()