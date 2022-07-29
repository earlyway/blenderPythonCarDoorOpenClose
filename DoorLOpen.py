Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import bpy
import math
    
def main():
    bpy.ops.screen.frame_jump(end = False)
    doorL = bpy.data.objects.get("Car05_Door_Left_LOD0.004")
    
    doorL.rotation_euler = [math.radians(90), 0, math.radians(0)]
    doorL.keyframe_insert(data_path = 'rotation_euler', frame = 0)
    
    doorL.rotation_euler = [math.radians(90), 0, math.radians(-80)]
    doorL.keyframe_insert(data_path = 'rotation_euler', frame = 30)
    
def stop_playback(scene):
    if scene.frame_current == 30:
        bpy.ops.screen.animation_cancel(restore_frame=False)
    
def keyframeRemove():
    ob = bpy.data.objects.get("Car05_Door_Left_LOD0.004")
    if scene.frame_current == 30:
        ob.animation_data_clear()
        
def aa():
    if bpy.app.timers.is_registered(stop_playback):
        return None
    else :
        bpy.app.timers.unregistered(keyframeRemove)

main()
bpy.ops.screen.animation_play()
bpy.app.handlers.frame_change_pre.append(stop_playback)
bpy.app.timers.register(aa, first_interval = 2.0)

