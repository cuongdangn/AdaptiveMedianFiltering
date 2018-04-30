# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 00:27:31 2018

@author: Bit
"""

from PIL import Image
path = "tiger.png" 
#path = "cat.png"
img = Image.open(path)
filterSize = 3
bolderSize = filterSize // 2
members = [(0,0)] * (filterSize*filterSize)
width, height = img.size
newimg = Image.new("L",(width,height),"white")
mid = (filterSize*filterSize)//2
for times in range(1):  # number ap filter
    for i in range(bolderSize,width-bolderSize):
        for j in range(bolderSize,height-bolderSize):
            for k in range(filterSize):
                for t in range(filterSize):
                    members[k*filterSize+t] = img.getpixel((i+k-1,j+t-1))
            members.sort()
            newimg.putpixel((i,j),(members[mid]))

for i in range(1,width):
    newimg.putpixel((i,0),newimg.getpixel((i,1)));

for i in range(1,width):
    newimg.putpixel((i,height-1),newimg.getpixel((i,height-2)));

for j in range(height):
    newimg.putpixel((0,j),newimg.getpixel((1,j)));
for j in range(height):
    newimg.putpixel((width-1,j),newimg.getpixel((width-2,j)));
    
img.show()
newimg.show()