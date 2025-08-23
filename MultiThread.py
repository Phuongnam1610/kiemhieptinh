from struct import pack
from main import *
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

    def __init__(self,u,udid,index,packtk,map=map):
        super().__init__(udid=udid,index=index,packtk=packtk,map=map)
        self.u=u
        

    def run(self):
        self.main()

def resetLD(devices):
    listtd=open("listtd.txt").readlines()
    listtk=open("listtk.txt").readlines()
    listmap=open("listmap.txt").readlines()
    tools.clear()
    for index,v in enumerate(devices):
        try:
            values=listtd[index].strip().split()
            coordinates = []
            tkmk=listtk[index].strip().split()
            for i in range(0, len(values), 2):
                x = int(values[i])
                y = int(values[i+1])
                coordinates.append([x, y])
            map=listmap[index].strip()

            
        except:
            coordinates=[[300,500]]
            tkmk=("A","B")
            map='tr'
            print(f"chua co toa do may {v}  ")
        a=MyThread(0,v,index=coordinates,packtk=tkmk,map=map)


        tools.append(a)
