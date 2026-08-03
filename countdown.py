import argparse
import calendar
import os
from datetime import date

import requests 

topic = os.environ.get("NTFY_TOPIC", "countInt-alertsApril")


def send_ntfy(topic, message, title="Start Grinding"):
    requests.post(
        f"https://ntfy.sh/{topic}",
        data=f"{message}".encode(encoding="utf-8"),
        headers={
            "Title": title,
            "Actions": "view, Debrief, https://tecanmol.github.io/Debrief/",
        },
    )


def days_until_monthEnd():
    today = date.today()
    last_day = calendar.monthrange(today.year, today.month)[1]  # e.g. 31 for Aug, 30 for Sep
    target = date(today.year, today.month, last_day)
    return (target - today).days, target


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--test",
        action="store_true",
        help="Send a one-off test notification instead of the real countdown",
    )
    args = parser.parse_args()

    if args.test:
        send_ntfy(
            topic,
            "✅ Countdown notifier is wired up and will run on schedule from here.",
            title="Test ping",
        )
        return

    days_left, target = days_until_monthEnd()
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