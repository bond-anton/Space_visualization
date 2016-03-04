import numpy as np
from mayavi import mlab

from Space.Coordinates import Cartesian
from Space.Curve.Parametric import Helix
from Space.Pathfinder import helix_between_two_points, arc_between_two_points
import Space_visualization as Visual

coordinate_system = Cartesian()
coordinate_system.rotate_axis_angle(np.ones(3), np.deg2rad(45))

fig = mlab.figure('CS demo', bgcolor=(0, 0, 0))
Visual.draw_coordinate_system_axes(fig, coordinate_system)

right_helix = Helix(name='Right Helix', coordinate_system=coordinate_system,
                    radius=2, pitch=0.5, start=0, stop=np.pi * 4, right=True)
left_helix = Helix(name='Left Helix', coordinate_system=coordinate_system,
                   radius=2, pitch=0.5, start=0, stop=np.pi * 2, right=False)

print 'Helix length:', left_helix.length()

right_helix_view = Visual.CurveView(fig=fig, curve=right_helix)
right_helix_view.draw()

left_helix_view = Visual.CurveView(fig=fig, curve=left_helix)
left_helix_view.draw()

point1 = np.array([1, 1, 0])
point2 = np.array([2, 2, 0])
points = np.vstack((coordinate_system.to_parent(point1), coordinate_system.to_parent(point2)))
mlab.points3d(points[:, 0], points[:, 1], points[:, 2], scale_factor=0.1)

helix_path = helix_between_two_points(coordinate_system, point1, point2, radius=1, loops=7, right=True)
helix_path_view = Visual.CurveView(fig=fig, curve=helix_path)
helix_path_view.draw()

'''
path = arc_between_two_points(coordinate_system, point1, point2, radius=1, right=True)

t = np.linspace(path.start, path.stop, num=101 * (path.stop - path.start) / (2 * np.pi), endpoint=True)
points = path.generate_points(t)
global_points = path.coordinate_system.to_parent(points)
mlab.plot3d(global_points[:, 0], global_points[:, 1], global_points[:, 2], color=(0, 1, 0))
Visual.draw_coordinate_system_axes(fig, path.coordinate_system)
'''
mlab.show()
