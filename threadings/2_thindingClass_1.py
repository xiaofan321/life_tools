import threading
import requests
import time

class myThread (threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        time.sleep(1)
        req = requests.get(self.url)
        print(req.status_code,self.url)

# 创建新线程
threads = [myThread('http://www.baidu.com') for _ in range(1,10)] 

# 开启新线程
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print ("退出主线程")
