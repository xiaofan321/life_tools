#coding=utf-8
import hashlib
import os


class Quchong():
    def __init__(self,path):
        self.path = path
        self.cachenum = 10000
        self.cachedata = {}
        self.rulelen = 1
        self.sqlpath = 'sqldata/'
        self.connf = {}
        self.resutpath = 'testres.txt'

    # 规则写进文件
    def torule(self):
        for md5val in self.cachedata:
            path = '%s/%s.txt'%(self.sqlpath,md5val[0:self.rulelen])
            fw = self.fileconn(path)
            fw.write(md5val+'\n')
            fres = self.fileconn(self.resutpath)
            fres.write(self.cachedata[md5val]+'\n')

    # 管理文件打开
    def fileconn(self,path):
        if path in self.connf:
            return self.connf[path]
        else:
            f = open(path,'w+',encoding='utf-8',errors="ignore")
            self.connf[path] = f
            return self.connf[path]

    # 查询md5是否重复
    def selectrule(self):
        for md5val in list(self.cachedata.keys()):
            path = '%s/%s.txt'%(self.sqlpath,md5val[0:self.rulelen])
            fr = self.fileconn(path)
            con = fr.read()
            if con.find(md5val) != -1:
                self.cachedata.pop(md5val)

    def getmd5(self,data):
        return hashlib.md5(data.encode("utf-8")).hexdigest()[8:-8]

    def main(self):
        
        if not os.path.exists(self.sqlpath):
            os.mkdir(self.sqlpath) 

        for root,dirs,files in os.walk(self.path):
            for file in files:
                filename = "%s\\%s"%(root,file)
                print('qc==>'+filename)

                with open(filename,encoding='utf-8') as fr:
                    flag = 1
                    for line in fr:
                        data = line.strip()
                        md5data = self.getmd5(data)
                        self.cachedata[md5data] = data
                        if flag >= self.cachenum:
                            # 
                            self.selectrule()
                            # 
                            self.torule()
                            self.cachedata.clear()
                            flag = 0
                        else:
                            flag += 1
                            self.cachedata[md5data] = data
        # 
        self.selectrule()
        # 
        self.torule()
        self.cachedata.clear()

    def __del__(self):
        for path in self.connf:
            print(str(self.connf[path])+'closed')
            self.connf[path].close()


if __name__ == '__main__':
    test = Quchong('D:\\test')
    test.main()
