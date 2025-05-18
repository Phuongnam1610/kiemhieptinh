def getfile(dvs,filename='listtk.txt'):
    
    listtk = open(filename).readlines()
    songuyen = len(listtk) // dvs
    sodu = len(listtk) % dvs
    listtkdachia=[]

    for i in range((dvs)):
        start=i*songuyen
        if(i==(dvs-1)):
            listtkdachia.append(listtk[start:start+songuyen+sodu])
        else:
            listtkdachia.append(listtk[start:start+songuyen])
        
    return (listtkdachia)