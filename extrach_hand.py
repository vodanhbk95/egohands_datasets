import scipy.io
import os
import numpy as np
import cv2

_LABELLED_SAMPLES = '/home/cybercore/Downloads/egohands_data/_LABELLED_SAMPLES/'
matlab_file = '/home/cybercore/Downloads/egohands_data/metadata.mat'
mat = scipy.io.loadmat(matlab_file)
number_videos = len(os.listdir(_LABELLED_SAMPLES))  #48

for video in range(number_videos):
    video_info = mat['video'][0][video] #7fields
    video_id = video_info[0].item()
    label_frames = video_info[6][0] #label of 100 frame images
    for i in range(100):
        frame_polygons = label_frames[i][0]

        frame_id = int(frame_polygons[0].item())
        my_left = label_frames[i][1]
        my_right = label_frames[i][2]
        your_left = label_frames[i][3]
        your_right = label_frames[i][4]
        
        my_left = my_left.reshape((-1,1,2))
        my_right = my_right.reshape((-1,1,2))
        your_left = your_left.reshape((-1,1,2))
        your_right = your_right.reshape((-1,1,2))
        all_pts = [my_left, my_right, your_left, your_right]
        
        file_name = 'frame_{:04d}.jpg'.format(frame_id)
        image_full_path = os.path.join(_LABELLED_SAMPLES+video_id, file_name)
        
        image = cv2.imread(image_full_path)
        mask = np.zeros(image.shape, np.uint8)
        
        for j, pts in enumerate(all_pts):
            
            if pts.size != 0:
                image_mask = np.zeros([*image.shape[:2], 4], dtype=np.uint8)
                x_min = int(np.min(pts[:, :, 0]))
                y_min = int(np.min(pts[:, :, 1]))
                x_max = int(np.max(pts[:, :, 0]))
                y_max = int(np.max(pts[:, :, 1]))
                image_mask[y_min:y_max, x_min:x_max,:3] = image[y_min:y_max, x_min:x_max]
                
                mask = np.zeros([*image.shape[:2]], dtype='uint8')
                cnt = pts[:,0].astype(int)
                cv2.drawContours(mask,[cnt],0,255,-1)

                image_mask[...,3] = mask
                cv2.imwrite(str(video_id)+ '_' + str(file_name.split('.')[0]) + '_' + f'{j}_hand.png', image_mask[y_min:y_max, x_min:x_max])
                

        
        
        
        
        
        
    
    

    
    