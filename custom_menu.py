#custom_menu.py

bl_info = {
        "name": "Custom Menu",
        "category": "3D View",
        "author": "Ray Bach"
        }        

import bpy

# Creates a menu for global 3D View
class customMenu(bpy.types.Menu):
    bl_label = "Custom Menu"
    bl_idname = "view3D.custom_menu"

    # Set the menu operators and draw functions
    def draw(self, context):
        layout = self.layout

        layout.operator('mesh.remove_doubles')
        layout.operator('mesh.faces_shade_smooth')
        layout.operator('mesh.faces_shade_flat')
        layout.operator('mesh.vertices_smooth')
        layout.operator('mesh.mark_sharp')
        layout.operator('mesh.mark_seam')
        layout.operator('mesh.edge_rotate')
        layout.operator('mesh.subdivide')
        layout.operator('mesh.merge')

def register():
    bpy.utils.register_class(customMenu)

def unregister():
    bpy.utils.unregister_class(customMenu)

if __name__ == "__main__":
    register()
