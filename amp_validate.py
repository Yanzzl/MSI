import json
import re
import subprocess
import sys
import csv
from subprocess import call
from urllib import request

import urllib3
from bs4 import BeautifulSoup
import requests
import lxml
# from urllib3 import request


def validator(url):
    # url = requests.get("https://www.newegg.com/")
    # if 'www.' not in url:
    #     url = 'www.' + url
    temp = url
    if 'http://' not in url and 'https://' not in url:
        url = 'http://' + url
    # try:
    # http = urllib3.PoolManager()
    # res = http.request("GET", url)
    # print("res ：{}".format(res.url))
    # print("add https :{}".format(url))
    # # print(re.findall("<title>(.*?)</title>", res))
    # url = request.urlopen(url).geturl()
    # print("new url is {}".format(url))
    # except:
    #     print("invalid url at request: {}".format(url))
    #     return -1
    try:
        # url = requests.get(url)
        # html_text = url.text
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"}

        # hdr = {
        #     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        #     'Accept-Encoding': 'gzip,deflate,sdch',
        #     'Accept-Language': 'en-US,en;q=0.8',
        #     'Connection': 'keep-alive'
        # }
        url = request.Request(url)
        url.add_header("User-Agent",
                       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE")

        html_text = request.urlopen(url, timeout=3)
        soup = BeautifulSoup(html_text, "html.parser")
        # soup = BeautifulSoup(html_text, "lxml")
        tags = soup.find_all('link')
        tags2 = soup.find_all('html')
        for tag in tags2:
            if 'amp' in tag.attrs or "⚡" in tag.attrs:
                return 1
        for tag in tags:
            values = tag.attrs['rel']
            for value in values:
                if value == 'amphtml':
                    return 2
    except:
        if 'https://' not in temp:
            url = 'https://' + temp
        try:

            url = request.Request(url)
            url.add_header("User-Agent",
                           "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36")

            html_text = request.urlopen(url, timeout=3)
            soup = BeautifulSoup(html_text, "html.parser")
            # soup = BeautifulSoup(html_text, "lxml")
            tags = soup.find_all('link')
            tags2 = soup.find_all('html')
            for tag in tags2:
                if 'amp' in tag.attrs or "⚡" in tag.attrs:
                    return 1
            for tag in tags:
                values = tag.attrs['rel']
                for value in values:
                    if value == 'amphtml':
                        return 2
        except:
            print("invalid url: {}".format(url.get_full_url()))
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
            # url = row["url"]
            url = row["Domain"]
            row_number += 1
            if row_number % 1000 == 0:
                print ("ROW " + str(row_number))
            print(url)
            # print(request.urlopen(url).geturl())
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






