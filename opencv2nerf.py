# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 23:45:27 2022

@author: kyujin Han
- Make video to frame
- add resize
- choose remove background?? (accurate not 100%; https://github.com/danielgatis/rembg)
"""

'''
1. Import Module
'''
import cv2
import os
from rembg import remove
from PIL import Image


def video2nerf(seg):
    '''
    2. Video
    '''
    os.makedirs('./images', exist_ok=True)
    default_path = "./video/"
    img_path = "./images"
    #default_path = "./data/video/"
    #img_path = "./data/images"
    
    video_name = os.listdir(default_path)[0]
    vid = cv2.VideoCapture(default_path + video_name)
    fps = vid.get(cv2.CAP_PROP_FPS) #fps 추출
    print("fps:",fps) # 24.0
    
    
    '''
    3. Make video to frame
    '''
    count = 0
    
    while(vid.isOpened()):
        ret, image = vid.read()
        #print(vid.get(1))
        
        try:
            # make fps 30.0 -> 15.0
            if (count % 2 == 0): 
                # resize 800x800
                image = cv2.resize(image, (800, 800), interpolation=cv2.INTER_AREA)
                
                # remove background
                if seg == 'y':
                    image = remove(image)
                    
                # save
                cv2.imwrite(img_path + "/%04d.jpg" % count, image)
                
                #print('Saved frame number :', str(int(vid.get(1))))
                #count += 1   
            
        except:
            print("Video to frame // Done")
            break
        
        count += 1
    vid.release()
    
    
    '''
    4. Make 100 frame
    - Limitations 3s (~fps 30일 때 90 frames)
    '''
    '''
    frames_num = int(fps*3.) # if fps: 30 -> 90 frames
    half = frames_num//2 # 45
    
    img_len = int(len(os.listdir(img_path)))
    if img_len > frames_num:
        mid = img_len//2
        lower = mid - half
        upper = mid + half
        
        for img2 in os.listdir(img_path)[upper:]:
            os.remove(img_path+"/"+img2)
        
        for img1 in os.listdir(img_path)[0:lower]:
            os.remove(img_path+"/"+img1)
    '''
    print("Imges frames:", len(os.listdir(img_path)))
    

if __name__ == "__main__":
    video2nerf('n')