# -*- coding: UTF-8 -*-
from time import sleep
import test
import getopt
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from concurrent.futures import ThreadPoolExecutor, as_completed
import json

thread_pool = ThreadPoolExecutor(max_workers=10)


def run_one(url, js, br=None, sleep_second=0, start_sleep=1):
    if br is None:
        browser = get_browser()
    else:
        browser = br
    browser.get(url)
    time.sleep(start_sleep)
    result = []
    for script in js:
        try:
            js_result = browser.execute_script(
                f"return {script}")
            result.append(js_result)
            if sleep_second != 0:
                time.sleep(sleep_second)
        except Exception as e:
            result.append(str(e))
    return result


def run_multiple(urls, js, sleep_second=0, start_sleep=2):
    # urls, js, sleep_second=0, start_sleep=1
    browser = get_browser()
    result = []
    for url in urls:
        re = run_one(url=url, js=js, br=browser,
                     sleep_second=sleep_second, start_sleep=start_sleep)
        result.append(re)
    return result


def get_browser():
    """
    获取浏览器对象
    :return:
    """
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_experimental_option(
        'excludeSwitches', ['enable-automation'])
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument("disable-cache")
    browser = webdriver.Chrome(chrome_options=chrome_options)
    return browser


def text_save(filename, data):  # filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename, 'w', encoding='utf-8')
    _result = ''
    for i in data:
        for j in i:
            _result += (str(j).replace('\n', '\t'))+('\t')
        _result += ('\n')
    file.write(_result)
    file.close()


if __name__ == '__main__':
    # # document.getElementsByClassName('info-card-item-value')[0].innerText
    # # document.getElementsByClassName('info-card-item-value')[1].innerText
    # # document.getElementsByClassName('info-card-item-value')[2].innerText
    # # document.getElementsByClassName('lg-timeline-current')[0].innerText

    # _result = run_multiple(
    #     urls=test.urls,
    #     js=test.js,
    #     start_sleep=2
    # )
    # print(_result)
    # getopt.getopt(sys.argv,)
    # all_task = run_multiple(urls=test.urls, js=test.js,
    #                         sleep_second=0, start_sleep=3)
    # print(all_task)
    op = open('c:/a.txt')
    line = op.readline()
    links = []
    while line:
        links.append(line)
        line = op.readline()
    links = [str(i).replace('\n', '') for i in links]
    op = open('c:/b.txt')
    line = op.readline()
    js = []
    while line:
        js.append(line)
        line = op.readline()
    js = [str(i).replace('\n', '') for i in js]
    _result = run_multiple(urls=links, js=js,
                           sleep_second=0, start_sleep=1)
    op.close()

    print(json.dumps(_result))
    text_save('c:/c.xls', _result)
