import bpy

scene = bpy.context.scene
objects = bpy.context.scene.objects

#"clicks" on an object
def selectOBJ(obj):
    scene.objects.active = obj
    obj.select = True
    return

source_rig = bpy.data.objects['source']
target_rig = bpy.data.objects['target']

selectOBJ(target_rig)
bpy.ops.object.mode_set(mode='EDIT')

bones = bpy.context.active_object.data.edit_bones[:]

#save each bone's location in a dictionary
bone_dic = {}

for bone in bones:
    bone_dic[bone.name] = (bone.head[0], bone.head[1], bone.head[2])

bpy.ops.object.mode_set(mode='OBJECT')

#place empties, set their constraints
for key, value in bone_dic.items():
    
    bpy.ops.object.empty_add(type='CUBE', radius=0.25, location=(value[0], value[1], value[2]))
    scene.objects.active.name = 'cap_{}'.format(key)
    parent = scene.objects.active
    
    bpy.ops.object.empty_add(type='SPHERE', radius=0.25, location=(value[0], value[1], value[2]))
    scene.objects.active.name = 'target_{}'.format(key)
    child = scene.objects.active
    child.show_x_ray = True

    child.select = True
    selectOBJ(parent)
    bpy.ops.object.parent_set(type='OBJECT', keep_transform=False)
    parent.constraints.new('COPY_TRANSFORMS')
    parent.constraints['Copy Transforms'].target = source_rig
    parent.constraints['Copy Transforms'].subtarget = key
    
    parent.hide = True
    
bpy.ops.object.select_all(action='DESELECT')

#set bone constraints
selectOBJ(target_rig)
pose_bones = bpy.context.active_object.pose.bones
for bone in pose_bones:
    bone.constraints.new('COPY_ROTATION')
    bone.constraints["Copy Rotation"].target = bpy.data.objects["target_{}".format(bone.name)]

    if bone.name.lower().endswith('hips') or bone.name.lower().endswith('root'):
        bone.constraints.new('COPY_LOCATION')
        bone.constraints['Copy Location'].target = bpy.data.objects["target_{}".format(bone.name)]
    
