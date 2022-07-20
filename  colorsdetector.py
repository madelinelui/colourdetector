import argparse 
import cv2
import pandas as pd
import numpy as np
import os 

print(os.getcwd())

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(ap.parse_args())

img_path = args['image']
#read image w opencv
img = cv2.imread(img_path)

#read csv and give names to columns
index=["colour", "colour_name", "hex","R","G","B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

#create window to display image input
cv2.namedWindow('image')

def draw_function(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked=True
        xpos=x
        ypos=y
        b,g,r = img[y,x]
        b=int(b)
        g=int(g)
        r=int(r)

cv2.setMouseCallBack('image', draw_function)

def getColorName(R,G,B):
    minimum=10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"])) + abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"colour_name"]
    return cname

while(1):
    cv2.imshow("image",img)
    if (clicked):
        #cv2.rectangle(image, startpoint, endpoint, color, thickness) -1 thickness fills rectangle entirely
        cv2.rectangle(img, (20,20), (750,60), (b,g,r), -1)

        #create text string to display
        text = getColorName(r,g,b) + ' R='+ str(r) + ' G='+ str(g) + ' B='+ str(b)

        #cv2.putText(img,text,start,font(0-7), fontScale, color, thickness, lineType, (optional bottomLeft bool) )
        cv2.putText(img, text, (50,50), 2, 0.8, (255,255,255), 2, cv2.LINE_AA)
        #for light colours, will display in black
        if(r+g+b>=600):
            cv2.putText(img, text, (50,50), 2, 0.8, (0,0,0), 2, cv2.LINE_AA)

        clicked=False

        #press Esc to break loop
        if cv2.waitKey(20) & 0xFF == 27:
            break
cv2.destroyAllWindows()





