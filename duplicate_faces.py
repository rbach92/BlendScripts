#duplicate_faces.py

bl_info = {
    'name' : 'Duplicate Faces',
    'category' : 'Object',
    'author' : 'Ray Bach'
    }

import bpy

class duplicate_faces(bpy.types.Operator):
    bl_idname = 'object.duplicate_faces'
    bl_label = 'Duplicate Faces'

    def execute(self, context):
        area = bpy.context.area
        area.type = 'VIEW_3D'
        bpy.ops.mesh.duplicate(mode = 1)
        bpy.ops.mesh.separate(type = 'SELECTED')
        bpy.ops.object.editmode_toggle()
        return {'FINISHED'}

def register():
    bpy.utils.register_class(duplicate_faces)

def unregister():
    bpy.utils.unregister_class(duplicate_faces)

if __name__ == '__main__':
    register()
