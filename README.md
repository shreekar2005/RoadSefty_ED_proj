# RoadSefty_ED_proj
WE had ED (engineering design) course
for that we have made this project

Aim : To detect cars at blind spots and alert others (other side of blind spot) that some vehical is comming from other side. This will decrese rate of accidents at blind spots (mainly in sharp terns, Ghats, underbridge crossing etc)

# Run this command to run the app

python detect_count_and_track.py --weights yolov7-tiny.pt --conf 0.55 --source traffic.mp4 --view-img --nosave --no-trace --device 0

python runforcamTOP.py --weights yolov7-tiny.pt --conf 0.55 --source EDVIDTOPVIEW.mp4 --view-img --nosave --no-trace --device 0

python runforcamTOPwithpico.py --weights yolov7-tiny.pt --conf 0.55 --source EDVIDTOPVIEW.mp4 --view-img --nosave --no-trace --device 0

python runforcamSIDE.py --weights yolov7-tiny.pt --conf 0.55 --source EDVIDSIDEVIEW.mp4 --view-img --nosave --no-trace --device 0

python runforcamSIDEwithpico.py --weights yolov7-tiny.pt --conf 0.55 --source EDVIDSIDEVIEW.mp4 --view-img --nosave --no-trace --device 0

python runfor_iriuncam.py --weights yolov7-tiny.pt --conf 0.55 --source 0 --view-img --nosave --no-trace --device 0

# Demos 

demo for how our hardware works :

demo for testing model in real world :
