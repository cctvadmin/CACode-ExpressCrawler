# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def run_one(url, js, br=None, sleep_second=0, start_sleep=1):
    if br is None:
        browser = get_browser()
    else:
        browser = br
    browser.get(url)
    time.sleep(start_sleep)
    result = []
    for script in js:
        js_result = browser.execute_script(
            f"return {script}")
        result.append(js_result)
        if sleep_second != 0:
            time.sleep(sleep_second)
    return result


def run_multiple(urls, js, sleep_second=0, start_sleep=1):
    browser = get_browser()
    result = []
    for url in urls:
        re = run_one(url=url, js=js, br=browser, sleep_second=sleep_second, start_sleep=start_sleep)
        result.append(re)
    return result


def get_browser():
    """
    获取浏览器对象
    :return:
    """
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options=chrome_options)
    return browser


if __name__ == '__main__':
    # document.getElementsByClassName('info-card-item-value')[0].innerText 快递单号
    # document.getElementsByClassName('info-card-item-value')[1].innerText 快递公司
    # document.getElementsByClassName('info-card-item-value')[2].innerText 预计送达时间
    # document.getElementsByClassName('lg-timeline-current')[0].innerText 第一条物流信息，包含送达状态、物流信息、物流更新日期
    _result = run_multiple(
        urls=[
            "https://v.m.jd.com/landpage/orderShare.action?shareData=JaCDsAFFI%2BcQP%2FXcPrFQLZGmAo8jyoALOYuFp1oD6%2F4%3D&customerName=**%E4%BC%9F&sharePageType=2&utm_source=iosapp&utm_medium=appshare&utm_campaign=t_335139774&utm_term=CopyURL&ad_od=share",
            "https://v.m.jd.com/landpage/orderShare.action?shareData=JaCDsAFFI%2BcQP%2FXcPrFQLWSf94MWw29B%2BKzTjFeXXsU%3D&customerName=**%E4%BC%9F&sharePageType=2&utm_source=iosapp&utm_medium=appshare&utm_campaign=t_335139774&utm_term=CopyURL&ad_od=share"],
        js=[
            "document.getElementsByClassName('info-card-item-value')[0].innerText",
            "document.getElementsByClassName('info-card-item-value')[1].innerText",
            "document.getElementsByClassName('info-card-item-value')[2].innerText",
            "document.getElementsByClassName('lg-timeline-current')[0].innerText"
        ],
        start_sleep=2
    )
    print(_result)
