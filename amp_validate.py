import json
import subprocess
import sys
import csv
from subprocess import call
from bs4 import BeautifulSoup
import requests



def validator(url):
    # url = requests.get("https://www.newegg.com/")
    if 'www.' not in url:
        url = 'www.' + url
    if 'https://' not in url:
        url = 'https://' + url
    try:
        url = requests.get(url)
        html_text = url.text
        soup = BeautifulSoup(html_text, "html.parser")
        tags = soup.find_all('link')
        tags2 = soup.find_all('html')
        for tag in tags2:
            if 'amp' in tag.attrs:
                return 1
        for tag in tags:
            values = tag.attrs['rel']
            for value in values:
                if value == 'amphtml':
                    return 2
    except:
        print("invalid url: {}".format(url))
        return -1
    return 0



if __name__ == '__main__':
    csv_path = "t.csv"
    fails = 0
    passes = 0
    have_amp_versions = 0
    invalid_url = 0
    row_number = 0
    with open(csv_path, newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        # reader = csv.reader(file, delimiter=',', quotechar='|')
        for row in reader:
            url = row["url"]
            row_number += 1
            if row_number % 1000 == 0:
                print ("ROW " + str(row_number))
            print(url)
            # print(validator(url))
            code = validator(url)
            print(code)
            if code == 1:
                passes = passes + 1
            elif code == 2:
                have_amp_versions = have_amp_versions + 1
            elif code == 0:
                fails = fails + 1
            else:
                invalid_url = invalid_url + 1
        print ("total passes: " + str(passes))
        print ("total fail: " + str(fails))
        print ("have amp versions: " + str(have_amp_versions))
        print ("Invalid url: " + str(invalid_url))






