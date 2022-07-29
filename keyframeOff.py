Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import bpy

ob = bpy.data.objects.get("Car05_Door_Left_LOD0.004")
ob2 = bpy.data.objects.get("Car05_Door_Right_LOD0.004")


ob.animation_data_clear()
ob2.animation_data_clear()

#keyframe_delete(data_path = 'rotation_euler', 
#frame=bpy.context.scene.frame_start,)