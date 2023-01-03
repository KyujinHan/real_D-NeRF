# real_D-NeRF
Let's implement real time scene in D-NeRF

----------
# Get started
## Envrionment  
0. Not noly python=3.6, it will use any version.  
  
1. First, you must install [COLMAP](https://kyujinpy.tistory.com/27).
  
2. And, you prepare your video.mp4.  
  
----------  
# How to implement
1. Video input  
```
'./data/video/' folder
```  
  
2. Run scripts  
- In 'data_folder', folder must have 'images' folder.  
- Below, command line.  
```
$data_folder> python [your_local_path]/colmap2nerf.py --colmap_matcher exhaustive --run_colmap --aabb_scale 16
```
>> Before you already make 'json' file, you input keyword 'y'. Then, the program will implement training stage.  
>> And, you can adjust many arguments.  
   
>> My opencv2nerf's fps is 10.0. (I set this)  
----------  
# MyResult  
## Input(Video type)  
![0246](https://user-images.githubusercontent.com/98331298/209640151-129b88c0-961b-4447-aeb9-9b5c3e067097.jpg)  
  
## Result  
![images_spiral_800000_disp](https://user-images.githubusercontent.com/98331298/210346479-31cbd4f5-7a4c-432b-b6f3-0ca8c18df66d.gif)
----------  
# References
[Instant-NGP](https://github.com/NVlabs/instant-ngp)  
[How to install COLMAP](https://ikaros79.tistory.com/entry/Instant-NGP-01-Windows%EC%97%90%EC%84%9C-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0)  

