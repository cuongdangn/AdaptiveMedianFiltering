# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 00:27:31 2018

@author: Bit
"""

from PIL import Image

#path = "tiger.png" 
#path = "cat.png"
#path = "horse.png"
path = "input/ship.png"
img = Image.open(path)
img = img.convert('LA');
width, height = img.size
newimg = img.copy()

def getName():
	name = '';
	for i in range(6,len(path)):
		name = name+path[i]
	#print(name)
	return name
def AdaptiveMedianFilter(sMax):
	filterSize = 3
	borderSize = sMax // 2;
	imgMax = img.getpixel((0,0))
	mid = (filterSize*filterSize)//2
	for i in range(width):
	    for j in range(height):
	        if(imgMax < img.getpixel((i,j))):
	            imgMax = img.getpixel((i,j))

	for i in range(borderSize,width-borderSize):
	    for j in range(borderSize,height-borderSize):
	        members = [imgMax] * (sMax*sMax)
	        filterSize = 3
	        zxy = img.getpixel((i,j))
	        result = zxy
	        while(filterSize<=sMax):
	            borderS = filterSize // 2
	            for k in range(filterSize):
	                for t in range(filterSize):
	                    members[k*filterSize+t] = img.getpixel((i+k-borderS,j+t-borderS))
	                    #print(members[k*filterSize+t])
	            members.sort()
	            med  = (filterSize*filterSize)//2
	            zmin = members[0]
	            zmax = members[(filterSize-1)*(filterSize+1)]
	            zmed = members[med]
	            if(zmed<zmax and zmed > zmin):
	                if(zxy>zmin and zxy<zmax):
	                    result = zxy
	                else: 
	                    result = zmed
	                break
	            else:
	                filterSize += 2

	        newimg.putpixel((i,j),(result))

def renoiseInBorder():
	borderSize = 1
	for i in range(1,width):
	    for j in range(borderSize):
	        newimg.putpixel((i,j),newimg.getpixel((i,borderSize)));

	for i in range(1,width):
	    for j in range(borderSize):
	        newimg.putpixel((i,height-j-1),newimg.getpixel((i,height-borderSize-1)));

	for j in range(height):
	    for i in range(borderSize):
	        newimg.putpixel((i,j),newimg.getpixel((borderSize,j)));
	        
	for j in range(height):
	    for i in range(borderSize):
	        newimg.putpixel((width - i-1,j),newimg.getpixel((width-borderSize-1,j)));


# main
img.show()
for i in range(9,1,-2):
	img = newimg.copy()
	#print(i)
	AdaptiveMedianFilter(i)
renoiseInBorder()
newimg.show()
newimg.save("output/output_"+getName())