# ##### BEGIN GPL LICENSE BLOCK #####
#
# ogl_velocitiesrenderer.py
# Example client script for physics_handle_cache
# Copyright (C) 2016 Quentin Wenger
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

"""
TO BE USED WITH physics_handle_cache ADDON

Usage:
1) install and enable physics_handle_cache in Blender
2) load this script into Blender's text editor
3) on an object with cached fluidsim, refresh the list of scripts
   in the physics properties / handle cache panel
4) enable the checkbox corresponding to this script
5) at frame change this script shows vertices as blue points and
   velocities as yellow lines.

"""




import bpy
import bgl

class OpenGLVelocitiesRenderer(object):

    def __init__(self, interfacer, name):
        super(OpenGLVelocitiesRenderer, self).__init__()
        self.interfacer = interfacer
        self.name = name
        self.handle = bpy.types.SpaceView3D.draw_handler_add(
            self.drawCallback, (), 'WINDOW', 'POST_VIEW')
        self.do_draw = False
        self.vertices = None
        self.velocities = None

    def __del__(self):
        bpy.types.SpaceView3D.draw_handler_remove(
            self.handle, 'WINDOW')
        super(OpenGLVelocitiesRenderer, self).__del__()

    def update(self, scene):
        # this method is used by the addon -
        # should be provided!
        self.do_draw = self.interfacer.isActive(self.name)
        if self.do_draw:
            # are these copies?
            self.vertices = self.interfacer.getCurrentObject().verts
            self.velocities = self.interfacer.getCurrentVelocity().vels

    def drawCallback(self):
        mat = self.interfacer.getBlenderObject().matrix_world
        if self.do_draw and self.interfacer.isClean():
            # isClean() is not really needed here, but it shows its
            # behavior and helps reducing (a tiny bit!) the run time...
            bgl.glColor3f(0.0, 1.0, 1.0)
            bgl.glPointSize(5)
            bgl.glBegin(bgl.GL_POINTS)
            for v in self.vertices:
                bgl.glVertex3f(*(mat*v))
            bgl.glEnd()
            bgl.glPointSize(1)

            bgl.glColor3f(1.0, 1.0, 0.0)
            bgl.glLineWidth(2)
            bgl.glBegin(bgl.GL_LINES)
            for v, w in zip(self.vertices, self.velocities):
                bgl.glVertex3f(*(mat*v))
                bgl.glVertex3f(*(mat*(v + w)))
            bgl.glEnd()
            bgl.glLineWidth(1)


# this in toplevel is also requested
# MAIN_CLASS should be set to any callable returning the
# requested instance, which provides the update() method.
MAIN_CLASS = OpenGLVelocitiesRenderer
