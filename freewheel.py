bl_info = {
    "name": "Freewheel",
    "author": "Jorge Vasquez",
    "version": (1, 0),
    "blender": (2, 74, 0),
    "description": "My Workflow tools",
    "category": "User Interface Preferences",
    "wiki_url": "http://www.yorchnet.com"}

import bpy
from bpy.types import Operator
from bpy.props import FloatVectorProperty
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector

class VIEW3D_MENU_YSelection(bpy.types.Menu):
    bl_label = "Yoech Selection Tools"
    bl_idname = "VIEW3D_MENU_YSelection"

    def draw(self, context):
        layout = self.layout
        
        layout.operator_menu_enum("mesh.select_random",property="action",text="Random")
        layout.prop_menu_enum(context.space_data, "viewport_shade")
        layout.operator("mesh.select_nth")
        layout.operator("mesh.loop_multi_select",text="Select Edge Ring").ring = True
        layout.operator("mesh.loop_multi_select",text="Select Edge Loop").ring = False
        layout.operator("space_data.viewport_shade",text="Wireframe").vlaue = "WIREFRAME"

#def add_object(self, context):
#    scale_x = self.scale.x
#    scale_y = self.scale.y
#
#    verts = [Vector((-1 * scale_x, 1 * scale_y, 0)),
#             Vector((1 * scale_x, 1 * scale_y, 0)),
#             Vector((1 * scale_x, -1 * scale_y, 0)),
#             Vector((-1 * scale_x, -1 * scale_y, 0)),
#            ]
#
#    edges = []
#    faces = [[0, 1, 2, 3]]
#
#    mesh = bpy.data.meshes.new(name="New Object Mesh")
#    mesh.from_pydata(verts, edges, faces)
#    # useful for development when the mesh may be invalid.
#    # mesh.validate(verbose=True)
#    object_data_add(context, mesh, operator=self)


#class OBJECT_OT_add_object(Operator, AddObjectHelper):
#    """Create a new Mesh Object"""
#    bl_idname = "mesh.add_object"
#    bl_label = "Add Mesh Object"
#    bl_options = {'REGISTER', 'UNDO'}
#
#    scale = FloatVectorProperty(
#            name="scale",
#            default=(1.0, 1.0, 1.0),
#            subtype='TRANSLATION',
#            description="scaling",
#            )
#
#    def execute(self, context):
#
#        add_object(self, context)
#
#        return {'FINISHED'}


# Registration

#def add_object_button(self, context):
#    self.layout.operator(
#        OBJECT_OT_add_object.bl_idname,
#        text="Add Object",
#        icon='PLUGIN')

addon_keymaps = [] # I' guessing this is the place to save original keymaps..., to be deregistered when needed.

#classes = (VIEW3D_MENU_YSelection)

def register():
    #for cls in classes:
    #    bpy.utils.register_class(cls)
    bpy.utils.register_class(VIEW3D_MENU_YSelection)    
        
    wm = bpy.context.window_manager

    if wm.keyconfigs.addon:
        km = wm.keyconfigs.addon.keymaps.new('Mesh', space_type='EMPTY', region_type='WINDOW', modal=False)
        kmi = km.keymap_items.new("wm.call_menu", 'W', 'PRESS', alt=True)
        kmi.properties.name = "VIEW3D_MENU_YSelection"


        #kmi = km.keymap_items.new('wm.call_menu_pie', 'TAB', 'PRESS')
        #kmi.properties.name = 'VIEW3D_PIE_object_mode'
        
        addon_keymaps.append(km)

        
#    bpy.utils.register_class(OBJECT_OT_add_object)
#    bpy.utils.register_manual_map(add_object_manual_map)
#    bpy.types.INFO_MT_mesh_add.append(add_object_button)


def unregister():
    bpy.utils.unregister_class(YSelection)

    #bpy.types.INFO_HT_header.remove(draw_item)

if __name__ == "__main__":
    register()
