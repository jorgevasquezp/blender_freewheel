import bpy,os

class YSelection(bpy.types.Menu):
    bl_label = "Yoech Selection Tools"
    bl_idname = "OBJECT_MT_y_selection"

    def draw(self, context):
        layout = self.layout
        
        layout.operator_menu_enum("mesh.select_random",property="action",text="Random")
        layout.operator("mesh.select_nth")
        layout.operator("mesh.loop_multi_select",text="Select Edge Ring").ring = True
        layout.operator("mesh.loop_multi_select",text="Select Edge Loop").ring = False

def draw_item(self, context):
    layout = self.layout
    layout.menu(YSelection.bl_idname)


def register():
    bpy.utils.register_class(YSelection)

    # lets add ourselves to the main header
    bpy.types.INFO_HT_header.append(draw_item)


def unregister():
    bpy.utils.unregister_class(YSelection)

    bpy.types.INFO_HT_header.remove(draw_item)

if __name__ == "__main__":
    register()

    # The menu can also be called from scripts
    bpy.ops.wm.call_menu(name=YSelection.bl_idname)