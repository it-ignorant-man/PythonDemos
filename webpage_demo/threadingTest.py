#!/usr/bin/env python
# -*- coding:utf-8 -*-
# %FileName  :threadingTest.py
# %Time      :2020/9/9 9:24
# %Author    :jimmy

import threading
import time
from webpage_demo import webBrowserUtil

'''
    该方法用于启动多个线程，调用刷微博程序
'''
class threadForOpen (threading.Thread):
    def __init__(self, threadID, name, counter, urlList):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.list = urlList
    def run(self):
        print("开始线程：" + self.name)
        url_open(self.name, self.counter, self.list)
        print("退出线程：" + self.name)

class threadForClose (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        print("开始线程：" + self.name)
        url_close(self.name)
        print("退出线程：" + self.name)

def url_open(threadName, counter, urlList):
    webBrowserUtil.url_open_noclose(threadName, counter, urlList)
    print("%s: %s" % (threadName, time.ctime(time.time())))

def url_close(threadName):
    webBrowserUtil.url_close(threadName)
    print("%s: %s" % (threadName, time.ctime(time.time())))

def main():
    # 创建新线程
    thread_new = threadForOpen(1, "Thread-new", 2000, url_list0)
    thread_page1 = threadForOpen(2, "Thread-page1", 2000, url_list1)
    thread_page2 = threadForOpen(3, "Thread-page2", 2000, url_list2)
    thread_hot = threadForOpen(4, "Thread-hot", 2000, url_list9)
    thread_new2 = threadForOpen(4, "Thread-new2", 2000, url_list02)

    thread_close = threadForClose(5, "Thread-close")

    # 开启新线程
    thread_new.start()
    thread_new2.start()
    thread_page1.start()
    thread_page2.start()
    thread_hot.start()
    thread_close.start()

    thread_new.join()
    thread_new2.join()
    thread_page1.join()
    thread_page2.join()
    thread_hot.join()
    print("------------------------------- 退出主线程")

# 重点刷新的微博
url_list0 = ["https://jiming.blog.csdn.net/article/details/110437544",
             "https://jiming.blog.csdn.net/article/details/110229694",
            "https://jiming.blog.csdn.net/article/details/104628663",
            "https://jiming.blog.csdn.net/article/details/110181822",
            "https://jiming.blog.csdn.net/article/details/110138972",
            "https://jiming.blog.csdn.net/article/details/110120677",
            "https://jiming.blog.csdn.net/article/details/110092870",
            "https://jiming.blog.csdn.net/article/details/109784917",
            "https://jiming.blog.csdn.net/article/details/109216423",
            "https://jiming.blog.csdn.net/article/details/108535608",
            "https://jiming.blog.csdn.net/article/details/108469548",
            "https://jiming.blog.csdn.net/article/details/108406389",
            "https://jiming.blog.csdn.net/article/details/108398164",
            "https://jiming.blog.csdn.net/article/details/107025598",
             "https://jiming.blog.csdn.net/article/details/111488947",
             "https://jiming.blog.csdn.net/article/details/111470585",
             "https://jiming.blog.csdn.net/article/details/111183470",
             "https://jiming.blog.csdn.net/article/details/111182740",
             "https://jiming.blog.csdn.net/article/details/111040063",
             "https://jiming.blog.csdn.net/article/details/110952842",
             "https://jiming.blog.csdn.net/article/details/111193298",
             "https://jiming.blog.csdn.net/article/details/104713763",
             "https://jiming.blog.csdn.net/article/details/111935494",
             "https://jiming.blog.csdn.net/article/details/110947742",
             "https://jiming.blog.csdn.net/article/details/111592387",
             "https://jiming.blog.csdn.net/article/details/111488947"]

# 重点刷新的微博2
url_list02 = ["https://jiming.blog.csdn.net/article/details/111193298",
             "https://jiming.blog.csdn.net/article/details/104713763",
             "https://jiming.blog.csdn.net/article/details/111935494",
             "https://jiming.blog.csdn.net/article/details/110947742",
             "https://jiming.blog.csdn.net/article/details/111592387",
             "https://jiming.blog.csdn.net/article/details/111488947",
             "https://jiming.blog.csdn.net/article/details/88175440"]



# 微博第一页
url_list1 = ["https://jiming.blog.csdn.net/article/details/103292427",
             "https://jiming.blog.csdn.net/article/details/88175440",
             "https://jiming.blog.csdn.net/article/details/108469548",
             "https://jiming.blog.csdn.net/article/details/108406389",
             "https://jiming.blog.csdn.net/article/details/108398164",
             "https://jiming.blog.csdn.net/article/details/107025598",
             "https://jiming.blog.csdn.net/article/details/105949946",
             "https://jiming.blog.csdn.net/article/details/105594350",
             "https://jiming.blog.csdn.net/article/details/105934467",
             "https://jiming.blog.csdn.net/article/details/105933636",
             "https://jiming.blog.csdn.net/article/details/105916975",
             "https://jiming.blog.csdn.net/article/details/105563650",
             "https://jiming.blog.csdn.net/article/details/105535214",
             "https://jiming.blog.csdn.net/article/details/105483105",
             "https://jiming.blog.csdn.net/article/details/105482044",
             "https://jiming.blog.csdn.net/article/details/105416113",
             "https://jiming.blog.csdn.net/article/details/105381045",
             "https://jiming.blog.csdn.net/article/details/105358934",
             "https://jiming.blog.csdn.net/article/details/105294743",
             "https://jiming.blog.csdn.net/article/details/110437544",
             "https://jiming.blog.csdn.net/article/details/105291788",
             "https://jiming.blog.csdn.net/article/details/105289343",
             "https://jiming.blog.csdn.net/article/details/104969236",
             "https://jiming.blog.csdn.net/article/details/104942598",
             "https://jiming.blog.csdn.net/article/details/104541167",
             "https://jiming.blog.csdn.net/article/details/104615086",
             "https://jiming.blog.csdn.net/article/details/104637508",
             "https://jiming.blog.csdn.net/article/details/104900530",
             "https://jiming.blog.csdn.net/article/details/104897398",
             "https://jiming.blog.csdn.net/article/details/104845731",
             "https://jiming.blog.csdn.net/article/details/104844231",
             "https://jiming.blog.csdn.net/article/details/104839501",
             "https://jiming.blog.csdn.net/article/details/104839050",
             "https://jiming.blog.csdn.net/article/details/104813309",
             "https://jiming.blog.csdn.net/article/details/104778603",
             "https://jiming.blog.csdn.net/article/details/104777782",
             "https://jiming.blog.csdn.net/article/details/104772396",
             "https://jiming.blog.csdn.net/article/details/104772543",
             "https://jiming.blog.csdn.net/article/details/104768288",
             "https://jiming.blog.csdn.net/article/details/104714555"]

# 微博第二页
url_list2 = ["https://jiming.blog.csdn.net/article/details/104713763",
             "https://jiming.blog.csdn.net/article/details/104696403",
             "https://jiming.blog.csdn.net/article/details/104695830",
             "https://jiming.blog.csdn.net/article/details/104694900",
             "https://jiming.blog.csdn.net/article/details/104694446",
             "https://jiming.blog.csdn.net/article/details/104693946",
             "https://jiming.blog.csdn.net/article/details/104690055",
             "https://jiming.blog.csdn.net/article/details/104675384",
             "https://jiming.blog.csdn.net/article/details/104674433",
             "https://jiming.blog.csdn.net/article/details/104648444",
             "https://jiming.blog.csdn.net/article/details/104556235",
             "https://jiming.blog.csdn.net/article/details/104547940",
             "https://jiming.blog.csdn.net/article/details/104535730",
             "https://jiming.blog.csdn.net/article/details/104535038",
             "https://jiming.blog.csdn.net/article/details/104532446",
             "https://jiming.blog.csdn.net/article/details/104531575",
             "https://jiming.blog.csdn.net/article/details/104530250",
             "https://jiming.blog.csdn.net/article/details/104529950",
             "https://jiming.blog.csdn.net/article/details/104521766",
             "https://jiming.blog.csdn.net/article/details/104520605",
             "https://jiming.blog.csdn.net/article/details/104511223",
             "https://jiming.blog.csdn.net/article/details/104500710",
             "https://jiming.blog.csdn.net/article/details/104500781",
             "https://jiming.blog.csdn.net/article/details/104494118",
             "https://jiming.blog.csdn.net/article/details/104492041",
             "https://jiming.blog.csdn.net/article/details/103989515",
             "https://jiming.blog.csdn.net/article/details/103972908",
             "https://jiming.blog.csdn.net/article/details/103924497",
             "https://jiming.blog.csdn.net/article/details/103912667",
             "https://jiming.blog.csdn.net/article/details/103922082",
             "https://jiming.blog.csdn.net/article/details/103911466",
             "https://jiming.blog.csdn.net/article/details/103906392",
             "https://jiming.blog.csdn.net/article/details/103890989",
             "https://jiming.blog.csdn.net/article/details/103736924",
             "https://jiming.blog.csdn.net/article/details/103698499",
             "https://jiming.blog.csdn.net/article/details/103697996",
             "https://jiming.blog.csdn.net/article/details/103686997",
             "https://jiming.blog.csdn.net/article/details/103680440",
             "https://jiming.blog.csdn.net/article/details/103496184"]

# 微博热度高的博文
url_list9 = ["https://jiming.blog.csdn.net/article/details/87002816",
             "https://jiming.blog.csdn.net/article/details/95500790",
             "https://jiming.blog.csdn.net/article/details/109784917",
             "https://jiming.blog.csdn.net/article/details/95495983",
             "https://jiming.blog.csdn.net/article/details/94617582",
             "https://jiming.blog.csdn.net/article/details/94602764",
             "https://jiming.blog.csdn.net/article/details/88656701",
             "https://jiming.blog.csdn.net/article/details/88179885",
             "https://jiming.blog.csdn.net/article/details/88414828",
             "https://jiming.blog.csdn.net/article/details/87987474",
             "https://jiming.blog.csdn.net/article/details/102895609",
             "https://jiming.blog.csdn.net/article/details/100583977",
             "https://jiming.blog.csdn.net/article/details/103906392",
             "https://jiming.blog.csdn.net/article/details/103697996",
             "https://jiming.blog.csdn.net/article/details/103185972",
             "https://jiming.blog.csdn.net/article/details/103924497",
             "https://jiming.blog.csdn.net/article/details/104541167",
             "https://jiming.blog.csdn.net/article/details/105294743",
             "https://jiming.blog.csdn.net/article/details/105594350",
             "https://jiming.blog.csdn.net/article/details/88070518",
             "https://jiming.blog.csdn.net/article/details/104897398",
             "https://jiming.blog.csdn.net/article/details/109784917"]



if __name__ == "__main__":
    main()
