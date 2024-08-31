import os
import sys
from bs4 import BeautifulSoup

BOLD = '\033[1m'
RESET = '\033[0m'

if not os.path.exists('weather.html'):
    sys.stderr.write('Error: weather.html not found\n')
    sys.exit(1)

soup = BeautifulSoup(open('weather.html', encoding='utf-8'), 'html.parser')
location = soup.find('h1')
temp = soup.find('span', attrs={'data-testid': 'TemperatureValue'})
state = soup.find('div', attrs={'data-testid': 'wxPhrase'})
warnings = soup.select('a > h2')

print("-"* 54)
print("|" + f"{BOLD}Weather for {location.text}{RESET}".center(60) + "|")
print(f"| + Temperature {temp.text}".ljust(53) + "|")
print(f"| + Condition: {state.text}".ljust(53) + "|")
for w in warnings:
    print(f"| + {w.text}".ljust(53) + "|")
print("-"* 54)
