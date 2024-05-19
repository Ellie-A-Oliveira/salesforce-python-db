from datetime import datetime

def dateformat(date):
    return datetime.strptime(date, "%Y-%m-%d")