"""
从文件中读取tri.txt
"""
import hou
import numpy as np

node = hou.pwd()
geo = node.geometry()

# 文件路径
file_path = node.parm("file").eval()
print("Reading from: ", file_path)

# 读取数据
data = np.loadtxt(file_path, skiprows=1, dtype=int)
print(data)

# 创建点
points = []
for i in range(np.max(data) + 1):
    points.append(geo.createPoint())

# 创建三角形
for tri in data:
    p1 = points[tri[0]]
    p2 = points[tri[1]]
    p3 = points[tri[2]]
    poly = geo.createPolygon()
    poly.addVertex(p1)
    poly.addVertex(p2)
    poly.addVertex(p3)
    