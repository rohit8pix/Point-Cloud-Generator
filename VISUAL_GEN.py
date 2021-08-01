
import open3d as open3d
import numpy as np 


def visual(rgb_path,depth_path, vis_type,filepath_saved):
	color_raw = o3d.io.read_image(rgb_path)
	depth_raw = o3d.io.read_image(rgb_path)
	rgbd_image = o3d.geometry.RGBDImage.create_from_tum_format(color_raw,depth_raw)
	if filepath_saved==None:
		pcd = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd_image,o3d.camera.PinholeCameraIntrinsic(o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault))
		# Flip it, otherwise the pointcloud will be upside down
		pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
		#o3d.io.write_point_cloud(filepath,pcd )
		if vis_type == 'RGBD':
			print(rgbd_image)
			print(rgbd_image.depth)
			print(rgbd_image.color)
		elif vis_type == 'pcd':
			print("Visualizing the pcd file")
			o3d.visualization.draw_geometries([pcd])
	else:
		pcd2 = o3d.io.read_point_cloud(filepath_saved)
		o3d.visualization.draw_geometries([pcd2])







