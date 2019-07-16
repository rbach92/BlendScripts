#mixamo_rename.py
#created by Ray Bach
#simply gets rid of the 'mixamorig:' prefix that
#mixamo attaches to joints

import bpy

#get all objects in scene
scene = bpy.context.scene
objects = bpy.context.scene.objects

#set rig to be active
for obj in objects:
    if obj.type == "ARMATURE":
        obj.select
        scene.objects.active = obj

#rename bones that have mixamo's prefix
bpy.ops.object.editmode_toggle()
for bone in bpy.context.active_object.data.edit_bones[:]:
    if bone.name[0:10] == 'mixamorig:':
        bone.name = bone.name[10:]
