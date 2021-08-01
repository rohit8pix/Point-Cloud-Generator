from PairImgDpt import *
from PLY_GEN import generate_PLY
from VISUAL_GEN import visual
from PCD_GEN import generate_pcd

rgb_path = "C:\\Users\\rosha\\OneDrive\\Desktop\\rgb_list.txt"
depth_path = "C:\\Users\\rosha\\OneDrive\\Desktop\\depth_list.txt"
traj_path = 'C:\\Users\\rosha\\OneDrive\\Desktop\\trajectory.txt'


rgb_list = read_file(rgb_path)
depth_list = read_file(depth_path)
pose_list = read_file(traj_path)

potential_RGBD_match = dict(match_pairs(rgb_list, depth_list,offset,maxdiff))
Final_RGBD_match= match_pairs(potential_RGBD_match, pose_list,0.0,0.01)
Final_RGBD_match.sort()



RGB = []
DEPTH = []

RGB, DEPTH =generate_rgb_depth(Final_RGBD_match, potential_RGBD_match)

limit = len(RGB) #user defined file geneartion limit

for i in range(len(RGB)):

	if (i<limit):
		path1 =os.path.normpath('C:\\Users\\rosha\\OneDrive\\Desktop\\rgbd_dataset_freiburg1_xyz\\rgb\\'+RGB[i])
		path2 = os.path.normpath('C:\\Users\\rosha\\OneDrive\\Desktop\\rgbd_dataset_freiburg1_xyz\\depth\\'+DEPTH[i])
		print("processing................" + str("")+str(i))
		#print(path2)
		save_To = 'rohit.ply'
		#file = filename+str(i+1)+'.txt'
		generate_PLY(path1,path2,save_To,i)
		#break


file  = open('rohit.ply','r')
count = 0
content = file.read()
colist = content.split('\n')

for i in colist:
	if i:
		count+=1
print(count)

#save_To_pcd = filepath


for i in range(len(RGB)):
	path1 =os.path.normpath('C:\\Users\\rosha\\OneDrive\\Desktop\\rgbd_dataset_freiburg1_xyz\\rgb\\'+RGB[i])
	path2 = os.path.normpath('C:\\Users\\rosha\\OneDrive\\Desktop\\rgbd_dataset_freiburg1_xyz\\depth\\'+DEPTH[i])
	visual(path1,path2,'RGBD', None)
	visual(path1,path2,'PCD',None)
	generate_pcd(path1,path2,save_To_pcd)