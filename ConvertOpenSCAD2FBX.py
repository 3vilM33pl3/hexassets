import os
import bpy

scad_directory= r'/home/olivier/Projects/Narrowboat/hexassets/OpenSCAD'
stl_directory= r'/home/olivier/Projects/Narrowboat/hexassets/STL'
fbx_directory= r'/home/olivier/Projects/Narrowboat/hexassets/FBX'
blender_directory=r'/home/olivier/Projects/Narrowboat/hexassets/Blender'

if not os.path.exists(stl_directory):
    os.mkdir(stl_directory)

if not os.path.exists(fbx_directory):
    os.mkdir(fbx_directory)

if not os.path.exists(blender_directory):
    os.mkdir(blender_directory)


for filename in os.listdir(scad_directory):
    cmd = 'openscad -o '+' '+ os.path.join(stl_directory, os.path.splitext(filename)[0] + '.stl '+ os.path.join(scad_directory, filename) )
    print(cmd)
    os.system(cmd)

bpy.app.debug_wm=True
bpy.ops.mesh.primitive_ico_sphere_add(location=(0, 0, 0))

for filename in os.listdir(stl_directory):
    if filename.endswith(".stl"):
        bpy.ops.object.select_all()
        bpy.ops.object.delete()

        filepath_stl=os.path.join(stl_directory, filename)
        print('Importing ' + filepath_stl)
        bpy.ops.import_mesh.stl(filepath=filepath_stl)

        filepath_blender=filepath=os.path.join(blender_directory,blender_directory,os.path.splitext(filename)[0] + '.blend')

        if os.path.exists(filepath_blender):
            os.remove(filepath_blender)

        print('Saving '+filepath_blender)
        bpy.ops.wm.save_as_mainfile(filepath=filepath_blender, check_existing=False)
        if bpy.data.is_saved:
            print('data saved')
        else:
            print('data NOT saved')

        filepath_fbx=os.path.join(fbx_directory, os.path.splitext(filename)[0] + '.fbx')
        fbx_filename = os.path.splitext(filename)[0] + '.fbx' +'\n'
        print('Exporting '+filepath_fbx)
        bpy.ops.export_scene.fbx(filepath=filepath_fbx)

        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete()

