from datetime import date, datetime

def formatDate(date):
    return '{}年{}月{}日（{}）'.format(
        date.year, 
        date.month, 
        date.day, 
        ['月','火','水','木','金','土','日'][date.weekday()])

def formatDateTime(time):
    return '西暦{}年（平成{}年）{}月{}日（{}）　{}時{}分{}秒'.format(
        time.year, 
        time.year - 1988,
        time.month, 
        time.day, 
        ['月','火','水','木','金','土','日'][time.weekday()],
        time.hour,
        time.minute,
        time.second)