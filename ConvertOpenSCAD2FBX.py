import os
import bpy

currentDir = os.getcwd()

scad_directory= currentDir + r'/OpenSCAD'
stl_directory= currentDir + r'/STL'
fbx_directory= currentDir + r'/FBX'
blender_directory= currentDir + r'/Blender'
img_directory= currentDir + r'/Images'

# ----------------------------------------- Game isometric camera

if not os.path.exists(stl_directory):
    os.mkdir(stl_directory)

if not os.path.exists(fbx_directory):
    os.mkdir(fbx_directory)

if not os.path.exists(blender_directory):
    os.mkdir(blender_directory)

if not os.path.exists(img_directory):
    os.mkdir(img_directory)

for filename in os.listdir(scad_directory):
    cmd = 'openscad -o '+' '+ os.path.join(stl_directory, os.path.splitext(filename)[0] + '.stl '+ os.path.join(scad_directory, filename) )
    print(cmd)
    os.system(cmd)

scene = bpy.context.scene
scene.render.resolution_x = 512
scene.render.resolution_y = 512
scene.render.resolution_percentage = 100

f = open('Assets.md', 'w')

for filename in os.listdir(stl_directory):
    if filename.endswith(".stl"):
        bpy.ops.object.select_all(action="SELECT")
        bpy.ops.object.delete()

        filepath_stl=os.path.join(stl_directory, filename)
        print('Importing ' + filepath_stl)
        bpy.ops.import_mesh.stl(filepath=filepath_stl)

        filepath_blender=filepath=os.path.join(blender_directory,blender_directory,os.path.splitext(filename)[0] + '.blend')

        if os.path.exists(filepath_blender):
            os.remove(filepath_blender)

        filepath_fbx=os.path.join(fbx_directory, os.path.splitext(filename)[0] + '.fbx')
        fbx_filename = os.path.splitext(filename)[0] + '.fbx' +'\n'
        print('Exporting '+filepath_fbx)
        bpy.ops.export_scene.fbx(filepath=filepath_fbx)

        # Create ISO came
        bpy.ops.object.camera_add(location=(30.60861, -30.60861, 25.00000) )
        object = bpy.context.object

        object.rotation_euler = (1.047198, 0, 0.785398)  # Euler angles are (60,0,45)

        object.data.type = 'ORTHO'  # We want Iso, so set the type of the camera to orthographic
        object.data.ortho_scale = 47.523  # Let's fit the camera to our basetile in size of 10
        object.data.shift_y = 0.1
        object.name = "IsoCam"  # let's rename the cam so that it cannot be confused with other cameras.
        bpy.context.scene.camera = object

        # Setup lights
        bpy.ops.object.light_add(type='SUN', radius=1.0, align='WORLD', location=(5.0, 2.0, 16.0))

        bpy.ops.object.light_add(
            type='SPOT',
            location=(-7, -5, 16.0),
            rotation=(1.223, -0.960, 0),
        )
        lamp1 = bpy.context.active_object.data
        lamp1.name = "key Light"

        bpy.ops.wm.save_as_mainfile(filepath=filepath_blender, check_existing=False)

        bpy.context.scene.render.filepath = os.path.join(img_directory, os.path.splitext(filename)[0] + '.png')
        bpy.ops.render.render(write_still=True)

        f.write('### ' + os.path.splitext(filename)[0] + '\n')
        f.write('![alt text](https://github.com/3vilM33pl3/hexassets/blob/master/Images/'+ os.path.splitext(filename)[0] + '.png?raw=true)\n')

f.close()