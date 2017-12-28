import threading
import requests

def loop(url):
    req = requests.get(url)
    print("%s=>%s"%(req.status_code,req.url))

def mainreq(urls):
    threads = [threading.Thread(target=loop,args=(url,)) for url in urls]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    urls = ['http://www.baidu.com' for _ in range(1,30)]
    # print(urls)
    mainreq(urls)
