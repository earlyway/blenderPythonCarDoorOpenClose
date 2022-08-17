Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import bpy

counter=0
loc=0

def run_10_times():
    global loc  #전역함수 global. loc 를 def로 불러와서 변수를 변경하겠다.
    global counter
    bpy.ops.mesh.primitive_cube_add(location=(0,loc,0)) #큐브 원형을 생성함((0,loc,0) 의 위치에)
    counter+=1
    loc+=2
    if counter==20:  #counter += 1 인데 20까지 run_10_times 함수를 반복. 20이 되면 None을 리턴하며 함수종료.
        return None
    return 0.05


def unreg():
    if bpy.app.timers.is_registered(run_10_times): #run_10_times 함수가 register 된것이 True라면
        print("unregg")		#system console 에 print.
    else:
        print("no need unreg")
    return None

bpy.app.timers.register(run_10_times, first_interval=0) #스크립트를 실행하고 0초 후 run_10_times함수를 register
bpy.app.timers.register(unreg, first_interval=1.0)      #스크립트를 실행하고 1초 후 unreg함수를 register


#system console -> 'unregg' output.
#unreg의 register 가 1초후 가 아닌 10초 후 register라면 system console창에 "no need unreg"가 출력될것임.
