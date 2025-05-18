from mainNMCamLogin import *
from PyQt5.QtCore import QThread
from file import *
tools=[]
threads=[]



def Ham():
        for i in tools:
            i.terminate()
        # for item in devicessl:
        for i in tools:
            i.start()

def stoptool():
        for i in tools:
            i.terminate()


class MyThread(QThread,toolLQ):
    # Tạo một tín hiệu để gửi thông báo từ thread con đến thread chính

    def __init__(self,udid,index,i):
        super().__init__(udid=udid,index=index,u=i)
        

    def run(self):
        self.main()

def resetLD(devices):
    listtd=open("listtd.txt").readlines()
    tools.clear()
    for k,v in enumerate(devices):
        try:
            values=listtd[i].strip().split()
            coordinates = []
            for i in range(0, len(values), 2):
                x = int(values[i])
                y = int(values[i+1])
                coordinates.append([x, y])
        except:
            coordinates=[[300,500]]
            print(f"chua co toa do may {v}  ")
        a=MyThread(v,coordinates,k)

        tools.append(a)
