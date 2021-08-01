

###file create/ generate PLY format

import sys
import os 
from PIL import Image


focalLength = 525.0
centerX = 319.5
centerY = 239.5
scalingFactor = 5000.0



def generate_PLY(path1,path2,filename,index):
    rgb = Image.open(path1)
    depth = Image.open(path2)

    points = []    
    for v in range(rgb.size[1]):
        for u in range(rgb.size[0]):
            color = rgb.getpixel((u,v))
            Z = depth.getpixel((u,v)) / scalingFactor
            if Z==0: continue
            X = (u - centerX) * Z / focalLength
            Y = (v - centerY) * Z / focalLength
            points.append("%f %f %f %d %d %d 0\n"%(X,Y,Z,color[0],color[1],color[2]))
    path3 = os.path.normpath('C:\\Users\\rosha\\OneDrive\\Desktop\\'+filename)
    file = open(path3,"a")
    file.write('''ply
    format ascii 1.0
    element vertex %d
    property float x
    property float y
    property float z
    property uchar red
    property uchar green
    property uchar blue
    property uchar alpha
    end_header
    %s
    '''%(len(points),"".join(points)))
    
    #file.close()

    print("DONE GENERATING PLY FILE"+str(index))


