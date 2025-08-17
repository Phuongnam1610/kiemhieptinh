from adb import *
from bandoutils import *
import numpy as np
from ocr import *
pkgame="com.blackhole.jx2mobile"
pkgame2="com.blackhole.jx2mobile/org.cocos2dx.cpp.AppActivity"

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
    def __init__(self,udid,index,packtk):
        self.udid=udid    
        self.index=index
        self.packtk=packtk
    

    def loadgame(self):
        closeGame(self.udid,pkgame)
        time.sleep(5)
        moGame(self.udid,pkgame2)
        time.sleep(random.randint(20,30))  # Random sleep between 10-30 seconds
    
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
                        logging.info('dang load')           

                        continue
                    sc1=sc[43:62,829:899]
                    time.sleep(5)
                    sc2=screen_capture(self.udid)[18:65,802:900]
                    
                    if(find3(sc2,sc1,threshold=0.99)!=0):
                        print('da ket thuc di chuyen')
                        logging.info('da ket thuc di chuyen')

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
        for i in range(2):
            self.tatauto()
            for i in range(2):
                click(self.udid, 933,69 ,"map")
                if (findFor(self.udid, 1, "nutx.png", 0)!= 0):
                    time.sleep(3)
                    click(self.udid,814,484,"the gioi")
                    click(self.udid, 413,369,"dai ly ")
                    click(self.udid, 621, 278,"chuduocdiem")
                    self.dungdi()
                    click(self.udid,723,180,"Thoai")
                    if (findFor(self.udid, 1, "hanhtrang.png", 0)!= 0):
                        return True

            self.tatNutX()
        
        
                    
    
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
            click(self.udid,66,135,"giam dinh")
            for i in range(2):
                click(self.udid,829,160,"o so 1")
            origin_list_o_so_1=getOHasItems(screen_capture(self.udid),1)
            giu_list_o_so_1=[]
            for i in (origin_list_o_so_1):
                click(self.udid, i[1][0],i[1][1] )
                click(self.udid, i[1][0],i[1][1] )
             

                if(self.cogiuonayko(i[1][0])):
                    logging.info(f"Giu o {i[0]}")

                    print("giu o nay")
                    print(i)
                    giu_list_o_so_1.append(i[0])
                click( self.udid,889,362)
            for i in range(2):
                click(self.udid,825,340,"o so 2")
            origin_list_o_so_2=getOHasItems(screen_capture(self.udid),2)
            giu_list_o_so_2=[]
            for i in (origin_list_o_so_2):
                click(self.udid, i[1][0],i[1][1] )
                

                click(self.udid, i[1][0],i[1][1] )
                if(self.cogiuonayko(i[1][0])):
                    logging.info(f"Giu o {i[0]}")

                    print("giu o nay")
                    giu_list_o_so_2.append(i[0])
                click( self.udid,889,362)
            return (loc_cac_o_can_bam(origin_list_o_so_1,giu_list_o_so_1,1),loc_cac_o_can_bam(origin_list_o_so_2,giu_list_o_so_2,2))

        return False
    def cogiuonayko(self,tdx):
        sc=screen_capture(self.udid)


        # scdo=sc[18:168,366:tdx]
        scxacxuat=sc[184:522,366:tdx]
        # if(find2(scdo,"giudo1.png",threshold=0.7)!= 0):
        #     print('giu do 1')
        #     return True
        # if(find2(scdo,"giudo2.png",threshold=0.7)!= 0):
        #     print('giu do 2')
        #     return True
        # if(find2(scdo,"giudo3.png",threshold=0.7)!= 0):
        #     print('giu do 3')

        #     return True
        # if(find2(scdo,"giudo4.png", threshold=0.7)!= 0):  
        #     print('giu do 4')

        #     return True
        # if(find2(scdo,"giudo5.png", threshold=0.7)!= 0):
        #     print('giu do 5')

        #     return True
        # if(find2(scdo,"phaohoa.png", threshold=0.8)!= 0):
        #     print('giu do phao hoa')

        #     return True
        if(find2(scxacxuat,"xacxuattim.png", threshold=th)!= 0):
            logging.info('giu do xac xuat tim')
            return True
        if(find2(scxacxuat,"xacxuatxanh.png", threshold=th)!= 0):
            logging.info('giu do xac xuat xanh')
            return True
        if(find2(scxacxuat,"yeucauxanh.png", threshold=th)!= 0):
            logging.info('giu do yeucau xanh')      
            return True
        if(find2(scxacxuat,"yeucautim.png", threshold=th)!= 0):
            logging.info('giu do yeucau tim')

            return True
        return False
    def suachua(self):
        for i in range(2):
            click(self.udid,68,92,"sua chua")
            click(self.udid, 36, 25,"avatar")
            click(self.udid, 60,151,"o so 1" )
            click(self.udid, 56,191,"o so 2" )
            click(self.udid, 63,241,"o so 3" )
            click(self.udid, 59,371,"o so 6" )
            click(self.udid,12,68,"nutx")

            return True
        return False
    def bando(self):
        listcx=self.giamdinh()#tra ve cac o can bam
        logging.info("cac o can bam %s",listcx)
        if(listcx==False):
            return False
        click(self.udid, 67,202,"ban nhanh" )
        for i in range(2):
            click(self.udid,829,160,"o so 1")
        for i in (listcx[0]):
            click(self.udid, i[0],i[1] )
            click(self.udid, i[0],i[1] )
        for i in range(2):
            click(self.udid,825,340,"o so 2")
        for i in (listcx[1]):
            click(self.udid, i[0],i[1] )
            click(self.udid, i[0],i[1] )
        click( self.udid,889,362)
        vang=self.checkVangHon10()
        self.tatNutX()
        if(vang==True):
            return self.guivangthukho()

        return True
    def tatNutX(self):
        for i in range(5):
            if (findFor(self.udid, 1, "nutx.png", 1)==0):
                return True
        return False

    def lenbai(self):
        for i in range(2):
            click(self.udid, 933,69 ,"map")
            if (findFor(self.udid, 1, "nutx.png", 0)!= 0):
                time.sleep(3)
                click(self.udid,814,484,"the gioi")
                for i,v in enumerate(self.index):
                    if(i==len(self.index)-1):
                        click(self.udid,528,476)
                        # doubleclick(self.udid,508,477,"o so 1")
                        delete(self.udid)
                        sendtext(self.udid,v[0])
                        time.sleep(1)
                        click(self.udid,561,481)
                        delete(self.udid)
                        sendtext(self.udid,v[1])
                        click(self.udid,621,480,"xac nhan")
                        click(self.udid,621,480,"xac nhan")
                    else:    
                        click(self.udid,v[0],v[1])

                self.dungdi()
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
        click(self.udid,936,229,"ngua")
        click(self.udid, 818, 76,"buff")
        for i in range(3):
            click(self.udid, 818, 125,"auto")
            click(self.udid, 818, 125,"auto")
            click(self.udid, 818, 125,"auto")
            sc=screen_capture(self.udid)
            sc=sc[99:141,790:842]
            if (find2(sc,"batauto.png")!=0):
                logging.info("bat auto thanh cong")
                return True
            # swipe(self.udid,83,446,142,330,500)
            # time.sleep(3)
            # swipe(self.udid,83,446,83,330,500)
        return False
        
    def tatauto(self):

        for i in range(3):
            click(self.udid, 818, 125,"auto")
            sc=screen_capture(self.udid)
            sc=sc[99:141,790:842]
            if (find2(sc,"batauto.png")==0):
                logging.info("tat auto thanh cong")
                return True
            swipe(self.udid,83,446,142,330,500)
            time.sleep(3)
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
                logging.info(f'thay tb so {i} hong')
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
            click(self.udid,893,180,"tui do")
            if(findFor(self.udid, 5,"hanhtrang.png",threshold=0.85,yclick=0))!=0:
                for i in range(2):
                    click(self.udid,829,160,"o so 1")
                listnull=getOHasItems(screen_capture(self.udid),1)
                print(' o full do so 1', len(listnull))
                logging.info(' o full do so 1 %s', len(listnull))
                if(len(listnull)>=30):
                    

                    for i in range(2):
                        click(self.udid,825,340,"o so 2")
                    listnull=getOHasItems(screen_capture(self.udid),2)
                    print(' o full do so 2', len(listnull))
                    logging.info(' o full do so 2 %s', len(listnull))
                    if(len(listnull)>=20):
                        self.tatNutX()
                        return True
                self.tatNutX()
                return False
        return False
    def muaTB(self):
        for i in range(2):
            self.tatauto()
            for i in range(2):
                click(self.udid, 933,69 ,"map")
                if (findFor(self.udid, 1, "nutx.png", 0)!= 0):
                    time.sleep(3)
                    click(self.udid,814,484,"the gioi")
                    click(self.udid, 413,369,"dai ly ")
                    click(self.udid,134,152,"chu tiem vu khi")
                    self.dungdi()
                    click(self.udid,723,180,"Thoai")
                    if (findFor(self.udid, 1, "muavukhi.png", 1,threshold=0.85)!= 0):
                        if (findFor(self.udid, 1, "hanhtrang.png", yclick=0,threshold=0.85)!= 0):
                            click(self.udid,248,387,"dan")
                            click(self.udid,728,339,"mua")
                            self.tatNutX()

                            return True
            self.tatNutX()
    #dành cho mua kiếm
    def muaTBKIEM(self):
        for i in range(2):
            self.tatauto()
            for i in range(2):
                click(self.udid, 933,69 ,"map")
                if (findFor(self.udid, 1, "nutx.png", 0)!= 0):
                    time.sleep(3)
                    click(self.udid,814,484,"the gioi")
                    click(self.udid,406,305,"ngamy")
                    click(self.udid,539,159,"diep tu hinh")
                    self.dungdi()
                    click(self.udid,723,180,"Thoai")
                    if (findFor(self.udid, 1, "chotanthu.png", 1,threshold=0.85)!= 0):
                        if (findFor(self.udid, 1, "hanhtrang.png", yclick=0,threshold=0.85)!= 0):
                            click(self.udid,130,112,"thanh tam to kiem")
                            click(self.udid,728,339,"mua")
                            self.tatNutX()

                            return True
            self.tatNutX()
    def suDungTB(self):
        for i in range(2):
            click(self.udid,893,180,"tui do")
            if(findFor(self.udid, 5,"hanhtrang.png",threshold=0.75,yclick=0))!=0:
                for i in range(2):
                    click(self.udid,829,160,"o so 1")                
                if (findFor(self.udid, 1, "sudungdan.png", yclick=1,threshold=0.7)!= 0):
                    if(findFor(self.udid, 1,"btnsudung.png",threshold=0.65,yclick=1))!=0:
                        self.tatNutX()
                        return True
            else:
                click(self.udid,825,340,"o so 2")
                if (findFor(self.udid, 1, "sudungdan.png", yclick=1,threshold=0.7)!= 0):
                    if(findFor(self.udid, 1,"btnsudung.png",threshold=0.65,yclick=1))!=0:
                        self.tatNutX()
                        return True

    def fullDo(self):                
        if(findFor(self.udid, 1, "vethanh.png", 1)!= 0):
            time.sleep(5)
            self.dungdi()
            time.sleep(3)
        if(self.vDL()==True):
            if(self.bando()==True):
                    if(self.lenbai()==True):
                            self.batauto()
                            return True
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
            if(self.bando()==True):
                        # if(self.buffmau()==True):
                if(self.lenbai()==True):
                    self.batauto()
                    return True
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
                click(self.udid, 818, 76,"buff")
                timebuff=time.time()
            if(findFor(self.udid,1,"hongtb2.png",threshold=0.85,yclick=0))!=0:
                if(self.hongTB()==False):
                    break
            if(findFor(self.udid, 1,"fulldo.png",threshold=0.85,yclick=0))!=0:
                if(self.fullDo()==False):
                    break
            elif(self.cFullRuong()==True):
                self.fullRuong()
            else:
                if(findFor(self.udid, 1, "vethanh.png", 1)!= 0):
                    time.sleep(5)
                    self.dungdi()                        
                    if(self.lenbai()==True):
                            self.batauto()
                    else:
                        break
                        
                   
            
            time.sleep(180)
    def vethukho(self):
       
        for i in range(2):
            click(self.udid, 933,69 ,"map")
            if (findFor(self.udid, 1, "nutx.png", 0)!= 0):
                time.sleep(3)
                click(self.udid,814,484,"the gioi")
                click(self.udid, 413,369,"dai ly ")
                click(self.udid, 667, 211,"thu kho")
                self.dungdi()
                click(self.udid,723,180,"Thoai")
                if (findFor(self.udid, 1, "hanhtrang.png", 0)!= 0):
                    return True
    def checkVangHon10(self):
        anh=screen_capture(udid=self.udid)
        anh=anh[430:446,663:682]
        if(getNumber(anh)>10):
            return True
        else:
            return False

    
    def catvang(self):
        for i in range(2):
            click(self.udid,47,133,"gui vang")
            click(self.udid,327,235,"o nhap vang")
            sendtext(self.udid,"8")
            if(findFor(self.udid,1,"dongy.png",threshold=0.85,yclick=1))!=0:
               self.tatNutX()
               return True
        self.tatNutX()
        return False
           
    def guivangthukho(self):
            if(self.vethukho()==True):
                return self.catvang()
            else:
                return False
   


        

                

            

    # def main(self):
    #     while True:
    #         self.loadgame()
       
    #         if (findFor(self.udid, 10, "btnvang.png",1 )== 0):
    #             continue
        
    #         else:
    #             time.sleep(random.randint(5,10))
    #             ClickedSignIn=False
    #             if(findFor(self.udid, 1, "3cid.png",1 )!= 0):
    #                 time.sleep(2)
    #                 doubleclick(self.udid,326,193)
    #                 print("tk la ",self.packtk[0])
    #                 print("mk la ",self.packtk[1])


    #                 sendtext(self.udid,self.packtk[0])
    #                 click(self.udid,314,246)
    #                 doubleclick(self.udid,314,246)
    #                 sendtext(self.udid,self.packtk[1])
                    
    #                 if(findFor(self.udid, 1, "signin.png",1 )!= 0):
    #                     ClickedSignIn=True
    #             if(ClickedSignIn==False):
    #                 continue
    #             time.sleep(random.randint(15,30)) 
    #             if(findFor(self.udid, 1, "btnvang.png",1 )== 0):
    #                 continue
    #             time.sleep(random.randint(15,30)) 
    #             findFor(self.udid,1,"nutx.png",yclick=1,threshold=0.8)
    #             if(self.lenbai()==True):
    #                     if(self.batauto()==True):
    #                         self.train()
    
    def main(self):###ld9
        try:
            
            while True:
                self.loadgame()
        
                if (findFor(self.udid, 10, "btnvang.png",1 )!= 0):
                    # continue
            
                # else:
                    time.sleep(random.randint(5,10))
                    ClickedSignIn=False
                    if(findFor(self.udid, 1, "3cidld9.png",1 )!= 0):
                        
                        if(findFor(self.udid, 1, "signinld9.png",1 )!= 0):
                            ClickedSignIn=True
                    if(ClickedSignIn==False):
                        continue
                    time.sleep(random.randint(15,30)) 
                    if(findFor(self.udid, 1, "btnvang.png",1 )== 0):
                        continue
                    time.sleep(random.randint(15,30)) 
                    findFor(self.udid,1,"nutx.png",yclick=1,threshold=0.8)
                    if(self.lenbai()==True):
                            if(self.batauto()==True):
                                self.train()
        except Exception as e:
            logging.error(e)
# a=toolLQ("emulator-5554",((405 ,369 ),(749 ,151),( 479 ,444 ),(203 ,180)),("A","B"))
# a.train()
