# coding=utf-8
# author：xiaofan
import os,chardet

def main(path,con):
    for root,dirs,files in os.walk(path):
        for file in files:
            filename = "%s\%s"%(root,file)
            try:
                with open(filename,"rb") as f:
                    data = f.read()
                    coding = chardet.detect(data[:100 if (len(data))>100 else len(data)])['encoding']
                    # print(coding)
                    data = data.decode(encoding=coding if coding else 'utf-8')

                    if data.find(con) != -1:
                        print(filename)
            except UnicodeDecodeError as e:
                # print('解码异常'+filename)
                pass
            except Exception as e:
                # print(e+filename)
                pass
    print("find finsh")

if __name__ == "__main__":
    path = r"E:\\test"
    con = "你好"
    main(path,con)