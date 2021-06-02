import http
import json
import re
import socket
import subprocess
import sys
import csv
import urllib
from subprocess import call
from urllib import request, error
from http.cookiejar import CookieJar
import urllib3
from bs4 import BeautifulSoup
import requests
import lxml


# from urllib3 import request


# def validator(url):
#     # url = requests.get("https://www.newegg.com/")
#     # if 'www.' not in url:
#     #     url = 'www.' + url
#     temp = url
#     if 'http://' not in url and 'https://' not in url:
#         url = 'http://' + url
#     # try:
#     # http = urllib3.PoolManager()
#     # res = http.request("GET", url)
#     # print("res ：{}".format(res.url))
#     # print("add https :{}".format(url))
#     # # print(re.findall("<title>(.*?)</title>", res))
#     # url = request.urlopen(url).geturl()
#     # print("new url is {}".format(url))
#     # except:
#     #     print("invalid url at request: {}".format(url))
#     #     return -1
#     try:
#         # url = requests.get(url)
#         # html_text = url.text
#         headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"}
#
#         # hdr = {
#         #     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
#         #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#         #     'Accept-Encoding': 'gzip,deflate,sdch',
#         #     'Accept-Language': 'en-US,en;q=0.8',
#         #     'Connection': 'keep-alive'
#         # }
#
#         url = request.Request(url)
#         url.add_header("User-Agent",
#                        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE")
#
#         html_text = request.urlopen(url, timeout=3)
#         a = html_text.getcode()
#         print(a)
#         soup = BeautifulSoup(html_text, "html.parser")
#         # soup = BeautifulSoup(html_text, "lxml")
#         tags = soup.find_all('link')
#         tags2 = soup.find_all('html')
#         for tag in tags2:
#             if 'amp' in tag.attrs or "⚡" in tag.attrs:
#                 return 1
#         for tag in tags:
#             values = tag.attrs['rel']
#             for value in values:
#                 if value == 'amphtml':
#                     return 2
#     except:
#         if 'https://' not in temp:
#             url = 'https://' + temp
#         try:
#
#             url = request.Request(url)
#             url.add_header("User-Agent",
#                            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36")
#
#             html_text = request.urlopen(url, timeout=1)
#             a = html_text.getcode()
#             print(a)
#             soup = BeautifulSoup(html_text, "html.parser")
#             # soup = BeautifulSoup(html_text, "lxml")
#             tags = soup.find_all('link')
#             tags2 = soup.find_all('html')
#             for tag in tags2:
#                 if 'amp' in tag.attrs or "⚡" in tag.attrs:
#                     return 1
#             for tag in tags:
#                 values = tag.attrs['rel']
#                 for value in values:
#                     if value == 'amphtml':
#                         return 2
#         except:
#             # a = html_text.getcode()
#             # print(a)
#             print("invalid url: {}, error code: {}".format(url.get_full_url(), 1))
#             return -1
#
#
#
#
#
#
#
#     return 0


# def val(url):
#     try:
#         # url = request.Request(url)
#         # url.add_header("User-Agent",
#         #                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36")
#
#         req = urllib.request.Request(url, headers={
#             'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'})
#         html_text = request.urlopen(req, timeout=5).read()
#
#         # except:
#         #     print("invalid url: {}, timeout ".format(url.get_full_url()))
#         #     return -1
#         soup = BeautifulSoup(html_text, "html.parser")
#         # soup = BeautifulSoup(html_text, "lxml")
#         tags = soup.find_all('link')
#         tags2 = soup.find_all('html')
#         for tag in tags2:
#             if 'amp' in tag.attrs or "⚡" in tag.attrs:
#                 return 1
#         for tag in tags:
#             try:
#                 values = tag.attrs['rel']
#             except:
#                 pass
#             for value in values:
#                 if value == 'amphtml':
#                     return 2
#     # except urllib.error.URLError as e:
#     #     if hasattr(e, 'code'):  # 此时是HTTPError
#     #         print("invalid url: {}, error code: {}, error reason: {}".format(url.get_full_url(), e.code, e.reason))
#     #     elif hasattr(e, 'reason'):  # 此时是URLError
#     #         print("invalid url: {}, error reason: {}".format(url.get_full_url(), e.reason))
#     #     # print("invalid url: {}, error code: {}".format(url.get_full_url(), e.reason))
#     #     return -1
#     # except socket.timeout as e:
#     #     print("invalid url: {}, timeout ".format(url.get_full_url()))
#     #     return -1
#     except urllib.error.HTTPError as e:
#         print("e code : {}".format(e.code))
#         if e.status != 307:
#             raise  # not a status code that can be handled here
#         html_text = urllib.request.urlopen(redirected_url)
#         soup = BeautifulSoup(html_text, "html.parser")
#         # soup = BeautifulSoup(html_text, "lxml")
#         tags = soup.find_all('link')
#         tags2 = soup.find_all('html')
#         for tag in tags2:
#             if 'amp' in tag.attrs or "⚡" in tag.attrs:
#                 return 1
#         for tag in tags:
#             try:
#                 values = tag.attrs['rel']
#             except:
#                 pass
#             for value in values:
#                 if value == 'amphtml':
#                     return 2
#     except urllib.error.URLError as e:
#         if hasattr(e, 'code'):
#             print("invalid url: {}, error code: {}, error reason: {}".format(url, e.code, e.reason))
#         elif hasattr(e, 'reason'):  # 此时是URLError
#             print("invalid url: {}, error reason: {}".format(url, e.reason))
#         # print("invalid url: {}, error code: {}".format(url.get_full_url(), e.reason))
#         return -1
#     except socket.timeout as e:
#         print("invalid url: {}, timeout ".format(url))
#         return -1
#
#     return 0


def val(url):
    try:
        # url = request.Request(url)
        # url.add_header("User-Agent",
        #                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36")

        req = urllib.request.Request(url, headers={
            'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'})
        html_text = request.urlopen(req, timeout=5)

        # except:
        #     print("invalid url: {}, timeout ".format(url.get_full_url()))
        #     return -1
        soup = BeautifulSoup(html_text, "html.parser")
        # soup = BeautifulSoup(html_text, "lxml")
        tags = soup.find_all('link')
        tags2 = soup.find_all('html')
        for tag in tags2:
            if 'amp' in tag.attrs or "⚡" in tag.attrs:
                return 1
        for tag in tags:
            try:
                values = tag.attrs['rel']
            except:
                pass
            for value in values:
                if value == 'amphtml':
                    return 2
    # except urllib.error.URLError as e:
    #     if hasattr(e, 'code'):  # 此时是HTTPError
    #         print("invalid url: {}, error code: {}, error reason: {}".format(url.get_full_url(), e.code, e.reason))
    #     elif hasattr(e, 'reason'):  # 此时是URLError
    #         print("invalid url: {}, error reason: {}".format(url.get_full_url(), e.reason))
    #     # print("invalid url: {}, error code: {}".format(url.get_full_url(), e.reason))
    #     return -1
    # except socket.timeout as e:
    #     print("invalid url: {}, timeout ".format(url.get_full_url()))
    #     return -1
    except urllib.error.HTTPError as e:
        if e.code == 308:
            try:
                redirected_url = urllib.parse.urljoin(url, e.headers['Location'])
                print("redirect to: {}".format(redirected_url))
                html_text = urllib.request.urlopen(redirected_url)
                soup = BeautifulSoup(html_text, "html.parser")
                # soup = BeautifulSoup(html_text, "lxml")
                tags = soup.find_all('link')
                tags2 = soup.find_all('html')
                for tag in tags2:
                    if 'amp' in tag.attrs or "⚡" in tag.attrs:
                        return 1
                for tag in tags:
                    try:
                        values = tag.attrs['rel']
                    except:
                        pass
                    for value in values:
                        if value == 'amphtml':
                            return 2
            except:
                print("invalid url: {}, redirected failed".format(redirected_url))
                return -1
        else:
            print("invalid url: {}, error code: {}, error reason: {}".format(url, e.code, e.reason))
            return -1
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):  # 此时是HTTPError
            print("invalid url: {}, error code: {}, error reason: {}".format(url, e.code, e.reason))
        elif hasattr(e, 'reason'):  # 此时是URLError
            print("invalid url: {}, error reason: {}".format(url, e.reason))
        # print("invalid url: {}, error code: {}".format(url.get_full_url(), e.reason))
        return -1
    except socket.timeout as e:
        print("invalid url: {}, timeout ".format(url))
        return -1
    except http.client.HTTPException as e:
        print("invalid url: {}, HTTPException".format(url))
        return -1
    except:
        print("invalid url: {}, unknown issue".format(url))
        return -1

    return 0


def val_without_user_agent(url):
    try:
        # url = request.Request(url)
        # url.add_header("User-Agent",
        #                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36")

        # req = urllib.request.Request(url, headers={
        #     'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'})
        html_text = request.urlopen(url, timeout=5).read()

        # except:
        #     print("invalid url: {}, timeout ".format(url.get_full_url()))
        #     return -1
        soup = BeautifulSoup(html_text, "html.parser")
        # soup = BeautifulSoup(html_text, "lxml")
        tags = soup.find_all('link')
        tags2 = soup.find_all('html')
        for tag in tags2:
            if 'amp' in tag.attrs or "⚡" in tag.attrs:
                return 1
        for tag in tags:
            try:
                values = tag.attrs['rel']
            except:
                pass
            for value in values:
                if value == 'amphtml':
                    return 2
    # except urllib.error.URLError as e:
    #     if hasattr(e, 'code'):  # 此时是HTTPError
    #         print("invalid url: {}, error code: {}, error reason: {}".format(url.get_full_url(), e.code, e.reason))
    #     elif hasattr(e, 'reason'):  # 此时是URLError
    #         print("invalid url: {}, error reason: {}".format(url.get_full_url(), e.reason))
    #     # print("invalid url: {}, error code: {}".format(url.get_full_url(), e.reason))
    #     return -1
    # except socket.timeout as e:
    #     print("invalid url: {}, timeout ".format(url.get_full_url()))
    #     return -1

    except urllib.error.HTTPError as e:
        if e.code == 308:
            try:
                redirected_url = urllib.parse.urljoin(url, e.headers['Location'])
                print("redirect to: {}".format(redirected_url))
                html_text = urllib.request.urlopen(redirected_url)
                soup = BeautifulSoup(html_text, "html.parser")
                # soup = BeautifulSoup(html_text, "lxml")
                tags = soup.find_all('link')
                tags2 = soup.find_all('html')
                for tag in tags2:
                    if 'amp' in tag.attrs or "⚡" in tag.attrs:
                        return 1
                for tag in tags:
                    try:
                        values = tag.attrs['rel']
                    except:
                        pass
                    for value in values:
                        if value == 'amphtml':
                            return 2
            except:
                print("invalid url: {}, redirected failed".format(redirected_url))
                return -1
        else:
            print("invalid url: {}, error code: {}, error reason: {}".format(url, e.code, e.reason))
            return -1
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):  # 此时是HTTPError
            print("invalid url: {}, error code: {}, error reason: {}".format(url, e.code, e.reason))
        elif hasattr(e, 'reason'):  # 此时是URLError
            print("invalid url: {}, error reason: {}".format(url, e.reason))
        # print("invalid url: {}, error code: {}".format(url.get_full_url(), e.reason))
        return -1
    except socket.timeout as e:
        print("invalid url: {}, timeout ".format(url))
        return -1
    except  http.client.HTTPException as e:
        print("invalid url: {}, HTTPException".format(url))
        return -1
    except:
        print("invalid url: {}, unknown issue".format(url))
        return -1

    return 0


def validator(url):
    temp = url

    if 'http://' not in url and 'https://' not in url:
        tmp = 'http://' + url
        code = val(tmp)
        if code != -1:
            return code
        elif 'www.' not in url:
            print("try with www.")
            tmp = 'http://www.' + url
            code = val(tmp)
            return code

    else:
        code = val(url)
        return code


def validator_without_ua(url):
    print("test without user agent")
    if 'http://' not in url and 'https://' not in url:
        tmp = 'http://' + url
        code = val_without_user_agent(tmp)
        if code != -1:
            return code
        elif 'www.' not in url:
            print("try with www.")
            tmp = 'http://www.' + url
            code = val_without_user_agent(tmp)
            return code

    else:
        code = val_without_user_agent(url)
        return code


def getcode(url):
    code = validator(url)
    if code == -1:
        code = validator_without_ua(url)
    return code


if __name__ == '__main__':
    csv_path = "a.csv"
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
                print("ROW " + str(row_number))
            startRow = 3000
            endRow = 3005
            if row_number < startRow:
                continue
            if row_number >= endRow:
                break
            print("-----------------------------------")
            print(url)
            # print(request.urlopen(url).geturl())
            # print(validator(url))
            code = getcode(url)
            print(code)

            if code == 1:
                with open('passes {}.txt'.format(startRow), "a", encoding="utf-8") as passs:
                    passs.write('row number: {}  url: {}\n'.format(row_number, url))
                passes = passes + 1
            elif code == 2:
                with open('have amp version {}.txt'.format(startRow), "a", encoding="utf-8") as ampv:
                    ampv.write('row number: {}  url: {}\n'.format(row_number, url))
                have_amp_versions = have_amp_versions + 1
            elif code == 0:
                fails = fails + 1
            else:
                with open('invalid url {}.txt'.format(startRow), "a", encoding="utf-8") as invalid:
                    invalid.write('row number: {}  url: {}\n'.format(row_number, url))
                invalid_url = invalid_url + 1
            if (row_number % 100 == 0):
                with open('result {}.txt'.format(startRow), "a", encoding="utf-8") as result:
                    result.write('+++++++++++++++++++++++++++++++++\n')
                    result.write("total number: " + str(row_number - startRow) + '\n')
                    result.write("total fail: " + str(fails) + '\n')
                    result.write("total fail: " + str(fails) + '\n')
                    result.write("have amp versions: " + str(have_amp_versions) + '\n')
                    result.write("Invalid url: " + str(invalid_url) + '\n')

                print("+++++++++++++++++++++++++++++++++")
                print("total number: " + str(row_number - startRow))
                print("total passes: " + str(passes))
                print("total fail: " + str(fails))
                print("have amp versions: " + str(have_amp_versions))
                print("Invalid url: " + str(invalid_url))
                print("+++++++++++++++++++++++++++++++++")
        with open('result {}.txt'.format(startRow), "a", encoding="utf-8") as result:
            result.write('================================================\n')
            result.write("total number: " + str(row_number - startRow) + '\n')
            result.write("total fail: " + str(fails) + '\n')
            result.write("total fail: " + str(fails) + '\n')
            result.write("have amp versions: " + str(have_amp_versions) + '\n')
            result.write("Invalid url: " + str(invalid_url) + '\n')
        print("total number: " + str(row_number - startRow))
        print("total passes: " + str(passes))
        print("total fail: " + str(fails))
        print("have amp versions: " + str(have_amp_versions))
        print("Invalid url: " + str(invalid_url))
