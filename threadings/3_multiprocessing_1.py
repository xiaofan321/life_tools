from multiprocessing import Process
import requests

# 子进程要执行的代码
def reqths(url):
    req = requests.get(url)
    print(req.status_code)

if __name__ == '__main__':
    ps = [Process(target=reqths, args=('http://www.baidu.com',)) for _ in range(1,10)] 
    for p in ps:
        p.start()
    for p in ps:
        p.join()

    print('end')
