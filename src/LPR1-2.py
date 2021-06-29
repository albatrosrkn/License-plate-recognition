# -*- coding: utf-8 -*-

from PIL import Image,ImageFilter
import time
pathfile=input("Please enter your plate file name:")
img = Image.open(str(pathfile)+".png","r")

px=img.load()
w, h = img.size
puntoarr=[]
genislikarr=[]
print(img.format,img.size,img.mode)
count=0
for x in range(h):
    for y in range(w):
        if px[y,x] == (255,255,255):
            print (" ",end="")
        if px[y,x] == (0,0,0):
            puntoarr.append(x)
            genislikarr.append(y)
            count+=1
            print("#",end="")
    print("")
#print(genislikarr)
genislikarr.sort()
mingenislik=genislikarr[0]
maxgenislik=genislikarr[len(genislikarr)-1]
genislik=maxgenislik-mingenislik
puntoarr.sort()
minpunto=puntoarr[0]
maxpunto=puntoarr[len(puntoarr)-1]
punto=(maxpunto-minpunto)-1
#print(genislikarr)
#print("genişlik: ",genislik)
print("Punto: ",punto)
#print(puntoarr)
bolarr=[]
countarr=0
count4=0
aley=0
print("----------------------------------------------------------")
print("Plaka: ",end="")
for j in range(0,(len(genislikarr)-1)):
    temp=genislikarr[j]
    temp2=genislikarr[j+1]
    countarr+=1
    if (temp+1<temp2):
        aley+=1
        #print("countarr: ",countarr-count4)
        #print("boolarr: ",genislikarr[count4:countarr])
        bolarr=genislikarr[count4:countarr]
        #print("--------------------------------------------------------------------------------------------------------")
        if countarr-count4==30 and  bolarr[len(bolarr)-1]-bolarr[0]==6:
            print("1",end="")
        elif countarr-count4==60 and  bolarr[len(bolarr)-1]-bolarr[0]==11:
            print("2",end="")
        elif countarr-count4==37 and  bolarr[len(bolarr)-1]-bolarr[0]==10:
            print("3",end="")
        elif countarr-count4==51 and  bolarr[len(bolarr)-1]-bolarr[0]==13:
            print("4",end="")
        elif countarr-count4==52 and  bolarr[len(bolarr)-1]-bolarr[0]==9:
            print("5",end="")
        elif countarr-count4==52 and  bolarr[len(bolarr)-1]-bolarr[0]==12:
            print("6",end="")
        elif countarr-count4==40 and  bolarr[len(bolarr)-1]-bolarr[0]==11:
            print("7",end="")
        elif countarr-count4==49 and  bolarr[len(bolarr)-1]-bolarr[0]==10:
            print("8",end="")
        elif countarr-count4==47 and  bolarr[len(bolarr)-1]-bolarr[0]==12:
            print("9",end="")
        elif countarr-count4==67 and  bolarr[len(bolarr)-1]-bolarr[0]==15:
            print("E",end="")
        elif countarr-count4==62 and  bolarr[len(bolarr)-1]-bolarr[0]==20:
            print("A",end="")
        elif countarr-count4==113 and  bolarr[len(bolarr)-1]-bolarr[0]==17:
            print("B",end="")
        elif countarr-count4==59 and  bolarr[len(bolarr)-1]-bolarr[0]==16:
            print("C",end="")
        elif countarr-count4==44 and  bolarr[len(bolarr)-1]-bolarr[0]==20:
            print("D",end="")
        elif countarr-count4==67 and  bolarr[len(bolarr)-1]-bolarr[0]==15:
            print("E",end="")
        elif countarr-count4==71 and  bolarr[len(bolarr)-1]-bolarr[0]==14:
            print("F",end="")
        elif countarr-count4==31 and  bolarr[len(bolarr)-1]-bolarr[0]==20:
            print("G",end="")
        elif countarr-count4==110 and  bolarr[len(bolarr)-1]-bolarr[0]==21:
            print("H",end="")
        elif countarr-count4==40 and  bolarr[len(bolarr)-1]-bolarr[0]==7:
            print("I",end="")
        elif countarr-count4==51 and  bolarr[len(bolarr)-1]-bolarr[0]==10:
            print("J",end="")
        elif countarr-count4==102 and  bolarr[len(bolarr)-1]-bolarr[0]==21:
            print("K",end="")
        elif countarr-count4==52 and  bolarr[len(bolarr)-1]-bolarr[0]==15:
            print("L",end="")
        elif countarr-count4==58 and  bolarr[len(bolarr)-1]-bolarr[0]==26:
            print("M",end="")
        elif countarr-count4==34 and  bolarr[len(bolarr)-1]-bolarr[0]==19:
            print("O",end="")
        elif countarr-count4==81 and  bolarr[len(bolarr)-1]-bolarr[0]==14:
            print("P",end="")
        elif countarr-count4==109 and  bolarr[len(bolarr)-1]-bolarr[0]==20:
            print("R",end="")
        elif countarr-count4==58 and  bolarr[len(bolarr)-1]-bolarr[0]==11:
            print("S",end="")
        elif countarr-count4==48 and  bolarr[len(bolarr)-1]-bolarr[0]==16:
            print("T",end="")
        elif countarr-count4==8 and  bolarr[len(bolarr)-1]-bolarr[0]==20:
            print("U",end="")
        elif countarr-count4==7 and  bolarr[len(bolarr)-1]-bolarr[0]==21:
            print("V",end="")
        elif countarr-count4==9 and  bolarr[len(bolarr)-1]-bolarr[0]==21:
            print("Y",end="")
        elif countarr-count4==76 and  bolarr[len(bolarr)-1]-bolarr[0]==16:
            print("Z",end="")
        count4=countarr
        
######################################################################################################################################
bolarr=genislikarr[count4:countarr]

if (countarr-count4)+1==30 and  bolarr[len(bolarr)-1]-bolarr[0]==6:
   print("1",end="")
elif (countarr-count4)+1==60 and  bolarr[len(bolarr)-1]-bolarr[0]==11:
    print("2",end="")
elif (countarr-count4)+1==37 and  bolarr[len(bolarr)-1]-bolarr[0]==10:
    print("3",end="")
elif (countarr-count4)+1==51 and  bolarr[len(bolarr)-1]-bolarr[0]==13:
    print("4",end="")
elif (countarr-count4)+1==52 and  bolarr[len(bolarr)-1]-bolarr[0]==9:
    print("5",end="")
elif (countarr-count4)+1==52 and  bolarr[len(bolarr)-1]-bolarr[0]==12:
    print("6",end="")
elif (countarr-count4)+1==40 and  bolarr[len(bolarr)-1]-bolarr[0]==11:
    print("7",end="")
elif (countarr-count4)+1==49 and  bolarr[len(bolarr)-1]-bolarr[0]==10:
    print("8",end="")
elif (countarr-count4)+1==47 and  bolarr[len(bolarr)-1]-bolarr[0]==12:
    print("9",end="")
elif (countarr-count4)+1==67 and  bolarr[len(bolarr)-1]-bolarr[0]==15:
    print("E",end="")
elif (countarr-count4)+1==62 and  bolarr[len(bolarr)-1]-bolarr[0]==20:
    print("A",end="")
elif countarr-count4==113 and  bolarr[len(bolarr)-1]-bolarr[0]==17:
    print("B",end="")
elif countarr-count4==59 and  bolarr[len(bolarr)-1]-bolarr[0]==16:
    print("C",end="")
elif countarr-count4==44 and  bolarr[len(bolarr)-1]-bolarr[0]==20:
    print("D",end="")
elif countarr-count4==67 and  bolarr[len(bolarr)-1]-bolarr[0]==15:
    print("E",end="")
elif countarr-count4==71 and  bolarr[len(bolarr)-1]-bolarr[0]==14:
    print("F",end="")
elif countarr-count4==31 and  bolarr[len(bolarr)-1]-bolarr[0]==20:
    print("G",end="")
elif countarr-count4==110 and  bolarr[len(bolarr)-1]-bolarr[0]==21:
    print("H",end="")
elif countarr-count4==40 and  bolarr[len(bolarr)-1]-bolarr[0]==7:
    print("I",end="")
elif countarr-count4==51 and  bolarr[len(bolarr)-1]-bolarr[0]==10:
    print("J",end="")
elif countarr-count4==102 and  bolarr[len(bolarr)-1]-bolarr[0]==21:
    print("K",end="")
elif countarr-count4==52 and  bolarr[len(bolarr)-1]-bolarr[0]==15:
    print("L",end="")
elif countarr-count4==58 and  bolarr[len(bolarr)-1]-bolarr[0]==26:
    print("M",end="")
elif countarr-count4==34 and  bolarr[len(bolarr)-1]-bolarr[0]==19:
    print("O",end="")
elif countarr-count4==81 and  bolarr[len(bolarr)-1]-bolarr[0]==14:
    print("P",end="")
elif countarr-count4==109 and  bolarr[len(bolarr)-1]-bolarr[0]==20:
    print("R",end="")
elif countarr-count4==58 and  bolarr[len(bolarr)-1]-bolarr[0]==11:
    print("S",end="")
elif countarr-count4==48 and  bolarr[len(bolarr)-1]-bolarr[0]==16:
    print("T",end="")
elif countarr-count4==8 and  bolarr[len(bolarr)-1]-bolarr[0]==20:
    print("U",end="")
elif countarr-count4==7 and  bolarr[len(bolarr)-1]-bolarr[0]==21:
    print("V",end="")
elif countarr-count4==9 and  bolarr[len(bolarr)-1]-bolarr[0]==21:
    print("Y",end="")
elif countarr-count4==76 and  bolarr[len(bolarr)-1]-bolarr[0]==16:
    print("Z",end="")

else:
    print("0",end="")

count=input()    
#print("countarr: ",countarr-count4)
#print("bool :",genislikarr[count4:countarr])

    
        
    
         
