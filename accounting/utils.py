from datetime import date

def formatDate(date):
    return '{}年{}月{}日（{}）'.format(
        date.year, 
        date.month, 
        date.day, 
        ['月','火','水','木','金','土','日'][date.weekday()])