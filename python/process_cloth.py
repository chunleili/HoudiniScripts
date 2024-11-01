# These arrays define point positions and a set of polygons composed
# of those points.  Note that the point positions could also be floating
# point values.
point_positions = ((0,0,0), (1,0,0), (1,1,0), (0,1,0))
poly_point_indices = ((0,1,2), (2,3,0))
import hou

geo = hou.pwd().geometry()

# Create all the points.
points = []
for position in point_positions:
    points.append(geo.createPoint())
    points[-1].setPosition(position)

# Now create the polygons, adding vertices that refer to the points.
for point_indices in poly_point_indices:
    poly = geo.createPolygon()
    for point_index in point_indices:
        poly.addVertex(points[point_index])