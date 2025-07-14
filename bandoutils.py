import cv2 
from adb import find3
def chiaO(crop,trang):
    listO=[]
    if(trang==1):
        hang=7
    else:
        hang=6
        
    for row in range(1,hang):
        for col in range(1,6):
            x1 = (col-1) * 48+7*(col-1)
            y1 = (row-1) * 48+7*(row-1)
            x2 = x1 + 48
            y2 = y1 + 48
            if(row==1):
                y1=16
                y2=48
            if(col==1):
                x1=0
            center_x = x1 + 48 // 2
            center_y = y1 + 48 // 2
            listO.append(((529+center_x,center_y+93), crop[y1:y2, x1:x2]))#tọa độ trung điểm và ảnh
            # print(f"{row} {col} {x1} {y1} {x2} {y2}")
    return listO


def getOHasItems(screen_capture,trang):
    fulldo=screen_capture[90:421,526:805]
    otrong = chiaO(cv2.imread("image\\fulltrong.png"),trang)
    ofulldo=chiaO(fulldo,trang)
    different_cells = []
    for i,v in enumerate(ofulldo):
        # cv2.imwrite("sosanh"+str(i)+".png",v[1])
        # cv2.imwrite("sosanhotrong"+str(i)+".png",otrong[i][1])
        if(find3(v[1],otrong[i][1],threshold=0.7)==0):
            different_cells.append(((i+1),v[0]))
    return different_cells


def get_cell_center(index, num_cols=5, cell_size=48):
    row = (index - 1) // num_cols
    col = (index - 1) % num_cols
    x = col * cell_size + cell_size / 2
    y = row * cell_size + cell_size / 2
    return (x, y)
def loc_cac_o_can_bam(listcg,trang):
    list_o_can_bam=[]
    if(trang==1):
        slo=31
    else:
        slo=21
    for i in range(1,slo):
        if(i not in listcg):
            list_o_can_bam.append(get_cell_center(i))
    return list_o_can_bam
