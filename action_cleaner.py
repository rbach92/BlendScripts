import bpy

actions = bpy.data.actions
objects = bpy.data.objects

saved_actions = []

#iterate thru all objects, save their action names
for obj in objects:
    if obj.animation_data:
        saved_actions.append(obj.animation_data.action.name)

#delete actions that aren't used by any objects
for act in actions:
    if act.name not in saved_actions:
        act.user_clear()

bpy.ops.wm.save_mainfile()
bpy.ops.wm.revert_mainfile()
