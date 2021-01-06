#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :webBrowserUtil.py
# @Time      :2020/9/9 10:08
# @Author    :jimmy
# @Describe  :自动打开浏览器（多网页）

import webbrowser
import requests
import time
import os
import traceback
from urllib3.exceptions import ConnectTimeoutError
import logging

'''
    该方法用于刷浏览器的访问量(有自动关闭方法)
    threadName      ：线程名称
    circle_num      ：将要循环打开的微博地址
    url_list        ：循环的次数
'''
def url_open(threadName, circle_num, url_list):
    # print("微博链接List： %s" % (url_list[:]))
    # print("共计需要循环： %s 次" % (circle_num))
    print("————————————————————start ———————————————————— \n")

    # 我本地的360se浏览器位置
    local_Path_360 = 'C:/Users/tjm/AppData/Roaming/360se6/Application/360se.exe'
    # 注册浏览器对象
    webbrowser.register('local_Path_360', None, webbrowser.BackgroundBrowser(local_Path_360))
    # 增加超时连接重试次数
    requests.adapters.DEFAULT_RETRIES = 5

    # 1.定义要打开的网页url
    for num in range(circle_num):
        i = 1
        for recent_url in url_list:
            try:
                # 2.判断链接能否访问
                r = requests.get(recent_url, timeout=1)
                result = r.status_code
                if (result == 200):
                    # 3.打开浏览器
                    # webbrowser.open(recent_url)
                    # webbrowser.get('circlepath').open_new_tab('www.baidu.com')
                    webbrowser.get('local_Path_360').open(recent_url)
                    print("[%s] - Open Success [%s]：%s" % (threadName, i, recent_url))
            except ConnectTimeoutError as ex:
                print("[%s] - Open Failure[%s]：%s - 这里出现了连接超时异常 \n ex = %s" % (threadName, i, recent_url, ex))
                traceback.print_exc()
                time.sleep(2)
            except Exception as ex:
                print("[%s] - Open Failure[%s]：%s - 这里出现了未知异常 \n ex = %s" % (threadName, i, recent_url, ex))
                traceback.print_exc()
                time.sleep(2)
            else:
                i += 1
                time.sleep(1.2)
                print("页面成功打开，启动新一轮循环...")
        # 4.关闭浏览器
        print("——————————开始执行关闭操作——————————")
        time.sleep(5)
        os.system('taskkill /F /IM 360se.exe')          # 关闭360浏览器
        # os.system('taskkill /F /IM Iexplore.exe')     # 关闭IE浏览器
        # os.system('taskkill /F /IM chrome.exe')       # 关闭google浏览器
        print("—————————— 关闭操作完成 ——————————")
        print("——————————执行第【%s】次循环，结束——————————" % (num+1))
        time.sleep(1)

'''
    该方法用于刷浏览器的访问量(无自动关闭方法)
    threadName      ：线程名称
    circle_num      ：将要循环打开的微博地址
    url_list        ：循环的次数
'''
def url_open_noclose(threadName, circle_num, url_list):
    # print("微博链接List： %s" % (url_list[:]))
    # print("共计需要循环： %s 次" % (circle_num))
    print("————————————————————start ———————————————————— \n")

    # 我本地的360se浏览器位置
    local_Path_360 = 'C:/Users/tjm/AppData/Roaming/360se6/Application/360se.exe'
    # 注册浏览器对象
    webbrowser.register('local_Path_360', None, webbrowser.BackgroundBrowser(local_Path_360))
    # 增加超时连接重试次数
    requests.adapters.DEFAULT_RETRIES = 5

    # 1.定义要打开的网页url
    for num in range(circle_num):
        i = 1
        for recent_url in url_list:
            try:
                # 2.判断链接能否访问
                r = requests.get(recent_url, timeout=1)
                result = r.status_code
                if (result == 200):
                    # 3.打开浏览器
                    # webbrowser.open(recent_url)
                    # webbrowser.get('circlepath').open_new_tab('www.baidu.com')
                    webbrowser.get('local_Path_360').open(recent_url)
                    print("[%s] - Open Success [%s]：%s" % (threadName, i, recent_url))
            except ConnectTimeoutError as ex:
                print("[%s] - Open Failure[%s]：%s - 这里出现了连接超时异常 \n ex = %s" % (threadName, i, recent_url, ex))
                traceback.print_exc()
                time.sleep(2)
            except Exception as ex:
                print("[%s] - Open Failure[%s]：%s - 这里出现了未知异常 \n ex = %s" % (threadName, i, recent_url, ex))
                traceback.print_exc()
                time.sleep(2)
            else:
                i += 1
                time.sleep(1.5)
                print("页面成功打开，启动新一轮循环...")

def url_close(threadName):
    num = 1
    while 1:
        time.sleep(20)
        print("——————————开始执行关闭浏览器操作——————————")
        os.system('taskkill /F /IM 360se.exe')          # 关闭360浏览器
        # os.system('taskkill /F /IM Iexplore.exe')     # 关闭IE浏览器
        # os.system('taskkill /F /IM chrome.exe')       # 关闭google浏览器
        print("—————————— [%s] - 第【%s】次关闭操作完成 ——————————" % (threadName, num))
        num += 1

if __name__ == '__main__':
    url_list = ["https://jiming.blog.csdn.net/article/details/108469548",
               "https://jiming.blog.csdn.net/article/details/108406389",
               "https://blog.csdn.net/weixin_44259720/article/details/108398164",
               "https://blog.csdn.net/weixin_44259720/article/details/103292427"]
    circle_num = 200

    url_open(url_list, circle_num)
