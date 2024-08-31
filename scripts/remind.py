import os
from datetime import datetime
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('title', type=str, help='Note to remind')
parser.add_argument('-b', '--body', type=str, dest="body", help='Body of the note')
parser.add_argument('-w', '--when', type=str, dest="when", help='When to remind. Format: YYYY-MM-DD HH:MM:SS')

args = parser.parse_args()
title, body, when = args.title, args.body, args.when
if len(when.split()) == 1:
    when_dt = datetime.strptime(when, "%Y-%m-%d")
    when = when_dt.strftime("%m/%d/%Y")
else:
    when_dt = datetime.strptime(when, "%Y-%m-%d %H:%M:%S")
    when = when_dt.strftime("%m/%d/%Y %H:%M:%S")
os.execv("/usr/bin/osascript", ["osascript", "-e", f'tell application "Reminders" to make new reminder with properties {{name:"{title}", body:"{body}", remind me date:date "{when}"}}'])
