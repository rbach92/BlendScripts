#snap_origin_to_selected.py

bl_info = {
    'name' : 'Origin to Selected',
    'category' : 'Object',
    'author' : 'Ray Bach'
    }

import bpy

class origin_to_selected(bpy.types.Operator):
    bl_idname = 'object.origin_to_selected'
    bl_label = 'Origin to Selected'

    def execute(self, context):
        area = bpy.context.area
        area.type = 'VIEW_3D'
        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type = 'ORIGIN_CURSOR')
        bpy.ops.object.editmode_toggle()
        return {'FINISHED'}

def register():
    bpy.utils.register_class(origin_to_selected)

def unregister():
    bpy.utils.unregister_class(origin_to_selected)

if __name__ == '__main__':
    register()
