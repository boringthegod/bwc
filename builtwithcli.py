import os
import requests
from bs4 import BeautifulSoup
import re
import argparse
from datetime import datetime

def fetch_data(domain, cookie_or_path):
    if os.path.isfile(cookie_or_path):
        with open(cookie_or_path, 'r') as file:
            cookie = file.read().strip()
    else:
        cookie = cookie_or_path
    url = f'https://builtwith.com/relationships/{domain}'
    headers = {
        'Cookie': 'BWSSON='+cookie
    }
    response = requests.get(url, headers=headers)
    return response.text

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    script = soup.find('script', string=re.compile('function drawChart'))
    domain_dates = {}
    if script:
        data = re.findall(r'\[\'(.*?)\',\'(.*?)\',new d\((\d+), (\d+), (\d+)\),new d\((\d+), (\d+), (\d+)\)\]', script.string)
        for domain, ip, start_year, start_month, start_day, end_year, end_month, end_day in data:
            end_date = datetime(int(end_year), int(end_month) + 1, int(end_day))
            if domain not in domain_dates or end_date > domain_dates[domain]:
                domain_dates[domain] = end_date

    return domain_dates

def is_domain_active(domain):
    try:
        response = requests.get(f'http://{domain}', timeout=5)
        return 200 <= response.status_code < 300
    except requests.RequestException:
        return False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--domain', required=True, help="Domain to search")
    parser.add_argument('-c', '--cookie', required=True, help="Cookie or path to cookie file")
    args = parser.parse_args()

    html = fetch_data(args.domain, args.cookie)
    domain_dates = parse_html(html)

    sorted_domains = sorted(domain_dates.items(), key=lambda x: x[1], reverse=True)

    for domain, date in sorted_domains:
        if is_domain_active(domain):
            print(f"https://{domain} - {date.strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    main()
