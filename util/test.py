import os
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
urls = [
    "https://v.m.jd.com/landpage/orderShare.action?shareData=JaCDsAFFI%2BcQP%2FXcPrFQLZGmAo8jyoALOYuFp1oD6%2F4%3D&customerName=**%E4%BC%9F&sharePageType=2&utm_source=iosapp&utm_medium=appshare&utm_campaign=t_335139774&utm_term=CopyURL&ad_od=share", "https://v.m.jd.com/landpage/orderShare.action?shareData=JaCDsAFFI%2BcQP%2FXcPrFQLWSf94MWw29B%2BKzTjFeXXsU%3D&customerName=**%E4%BC%9F&sharePageType=2&utm_source=iosapp&utm_medium=appshare&utm_campaign=t_335139774&utm_term=CopyURL&ad_od=share", "https://v.m.jd.com/landpage/orderShare.action?shareData=awyhCR03%2Fq0xkJxw3MF0BgIu%2BAgkExXdNSk4GORB2So%3D&customerName=*%E5%A6%99&sharePageType=2&utm_source=iosapp&utm_medium=appshare&utm_campaign=t_335139774&utm_term=CopyURL&ad_od=share", "https://v.m.jd.com/landpage/orderShare.action?shareData=awyhCR03%2Fq0xkJxw3MF0BgIu%2BAgkExXdNSk4GORB2So%3D&customerName=*%E5%A6%99&sharePageType=2&utm_source=iosapp&utm_medium=appshare&utm_campaign=t_335139774&utm_term=CopyURL&ad_od=share", "https://v.m.jd.com/landpage/orderShare.action?shareData=awyhCR03%2Fq0xkJxw3MF0BgIu%2BAgkExXdNSk4GORB2So%3D&customerName=*%E5%A6%99&sharePageType=2&utm_source=iosapp&utm_medium=appshare&utm_campaign=t_335139774&utm_term=CopyURL&ad_od=share", "https://v.m.jd.com/landpage/orderShare.action?shareData=awyhCR03%2Fq0xkJxw3MF0BgIu%2BAgkExXdNSk4GORB2So%3D&customerName=*%E5%A6%99&sharePageType=2&utm_source=iosapp&utm_medium=appshare&utm_campaign=t_335139774&utm_term=CopyURL&ad_od=share", "https://v.m.jd.com/landpage/orderShare.action?shareData=awyhCR03%2Fq0xkJxw3MF0BgIu%2BAgkExXdNSk4GORB2So%3D&customerName=*%E5%A6%99&sharePageType=2&utm_source=iosapp&utm_medium=appshare&utm_campaign=t_335139774&utm_term=CopyURL&ad_od=share", "https://v.m.jd.com/landpage/orderShare.action?shareData=awyhCR03%2Fq0xkJxw3MF0BgIu%2BAgkExXdNSk4GORB2So%3D&customerName=*%E5%A6%99&sharePageType=2&utm_source=iosapp&utm_medium=appshare&utm_campaign=t_335139774&utm_term=CopyURL&ad_od=share", "https://v.m.jd.com/landpage/orderShare.action?shareData=awyhCR03%2Fq0xkJxw3MF0BgIu%2BAgkExXdNSk4GORB2So%3D&customerName=*%E5%A6%99&sharePageType=2&utm_source=iosapp&utm_medium=appshare&utm_campaign=t_335139774&utm_term=CopyURL&ad_od=share", "https://v.m.jd.com/landpage/orderShare.action?shareData=awyhCR03%2Fq0xkJxw3MF0BgIu%2BAgkExXdNSk4GORB2So%3D&customerName=*%E5%A6%99&sharePageType=2&utm_source=iosapp&utm_medium=appshare&utm_campaign=t_335139774&utm_term=CopyURL&ad_od=share", "https://v.m.jd.com/landpage/orderShare.action?shareData=JaCDsAFFI%2BcQP%2FXcPrFQLWSf94MWw29B%2BKzTjFeXXsU%3D&customerName=**%E4%BC%9F&sharePageType=2&utm_source=iosapp&utm_medium=appshare&utm_campaign=t_335139774&utm_term=CopyURL&ad_od=share", "https://v.m.jd.com/landpage/orderShare.action?shareData=awyhCR03%2Fq0xkJxw3MF0BgIu%2BAgkExXdNSk4GORB2So%3D&customerName=*%E5%A6%99&sharePageType=2&utm_source=iosapp&utm_medium=appshare&utm_campaign=t_335139774&utm_term=CopyURL&ad_od=share", "https://v.m.jd.com/landpage/orderShare.action?shareData=awyhCR03%2Fq0xkJxw3MF0BgIu%2BAgkExXdNSk4GORB2So%3D&customerName=*%E5%A6%99&sharePageType=2&utm_source=iosapp&utm_medium=appshare&utm_campaign=t_335139774&utm_term=CopyURL&ad_od=share", "https://v.m.jd.com/landpage/orderShare.action?shareData=awyhCR03%2Fq0xkJxw3MF0BgIu%2BAgkExXdNSk4GORB2So%3D&customerName=*%E5%A6%99&sharePageType=2&utm_source=iosapp&utm_medium=appshare&utm_campaign=t_335139774&utm_term=CopyURL&ad_od=share"
]
js = [
    "document.getElementsByClassName('info-card-item-value')[0].innerText",
    "document.getElementsByClassName('info-card-item-value')[1].innerText",
    "document.getElementsByClassName('info-card-item-value')[2].innerText",
    "document.getElementsByClassName('lg-timeline-current')[0].innerText"
]


def main():
    popen = os.popen('dir')
    text = popen.read()
    print(text)
    popen.close()


if __name__ == '__main__':
    main()
