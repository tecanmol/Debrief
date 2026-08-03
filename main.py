import requests
from datetime import date   
import calendar

topic = "countInt-alertsApril"


def send_ntfy(topic,message):
    requests.post(f"https://ntfy.sh/{topic}",
    data=f"{message}".encode(encoding='utf-8'),
    headers={ "Title": "Start Grinding",
             "Actions": "view, Debrief, https://tecanmol.github.io/Debrief/"})
    
    
def days_until_monthEnd():
    today = date.today()
    last_day = calendar.monthrange(today.year, today.month)[1]  # e.g. 31 for Aug, 30 for Sep
    target = date(today.year, today.month, last_day)
    return (target - today).days, target
    
def main():
    days_left,target   = days_until_monthEnd()
    target_str = f"{target.strftime('%B')} {target.day}"
    
    if days_left == 0:
        message = f"Today is {target_str} ⁉️"
    elif days_left == 1:
        message = f"⏳ 1 day left until {target_str}!"
    else:
        message = f"⏳ {days_left} days left until {target_str}!"

    send_ntfy(topic, message)
    
if __name__ == "__main__":
    main()