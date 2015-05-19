# ##### BEGIN GPL LICENSE BLOCK #####
#
#  3dview_border_lines.py
#  Draw thicker lines for border edges
#  Copyright (C) 2015 Quentin Wenger
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####



bl_info = {"name": "Border Lines",
           "description": "Draw thicker lines for border edges",
           "author": "Quentin Wenger (Matpi)",
           "version": (1, 1),
           "blender": (2, 74, 0),
           "location": "3D View(s) -> Properties -> Shading",
           "warning": "",
           "wiki_url": "",
           "tracker_url": "",
           "category": "3D View"
           }



import bpy
from bpy_extras.mesh_utils import edge_face_count_dict
from mathutils import Vector
from bgl import glBegin, glLineWidth, glColor3f, glColor4f, glVertex3f, glEnd, GL_LINE_STRIP


handle = []
do_draw = [False]
point_size = [3.0]



def drawCallback():
    obj = bpy.context.object
    if obj and obj.type == 'MESH' and obj.data:
        if do_draw[0]:
            mesh = obj.data
            counts = edge_face_count_dict(mesh)
            settings = bpy.context.user_preferences.themes[0].view_3d
            show_edge_crease = mesh.show_edge_crease
            show_edge_seams = mesh.show_edge_seams
            show_edge_sharp = mesh.show_edge_sharp
            show_freestyle_edge_marks = mesh.show_freestyle_edge_marks
            
            for edge in mesh.edges:
                # border edges
                if counts[edge.key] == 1:
                    coords = [obj.matrix_world*Vector(mesh.vertices[i].co) for i in edge.key]

                    def drawColorSize(color, main=True, alpha=None):

                        if main:
                            glLineWidth(point_size[0])
                        else:
                            glLineWidth(point_size[0]/3.0)
                        if alpha is None:
                            glColor3f(*color[:3])
                        else:
                            glColor4f(color[0], color[1], color[2], alpha)
                        glBegin(GL_LINE_STRIP)
                        for coord in coords:
                            glVertex3f(*coord)
                        glEnd()
                    
                    
                    if bpy.context.mode == 'OBJECT' and (obj.show_wire or bpy.context.space_data.viewport_shade == 'WIREFRAME'):
                        if obj.select:
                            drawColorSize(settings.object_active)
                        else:
                            drawColorSize(settings.wire)

                    elif bpy.context.mode == 'EDIT_MESH':
                        main = False
                        if edge.use_freestyle_mark and show_freestyle_edge_marks:
                            drawColorSize(settings.freestyle_edge_mark)
                        elif edge.use_edge_sharp and show_edge_sharp:
                            drawColorSize(settings.edge_sharp)
                        elif edge.use_seam and show_edge_seams:
                            drawColorSize(settings.edge_seam)
                        else:
                            main = True
                            
                        if edge.crease and show_edge_crease:
                            drawColorSize(settings.edge_crease, alpha=edge.crease)
                            main = False

                        if edge.select:
                            drawColorSize(settings.edge_select, main=main)
                        else:
                            drawColorSize(settings.wire_edit, main=main)
                    
                    glLineWidth(1.0)
            


def updateScene(scene=None, force=False):
    if bpy.context.mode == 'EDIT_MESH':
        obj = bpy.context.object

        border_lines = bpy.context.window_manager.border_lines

        if border_lines.updating_locked or force:
            obj.update_from_editmode()

            for window in bpy.context.window_manager.windows:
                for area in window.screen.areas:
                    if area.type == 'VIEW_3D':
                        for region in area.regions:
                            if region.type == 'WINDOW':
                                region.tag_redraw()
                                break

class RefreshOperator(bpy.types.Operator):
    bl_idname = "wm.border_lines_refresh"
    bl_label = "Refresh"
    bl_description = "Update values"

    @classmethod
    def poll(cls, context):
        return (context.area.type == 'VIEW_3D' and
            context.mode == 'EDIT_MESH')

    def execute(self, context):
        if not context.window_manager.border_lines.updating_locked:
            updateScene(force=True)
        return {'FINISHED'}



def updateBGLData(self, context):
    point_size[0] = self.borderlines_width
    if self.borderlines_use:
        do_draw[0] = True
        return

    do_draw[0] = False


class BorderLinesCollectionGroup(bpy.types.PropertyGroup):
    borderlines_use = bpy.props.BoolProperty(
        name="Border Lines",
        description="Display border edges thicker",
        default=False,
        update=updateBGLData)
    borderlines_width = bpy.props.FloatProperty(
        name="Width",
        description="Border lines width in pixels",
        min=1.0,
        max=20.0,
        default=3.0,
        subtype='PIXEL',
        update=updateBGLData)
    updating_locked = bpy.props.BoolProperty(
        name="Locked Refresh",
        description="Whether to continuously update values",
        default=False)


    
    
def displayBorderLinesPanel(self, context):
    layout = self.layout

    border_lines = context.window_manager.border_lines

    if context.mode == 'EDIT_MESH' and border_lines.borderlines_use:
        split = layout.split(percentage=0.7)
        split.prop(border_lines, "borderlines_use")
        split2 = split.split(align=True)
        if border_lines.updating_locked:
            split2.operator("wm.border_lines_refresh", text="", icon='FILE_REFRESH', emboss=False)
            split2.prop(border_lines, "updating_locked", icon_only=True, toggle=True, icon='LOCKED')
        else:
            split2.operator("wm.border_lines_refresh", text="", icon='FILE_REFRESH')
            split2.prop(border_lines, "updating_locked", icon_only=True, toggle=True, icon='UNLOCKED')
    else:
        layout.prop(border_lines, "borderlines_use")


    if border_lines.borderlines_use:
        layout.prop(border_lines, "borderlines_width")        
        

def register():
    bpy.utils.register_module(__name__)
    bpy.types.WindowManager.border_lines = bpy.props.PointerProperty(
        type=BorderLinesCollectionGroup)
    bpy.types.VIEW3D_PT_view3d_shading.append(displayBorderLinesPanel)
    bpy.app.handlers.scene_update_post.append(updateScene)
    if not handle:
        handle[:] = [bpy.types.SpaceView3D.draw_handler_add(drawCallback, (), 'WINDOW', 'POST_VIEW')]

    

def unregister():
    bpy.types.VIEW3D_PT_view3d_shading.remove(displayBorderLinesPanel)
    del bpy.types.WindowManager.border_lines
    # to be sure...
    if updateScene in bpy.app.handlers.scene_update_post:
        bpy.app.handlers.scene_update_post.remove(updateScene)
    if handle:
        bpy.types.SpaceView3D.draw_handler_remove(handle[0], 'WINDOW')
        handle[:] = []
    bpy.utils.unregister_module(__name__)
    

if __name__ == "__main__":
    register()
