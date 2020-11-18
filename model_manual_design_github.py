# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 10:15:18 2020

@author: medea
"""

import cv2
maximumx = 334 # x size in micrometers
maximumy = 270 # y size in micrometers
img=cv2.imread('input.png')
number_of_pixels = img.shape

max_x_pixels = number_of_pixels[1]
max_y_pixels = number_of_pixels[0]
list_coordinatesx = []
list_coordinatesy = []

def draw_circle1(event,x,y,flags,param):
    global mouseX,mouseY
    global d
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),5,(0,0,255),-1)    
        mouseX,mouseY = x,y
        list_coordinatesx.append(mouseX)
        list_coordinatesy.append(mouseY)
        print(mouseX,mouseY)
        if len (list_coordinatesx)> 1:
            cv2.line(img, (list_coordinatesx[-2],list_coordinatesy[-2]), (list_coordinatesx[-1],list_coordinatesy[-1]), (255,0,0), 3)
        
cv2.namedWindow('image',cv2.WINDOW_NORMAL )
cv2.setMouseCallback('image',draw_circle1)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(20)
    if k ==27:
        break        


cv2.imwrite('points.png', img)
cv2.destroyAllWindows()
#replacing the closest points by only one point
for t in range (0, len(list_coordinatesx)):
    for g in range (0, len(list_coordinatesx)):
        if g != t:
            dist = abs ((list_coordinatesx[t]) -(list_coordinatesx[g]))+ abs((list_coordinatesy[t]) -(list_coordinatesy[g]))
            
            if dist < 10: #coordinates in pixels
                list_coordinatesx[t] = list_coordinatesx[g]
                list_coordinatesy[t] = list_coordinatesy[g]
                
    

list_string = [] 
list_opposite_string =[]# testing the edge in the other direction
for i in range (1, len(list_coordinatesx)):
    list_string.append(str((list_coordinatesx[i-1]/max_x_pixels)*maximumx) + ' ' + str((list_coordinatesy[i-1]/max_y_pixels)*maximumy)+ ' ' + str((list_coordinatesx[i]/max_x_pixels)*maximumx) + ' ' + str((list_coordinatesy[i]/max_y_pixels)*maximumy))
    list_opposite_string.append(str((list_coordinatesx[i]/max_x_pixels)*maximumx) + ' ' + str((list_coordinatesy[i]/max_y_pixels)*maximumy)+ ' ' + str((list_coordinatesx[i-1]/max_x_pixels)*maximumx) + ' ' + str((list_coordinatesy[i-1]/max_y_pixels)*maximumy))
list_processed = []
for a in range (0, len(list_string)):
    if list_string[a] not in list_processed and list_opposite_string[a]  not in list_processed:
        list_processed.append(list_string[a])
textfile = open('out.txt','w+') #this out file will be read by FEM software, it contains all the clicked boundaries
for b in range (0, len(list_processed)):
    textfile.write(list_processed[b])
    textfile.write('\n')

textfile.close()

textfile2 = open('pixels_coordinates.txt','w+') #this file records the pixels of clicked points 

for c in range (0, len(list_coordinatesx)):
    mystr = str(list_coordinatesx[c]) + ' ' +str(list_coordinatesy[c])
    textfile2.write(mystr)
    textfile2.write('\n')

textfile2.close()




