import sys
import os
import numpy  
from PIL import Image



traj_path = 'C:\\Users\\rosha\\OneDrive\\Desktop\\trajectory.txt'

def read_file(filepath):
	file = open(filepath)
	data = file.read()
	lines = data.replace(","," ").replace("\t"," ").split("\n") 
	list = [[v.strip() for v in line.split(" ") if v.strip()!=""] for line in lines if len(line)>0 and line[0]!="#"]
	list = [((l[0]),l[1:]) for l in list if l[0]!='{"mode":"full"' and len(l)>1]
	return dict(list)


offset = 0.0
maxdiff = 0.02


def match_pairs(first_list, second_list,offset, maxdiff):
	first_keys = first_list.keys()
	second_keys = second_list.keys()

	potential_matches = [(abs(float(a) - (float(b) + offset)), a, b) for a in first_keys for b in second_keys if abs(float(a) - (float(b) + offset)) < maxdiff]
	#print(potential_matches)
	potential_matches.sort()
	matches = []

	for diff, a, b in potential_matches:
	    if a in first_keys and b in second_keys:
	        list(first_keys).remove(a)
	        list(second_keys).remove(b)
	        matches.append((a, b))
	matches.sort()
	return (matches)




all_points = []
RGB = []
DEPTH = []

def generate_rgb_depth(Final_RGBD_match, potential_RGBD_match):
	list  = range(0,len(Final_RGBD_match),1)
	for frame,i in enumerate(list):
	    rgb_stamp,traj_stamp = Final_RGBD_match[i]
	    rgb_file = rgb_list[rgb_stamp][0]
	    depth_file = depth_list[potential_RGBD_match[rgb_stamp]][0]
	    #print(rgb_file.split('rgb/')[1],"rgb",depth_file.split('depth/'),"depth")
	    RGB.append(rgb_file.split('rgb/')[1])
	    DEPTH.append(depth_file.split('depth/')[1])
	return(RGB,DEPTH)







