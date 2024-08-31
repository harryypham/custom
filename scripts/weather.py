import os
import sys
from bs4 import BeautifulSoup

BOLD = '\033[1m'
RESET = '\033[0m'
EXTRA_ATTRS = ["High/Low", "Wind", "Humidity", "Dew Point", "Pressure", "UV Index", "Visibility", "Moon Phase"]
ALL_FLAG = len(sys.argv) > 1 and '-a' in sys.argv

if "-h" in sys.argv:
    print("usage: weather [-a]")
    sys.exit(0)

if not os.path.exists('weather.html'):
    sys.stderr.write('Error: weather.html not found\n')
    sys.exit(1)

# Extract weather information from html file
soup = BeautifulSoup(open('weather.html', encoding='utf-8'), 'html.parser')
location = soup.find('h1')
temp = soup.find('span', attrs={'data-testid': 'TemperatureValue'})
state = soup.find('div', attrs={'data-testid': 'wxPhrase'})
warnings = soup.select('a > h2')
if ALL_FLAG:
    extra_cols = soup.find_all('div', attrs={'data-testid': 'wxData'})
    extra_infos = [col.text for col in extra_cols]

    extra_infos[1] = extra_infos[1].strip("Wind Direction")
    extra_infos[4] = extra_infos[4].strip("Arrow Down")

# Display weather information
print("-"* 54)
print("|" + f"{BOLD}Weather for {location.text}{RESET}".center(60) + "|")
print("|".ljust(53) + "|")
print(f"| + Temperature: {temp.text}".ljust(53) + "|")
print(f"| + Condition: {state.text}".ljust(53) + "|")
for w in warnings:
    print(f"| + {w.text}".ljust(53) + "|")
if ALL_FLAG:
    for i, attr_name in enumerate(EXTRA_ATTRS):
        print(f"| + {attr_name}: {extra_infos[i]}".ljust(53) + "|")
print("|".ljust(53) + "|")
print("-"* 54)
