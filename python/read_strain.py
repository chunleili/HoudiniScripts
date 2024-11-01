"""
从文件中读取strain.txt数据，并将其写入到几何体的primitive属性中。
"""
node = hou.pwd()
geo = node.geometry()

import hou
import numpy as np

# 文件路径
file_path = node.parm("file").eval()
print("Reading from: ",file_path)

# 获取当前节点的几何体
node = hou.pwd()
geo = node.geometry()
strain_data = np.loadtxt(file_path, skiprows=1)

# 确保几何体中有足够的 primitives
num_prims = len(geo.prims())
print("num_prims: ", num_prims)
if num_prims < len(strain_data):
    for _ in range(len(strain_data) - num_prims):
        geo.createPolygon()

# 为每个 primitive 创建一个名为 "strain" 的属性，并设置其值
for i, prim in enumerate(geo.prims()):
    prim.setAttribValue("strain", strain_data[i])

print("Strain data has been written to primitive attributes.")