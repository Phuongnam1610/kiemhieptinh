from adb import *
import numpy as np
pkgame="com.tepaylink.kiemhieptinh2mobile"
pkgame2="com.tepaylink.kiemhieptinh2mobile/org.cocos2dx.cpp.AppActivity"


def cam(img):
    """
    Kiểm tra màu cam trong ảnh với phương pháp cải tiến
    
    Args:
        img: Ảnh numpy array định dạng BGR
        
    Returns:
        bool: True nếu tìm thấy màu cam, False nếu không
    """
    # Chuyển đổi ảnh sang không gian màu HSV để kiểm tra màu sắc tốt hơn
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Định nghĩa ngưỡng màu cam trong HSV
    # Hue: 0-20 (màu cam)
    # Saturation: 100-255 (độ bão hòa cao)
    # Value: 100-255 (độ sáng cao)
    lower_orange = np.array([0, 100, 100])
    upper_orange = np.array([20, 255, 255])
    
    # Tạo mặt nạ cho màu cam
    mask = cv2.inRange(hsv, lower_orange, upper_orange)
    
    # Kiểm tra xem có pixel màu cam không
    return np.any(mask)
    # Tải ảnh    
    # Kiểm tra từng điểm ảnh
    found = False
    for x in range(img.shape[1]):
        for y in range(img.shape[0]):
            b, g, r = img[y, x]
            d = abs(r - 195) + abs(g - 102) + abs(b - 38)
            if d <= 10:
                found = True
                break
            
    return found
class toolLQ():
    def __init__(self,udid,index):
        self.udid=udid    
        self.index=index
    def test(self):
        while True:
            if(findFor(self.udid, 1,"fulldo.png",threshold=0.85,yclick=0))!=0:
                if(findFor(self.udid, 1, "vethanh.png", 1)!= 0):
                    time.sleep(5)
                    self.dungdi()
                if(self.vDL()==True):
                        time.sleep(1)
                        click(self.udid,814,212,"Thoai")
                        time.sleep(5)
                        if (findFor(self.udid, 1, "hanhtrang.png", 0)!= 0):
                            if(self.bando()==True):
                                # if(self.buffmau()==True):
                                    if(self.lenbai()==True):
                                            self.batauto()
                                    else:
                                        break
                            else:
                                break
                        else:
                            break
                else:
                    break

    def loadgame(self):
        closeGame(self.udid,pkgame)
        time.sleep(5)
        moGame(self.udid,pkgame2)
        time.sleep(random.randint(20,60))  # Random sleep between 10-30 seconds
    
    def dungdi(self):
        time.sleep(5)
        for i in range(100):
            # click(self.udid, 856,110 ,"map")
            # if (findFor(self.udid, 5, "dichuyen.png", 0)!= 0):
                # for i in range(50):
                    sc=screen_capture(self.udid)
                    if(find2(sc,"loadgame.png",threshold=0.94)!=0):
                        time.sleep(5)
                        print('dang load')
                        continue
                    sc1=sc[41:52,829:880]
                    time.sleep(5)
                    sc2=screen_capture(self.udid)[18:65,802:896]
                    
                    if(find3(sc2,sc1,threshold=0.99)!=0):
                        print('da ket thuc di chuyen')
                        time.sleep(5)
                        return True
            # else:
                # findFor(self.udid, 1, "nutx.png", 1,threshold=0.85)    

        return False
                    
                    
                
    
    def phu(self):

        for i in range(2):
            if(findFor(self.udid, 1, "phu.png", 1)!= 0):
                time.sleep(10)
                click(self.udid, 856,110 ,"map")
                time.sleep(5)
                if (findFor(self.udid, 1, "dailyphu.png", 0,threshold=0.8)!= 0):
                    return True
                click(self.udid,888,29,"nutx")
            else:
                click(self.udid,916 ,384 )
                time.sleep(5)
        return False
    
    def chuduocdiem(self):
        
        for i in range(2):
            click(self.udid, 856,110 ,"map")
            time.sleep(5)
            if (findFor(self.udid, 1, "dichuyen.png", 0)!= 0):
                click(self.udid, 575, 310,"chuduocdiem")
                self.dungdi()
                for i in range(3):
                    click(self.udid,814,212,"Thoai")
                    time.sleep(5)
                    if (findFor(self.udid, 1, "hanhtrang.png", 0)!= 0):
                        return self.bando()
                    
                return False
            else:
                findFor(self.udid, 1, "nutx.png", 1,threshold=0.85)    
    
    def vDL(self):
        if(self.tatauto()==True):
            for i in range(2):
                click(self.udid, 856,110 ,"map")
                time.sleep(5)
                
                if (findFor(self.udid, 1, "dichuyen.png", 0)!= 0):
                    click(self.udid,687,19,"the gioi")
                    time.sleep(5)
                    click(self.udid, 238, 401,"dai ly ")
                    time.sleep(5)
                    click(self.udid, 575, 310,"chuduocdiem")
                    self.dungdi()
                    return True
        
        return False
        
                    
    
    def update_value(self,o,y=1):
        vthang = (o - 1) // 5 + 1
        vtcot = (o - 1) % 5 + 1
        x=int(vtcot*54.8-(54.8/2))
        y=int(vthang*52.75-(52.75/2))
        return (x+496,y+153)
    def update_value2(self,o,y=1):
        vthang = (o - 1) // 5 + 1
        vtcot = (o - 1) % 5 + 1
        x=int(vtcot*54.8-(54.8/2))
        y=int(vthang*52.75-(52.75/2))
        return (x+494,y+43)
    
    
   

    def locdo(self,listcanxoa):
        # listcanxoa=[16,11,6,1,2,7,12,17,18,13,8,3,4,9,14,19,20,15,10,5]        
        # listcanxoa=[26,21,16,11,6,1,2,7,12,17,22,27,28,23,18,13,8,3,4,9,14,19,24,29,30,25,20,15,10,5]        
        sc=screen_capture(self.udid)
        listnull=find2(sc[43:368,494:760],"otrong.png",threshold=0.75)
        listsdo=find2(sc[43:368,494:760],"sachdo.png",threshold=0.65)
        if(listnull!=0):            
            for i in listnull:
                vtcot=(i[0]+(54.8/2))/54.8
                vtcot=round(vtcot)
                vthang=(i[1]+(52.75/2))/52.75
                vthang=round(vthang)
                o=(vthang - 1) * 5 + vtcot
                if(o in listcanxoa):
                    listcanxoa.remove(o)
        if(listsdo!=0):
            for i in listsdo:
                vtcot=(i[0]+(54.8/2))/54.8
                vtcot=round(vtcot)
                vthang=(i[1]+(52.75/2))/52.75
                vthang=round(vthang)
                o=(vthang - 1) * 5 + vtcot
                if(o in listcanxoa):
                    listcanxoa.remove(o)
        updated_arr = list(map(self.update_value2, listcanxoa))
        return (updated_arr)

            
    def findC(self,image,count=5,c=1):
        if(findFor(self.udid,img=image,n=count,yclick=c)!=0):
            return True
        else:
            return False
    def giamdinh(self):
        for i in range(2):
            click(self.udid,121,90,"giam dinh")
            time.sleep(5)
            if (findFor(self.udid, 1, "giamdinh.png",0 ,threshold=0.8)!= 0):
                
                for i in range(2):
                    click(self.udid,787,126,"o so 1")
                    time.sleep(3)
                time.sleep(1)
                listcanxoa1=[26,21,16,11,6,1,2,7,12,17,22,27,28,23,18,13,8,3,4,9,14,19,24,29,30,25,20,15,10,5]        
                listcx1=self.locdo(listcanxoa1)
                lrm1=[]
                for i in (listcx1):
                    click(self.udid, i[0],i[1] )
                    time.sleep(1)
                    click(self.udid, i[0],i[1] )
                    time.sleep(1)
                    a=False
                    sc=screen_capture(self.udid)
                    if(find2(sc,"yeucau.png", 0,threshold=th)!= 0):
                        a=True
                    elif(find2(sc,"xacxuat.png", 0,threshold=th)!= 0):
                        a=True
                    elif(find2(sc,"yeucau2.png", 0,threshold=th)!= 0):
                        a=True
                    elif(find2(sc,"xacxuat2.png", 0,threshold=th)!= 0):
                        a=True
                    if(a==True):
                       lrm1.append(i)
                for i in lrm1:
                    if(i in listcx1 ):
                        listcx1.remove(i)
                #sang ô 2
                for i in range(2):
                    click(self.udid,786,268,"o so 2")
                time.sleep(3)
                listcanxoa2=[16,11,6,1,2,7,12,17,18,13,8,3,4,9,14,19,20,15,10,5]      
                listcx2=self.locdo(listcanxoa2)
                lrm1=[]
                for i in (listcx2):
                    click(self.udid, i[0],i[1] )
                    time.sleep(1)
                    click(self.udid, i[0],i[1] )
                    time.sleep(1)
                    a=False
                    sc=screen_capture(self.udid)
                    
                    if(find2(sc,"yeucau.png", 0,threshold=th)!= 0):
                        a=True
                    elif(find2(sc,"xacxuat.png", 0,threshold=th)!= 0):
                        a=True
                    elif(find2(sc,"yeucau2.png", 0,threshold=th)!= 0):
                        a=True
                    elif(find2(sc,"xacxuat2.png", 0,threshold=th)!= 0):
                        a=True
                    if(a==True):
                       lrm1.append(i)
                for i in lrm1:
                    if(i in listcx2 ):
                        listcx2.remove(i)
                return (listcx1,listcx2)
        return False
    def suachua(self):
        for i in range(2):
            click(self.udid,121,189,"sua chua")
            time.sleep(5)
            click(self.udid, 30, 37,"avatar")
            time.sleep(5)
            click(self.udid, 175,94,"o so 1" )
            time.sleep(1)
            findFor(self.udid, 1, "dongy3.png",1,threshold=0.8 )
            click(self.udid, 185,200,"o so 2" )
            time.sleep(1)
            findFor(self.udid, 1, "dongy3.png",1,threshold=0.8 )
            click(self.udid, 183,387,"o so 3" )
            time.sleep(1)
            findFor(self.udid, 1, "dongy3.png",1,threshold=0.8 )
            time.sleep(1)
            click(self.udid,476 ,32 ,"x")
            return True
        return False
    def bando(self):
        listcx=self.giamdinh()
        if(listcx==False):
            return False
        if(self.suachua()==False):
            return False
        for i in range(2):
            click(self.udid, 116,357,"ban nhanh" )
            time.sleep(5)
            if (findFor(self.udid, 2, "bannhanh.png", 0)!= 0):
                for i in range(2):
                    click(self.udid,787,126,"o so 1")
                time.sleep(5)
                for i in (listcx[0]):
                    click(self.udid, i[0],i[1] )
                    click(self.udid, i[0],i[1] )
                for i in range(2):
                    click(self.udid,786,268,"o so 2")
                time.sleep(5)
                for i in (listcx[1]):
                    click(self.udid, i[0],i[1] )
                    click(self.udid, i[0],i[1] )

                click(self.udid, 917, 27,"nutx")
                return True
        return False
            
    def lenbai(self):
        for i in range(2):
            click(self.udid, 856,110 ,"map")
            time.sleep(5)
            if (findFor(self.udid, 1, "dichuyen.png", 0)!= 0):
                time.sleep(3)
                click(self.udid,687,19,"the gioi")
                time.sleep(10)
                for i in self.index:
                    clickTC=True
                    for a in range(10):
                        sc=screen_capture(self.udid)
                        sc1=sc[179:201,347:376]
                        if(clickTC==True):
                            click(self.udid,i[0],i[1])
                        else:
                            click(self.udid,int(i[0])+random.randint(-5,5),int(i[1])+random.randint(-5,5))
                        time.sleep(10)
                        sc2=screen_capture(self.udid)[157:204,318:393]
                        
                        if(find3(sc2,sc1,threshold=0.8)!=0):
                            clickTC=False
                        else:
                            clickTC=True
                            break
                self.dungdi()
                time.sleep(3)
                click(self.udid,888,29,"nutx")  
                return True
                
            time.sleep(3)
            click(self.udid,888,29,"nutx")  
        return False
    def skill(self):
        for i in range(3):
            if (findFor(self.udid, 1, "skill.png", 1)!= 0):
                time.sleep(3)
                swipe(self.udid, 700, 326, 582, 294, 3000)
                return
            click(self.udid,917,375,"mo rong")
            time.sleep(5)
            
    def vaoTD(self):
        for i in range(2):
            click(self.udid, 856,110 ,"map")
            time.sleep(5)
            if (findFor(self.udid, 1, "dichuyen.png", 0)!= 0):
                click(self.udid, self.index[0],self.index[1],"toado")
                click(self.udid,888,28,"nutx")
                # time.sleep(5)
                self.dungdi()
                return True
            
        return False

    def batauto(self):
        click(self.udid,918, 263,"ngua")
        time.sleep(3)
        click(self.udid, 916, 216,"buff")
        time.sleep(3)
        for i in range(3):
            click(self.udid, 864, 209,"auto")
            time.sleep(3)
            sc=screen_capture(self.udid)
            sc=sc[191:216,840:880]
            if (cam(sc)==True):
                swipe(self.udid,83,446,142,330,500)
                time.sleep(3)
                swipe(self.udid,83,446,83,330,500)
                return True
            swipe(self.udid,83,446,142,330,500)
            time.sleep(3)
            swipe(self.udid,83,446,83,330,500)
        return False
        
    def tatauto(self):
        for i in range(4):
            click(self.udid, 864, 209,"auto")
            time.sleep(5)
            sc=screen_capture(self.udid)
            
            sc=sc[191:216,840:880]
            if (cam(sc)==False):
                swipe(self.udid,83,446,142,330,500)
                time.sleep(1)
                swipe(self.udid,83,446,83,330,500)
                return True
            swipe(self.udid,83,446,142,330,500)
            time.sleep(1)
            swipe(self.udid,83,446,83,330,500)
        return False
        
        
    def checkMap(self):
        for i in range(2):
            click(self.udid, 856,110 ,"map")
            time.sleep(5)
            if (findFor(self.udid, 5, "dichuyen.png", 0)!= 0):
                time.sleep(5)
                for i in range(1):
                    if (findFor(self.udid, 5, "pmd2.png", 0,threshold=0.85)!= 0):
                        click(self.udid,888,29,"nutx")
                        return 1
                    # if (findFor(self.udid, 5, "dailyphu.png", 0,threshold=0.85)!= 0):
                    #     click(self.udid,888,29,"nutx")
                    #     return 0  
            click(self.udid,888,29,"nutx")
                          
        return 2
    def checkTB(self):
        for i in range(2):
                click(self.udid,787,126,"o so 1")
        time.sleep(5)
        for i in range(6):
            click(self.udid,754-i*45,50,f"tb {i}")
            time.sleep(1)
            if(findFor(self.udid, 3,"200.png",threshold=0.8,yclick=0))!=0:
                print(f'thay tb so {i} hong')
                if(findFor(self.udid, 5,"sudung.png",threshold=0.8,yclick=1))!=0:
                    click(self.udid,909,23,"nutx")
                    time.sleep(1)
                    return True
        click(self.udid,909,23,"nutx")
        time.sleep(1)
        return False
    
    def ngamy(self):
        ftb=False
        for i in range(2):
            self.tatauto()
            click(self.udid, 856,110 ,"map")
            time.sleep(5)
            if (findFor(self.udid, 5, "dichuyen.png", 0)!= 0):
                click(self.udid,687,19,"the gioi")
                time.sleep(5)
                click(self.udid, 220, 318,"ngamy")
                time.sleep(5)
                click(self.udid,445,162)
                self.dungdi()
                time.sleep(2)
                click(self.udid,814,212,"Thoai")
                time.sleep(5)
                if (findFor(self.udid, 5, "vatdung.png", 1,threshold=0.85)!= 0):
                    time.sleep(5)
                    if (findFor(self.udid, 5, "hanhtrang.png", 0)!= 0):
                        time.sleep(5)
                        click(self.udid, 116,357,"ban nhanh" )
                        time.sleep(5)
                        if (findFor(self.udid, 5, "bannhanh.png", 0)!= 0):
                            for i in range(6):
                                click(self.udid,754-i*45,50,f"tb {i}")
                                click(self.udid,754-i*45,50,f"tb {i}")
                                time.sleep(5)
                            ftb=True
                            break
        if(ftb==True):
            ftb=False
            for i in range(2):
                click(self.udid,890,18,"nutx")
                time.sleep(5)
                click(self.udid,814,212,"Thoai")
                time.sleep(5)  
                if (findFor(self.udid, 5, "tanthu.png", 1,threshold=0.85)!= 0):
                    time.sleep(5)
                    for i in range(2):
                        if (findFor(self.udid, 5, "kiem.png", 0)!= 0):
                            ftb=True
                            break
                        click(self.udid,209,498)
                    if(ftb==False):
                        continue
                    else:
                        ftb=False
                        kiem=findFor(self.udid,5,"kiem.png",0,threshold=0.8)
                        if(kiem!=0):
                            xquydoi=kiem[0][0]
                            yquydoi=kiem[0][1]
                        for i in range(6):
                            click(self.udid,xquydoi+500,yquydoi,"quy doi")
                            time.sleep(5)
                            if (findFor(self.udid, 5, "dongy2.png", 1)!= 0):
                                ftb=True
                            else:
                                ftb=False
                                break
                        if(ftb==False):
                            continue
                        else:
                            click(self.udid,821,40,"nutx")
                            time.sleep(5)
                            click(self.udid,601,495,"hanhtrang")
                            time.sleep(5)
                            if(findFor(self.udid, 5,"hanhtrang.png",threshold=0.85,yclick=0))!=0:
                                if(self.checkTB()==True):
                                    return True
                                    # if(self.lenbai()==True):
                                    #     if(self.vaoTD()==True):
                                    #         return self.batauto()
                                else:
                                    return False
        else:
            return False                                   
                                            


                                   
                    
                    
           

    def doitb(self):
        for i in range(2):
            if(self.tatauto()==True):
                click(self.udid,601,495,"hanhtrang")
                time.sleep(5)
                if(findFor(self.udid, 5,"hanhtrang.png",threshold=0.85,yclick=0))!=0:
                    if(self.checkTB()==True):
                        return True
                    else:
                        return self.ngamy()

    def checkhong(self):  
        for i in range(5):
            click(self.udid,913 ,367,"4")
            time.sleep(1)
            if(findFor(self.udid, 5, "buffmau.png", 1,threshold=0.8)!= 0):
                for i in range(5):
                    click(self.udid,879,324,"buff mau")
                return True       
    def buffmau(self):
        a=False
        for i in range(5):
            click(self.udid,913 ,367,"4")
            time.sleep(5)
            if(findFor(self.udid, 2, "buffmau.png", 1,threshold=0.8)!= 0):
                for i in range(2):
                    click(self.udid,879,324,"buff mau")
                # if(a==False):
                #     if(findFor(self.udid, 5,"hongtb.png",threshold=0.85,yclick=0))!=0:
                #         if(self.doitb()==True):
                #             a=True
                #             self.buffmau()
                #             return True
                #         else:
                #             return False
                # time.sleep(5)
                return True
            
            
        return False      
    def hongTB(self):
        if(findFor(self.udid, 1, "vethanh.png", 1)!= 0):
                        time.sleep(5)
                        self.dungdi()
        if(self.muaTB()==True):
            if(self.suDungTB()==True):
                if(self.lenbai()==True):
                        self.batauto()
                        return True
            else:
                return False
        else:
            return False
    def cFullRuong(self):
        for i in range(2):
            click(self.udid,601,495,"hanhtrang")
            time.sleep(5)
            if(findFor(self.udid, 5,"hanhtrang.png",threshold=0.85,yclick=0))!=0:
                for i in range(2):
                    click(self.udid,787,126,"o so 1")
                time.sleep(5)
                sc=screen_capture(self.udid)
                listnull=find2(sc[43:368,494:760],"otrong.png",threshold=0.75)    
                if(listnull==0):
                    for i in range(2):
                        click(self.udid,786,268,"o so 2")
                    time.sleep(5)
                    sc=screen_capture(self.udid)
                    listnull=find2(sc[43:368,494:760],"otrong.png",threshold=0.75)    
                    if(listnull==0):
                        click(self.udid, 917, 27,"nutx")
                        return True
                click(self.udid, 917, 27,"nutx")
                return False
        return False
    def muaTB(self):
        for i in range(2):
            self.tatauto()
            click(self.udid, 856,110 ,"map")
            time.sleep(5)
            if (findFor(self.udid, 1, "dichuyen.png", 0)!= 0):
                click(self.udid,687,19,"the gioi")
                time.sleep(5)
                click(self.udid,605,337,"ngu duoc")
                time.sleep(5)
                click(self.udid,397,314,"thai quang")
                self.dungdi()
                click(self.udid,814,212,"Thoai")
                time.sleep(5)
                if (findFor(self.udid, 1, "danhchotan.png", 1,threshold=0.85)!= 0):
                    time.sleep(5)
                    if (findFor(self.udid, 1, "quydoi.png", yclick=0,threshold=0.85)!= 0):
                        click(self.udid,818,309,"scroll")
                        time.sleep(5)
                        click(self.udid,745,192,"quy doi")
                        time.sleep(5)
                        if (findFor(self.udid, 1, "dongymtb.png", yclick=1,threshold=0.85)!= 0):
                            time.sleep(5)
                            for i in range(3):
                                if (findFor(self.udid, 1, "quydoi.png", yclick=0,threshold=0.85)!= 0):
                                    click(self.udid,825 ,45,"nutx")
                                else:
                                    break
                            return True
            click(self.udid,888,29,"nutxmap")
    def suDungTB(self):
        for i in range(2):
            click(self.udid, 611,507,"hanh trang")
            time.sleep(5)
            click(self.udid,787,126,"o so 1")
            time.sleep(5)
            if (findFor(self.udid, 1, "dao.png", yclick=1,threshold=0.8)!= 0):
                time.sleep(5)
                if(findFor(self.udid, 1,"sudung.png",threshold=0.8,yclick=1))!=0:
                    time.sleep(5)
                    click(self.udid,891,29,"nutx")
                    return True
            else:
                click(self.udid,786,268,"o so 2")
                time.sleep(5)
                if (findFor(self.udid, 1, "dao.png", yclick=1,threshold=0.8)!= 0):
                    time.sleep(5)
                    if(findFor(self.udid, 1,"sudung.png",threshold=0.8,yclick=1))!=0:
                        time.sleep(5)
                        click(self.udid,891,29,"nutx")
                        return True

    def fullDo(self):                
        if(findFor(self.udid, 1, "vethanh.png", 1)!= 0):
            time.sleep(5)
            self.dungdi()
            time.sleep(3)
        if(self.vDL()==True):
                time.sleep(3)
                click(self.udid,814,212,"Thoai")
                time.sleep(5)
                if (findFor(self.udid, 1, "hanhtrang.png", 0)!= 0):
                    time.sleep(3)
                    if(self.bando()==True):
                            time.sleep(3)
                        # if(self.buffmau()==True):
                            if(self.lenbai()==True):
                                    time.sleep(3)
                                    self.batauto()
                                    return True
                            else:
                                return False
                    else:
                        return False
                else:
                    return False
        else:
            return False

    def fullRuong(self):
        if(findFor(self.udid, 1, "vethanh.png", 1)!= 0):
            time.sleep(5)
            self.dungdi()
            time.sleep(3)
        if(self.vDL()==True):
            time.sleep(3)
            click(self.udid,814,212,"Thoai")
            time.sleep(5)
            if (findFor(self.udid, 1, "hanhtrang.png", 0)!= 0):
                if(self.bando()==True):
                    time.sleep(3)
                            # if(self.buffmau()==True):
                    if(self.lenbai()==True):
                        time.sleep(3)
                        self.batauto()
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    def train(self):
        start_time = time.time()
        timebuff=time.time()
        while True:
            # Kiểm tra thời gian hiện tại
            current_time = time.time()
            # Tính thời gian đã trôi qua
            elapsed_time = current_time - start_time
            elapsed_timebuff=current_time - timebuff
            # Kiểm tra nếu đã đến 20 phút
            if elapsed_time >= 3600:  # 20 phút = 1200 giây
                break
            if(elapsed_timebuff>=600):
                click(self.udid, 916, 216,"buff")
                time.sleep(5)
                self.skill()
                click(self.udid,6 ,205 )
                timebuff=time.time()
                # swipe(self.udid,83,446,142,330,300)
            # self.checkhong()
            # if(self.cFullRuong()==True):
            #         if(findFor(self.udid, 5, "vethanh.png", 1)!= 0):
            #             time.sleep(5)
            #             self.dungdi()
            #         if(self.vDL()==True):
            #             for i in range(2):
            #                 click(self.udid,814,212,"Thoai")
            #                 time.sleep(5)
            #                 if (findFor(self.udid, 5, "hanhtrang.png", 0)!= 0):
            #                     if(self.bando()==True):
            #                         if(self.buffmau()==True):
            #                             if(self.lenbai()==True):
            #                                     self.batauto() 
            #         else:
            #             break
            if(findFor(self.udid,1,"hongtb2.png",threshold=0.85,yclick=0))!=0:
                if(self.hongTB()==False):
                    break
            if(findFor(self.udid, 1,"fulldo.png",threshold=0.85,yclick=0))!=0:
                if(self.fullDo()==False):
                    break
            
            # elif(findFor(self.udid, 5,"hongtb.png",threshold=0.85,yclick=0))!=0:
            #         if(self.doitb()==True):
            #             if(self.lenbai()==True):
            #                     self.batauto()
            #             pass
            #         else:
            #             break
            elif(self.cFullRuong()==True):
                self.fullRuong()
            else:
                if(findFor(self.udid, 1, "vethanh.png", 1)!= 0):
                    time.sleep(5)
                    self.dungdi()
                    if(self.buffmau()==True):
                        
                        if(self.lenbai()==True):
                                self.batauto()
                        else:
                            break
                        
                    else:
                        break  
            
            time.sleep(180)
            

    def main(self):
        while True:
            self.loadgame()
            a=False
            for i in range(10):
                if (findFor(self.udid, 1, "dangnhap.png",1 )!= 0):
                    a=True
                    break
                else:
                    click(self.udid, 844,339 )
            if(a==False):
                continue
            else:
                time.sleep(10)
                if (findFor(self.udid, 1, "batdau.png",1 )!= 0):
                    time.sleep(random.randint(20,60)) 
                    findFor(self.udid,1,"roikhoi.png",threshold=0.8)
                    # a=self.checkMap()
                    # ck=False
                    # if(a==1):
                        # ck=True
                        # pass
                    # else:
                    if(self.lenbai()==True):
                            if(self.batauto()==True):
                                self.train()
# a=toolLQ("emulator-5554",(30))
# # print(a.giamdinh())
# while True:
#     # sc=screen_capture(a.udid)
#     # sc=sc[184:186,328:748]
#     # print(cdo(sc))
#     # time.sleep(5)
#     print(a.batauto())
#     time.sleep(5)
    