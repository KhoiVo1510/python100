calendar = {"jan": [31, 1], "feb": [28, 2], "mar": [31, 3], "apr": [30, 4], "may": [31, 5], "june": [30, 6],\
            "july": [31, 7], "aug": [31, 8], "sept": [30, 9], "oct": [31, 10], "nov": [30, 11], "dec": [31, 12]}

def check_month(month):
    if month in calendar.keys():
        return True
    return False

def check_date(month, day):
    if month not in calendar.keys():
        return False
    if not(day.isdigit()):
        return False
    if int(day) > calendar[month][0] or int(day) == 0:
        return False
    return True

def cal_days(month, day):
    total_days = -1
    if check_date(month, day):
        for i in range(calendar[month][1] - 1):
            total_days += calendar[month][0]
        total_days += int(day)
        print(f"Total days since 1 Jan = {total_days} days")
    else:
        print("Type again.")

date = input("Type date(Ex: 15 Oct): ")

date = date.split()

cal_days(date[1].lower(), date[0])
