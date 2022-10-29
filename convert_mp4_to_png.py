import os
import subprocess
import shutil

def video_process(source_dir_path, dst_dir_path, types, img_ext, maxSize=1024):
    if not os.path.exists(dst_dir_path):
        os.makedirs(dst_dir_path)

    # check that video formats equal types 
    for file_name in os.listdir(source_dir_path):
        for type in types:
            if type not in file_name:
                continue

        name, ext = os.path.splitext(file_name)
    
        video_file_path = os.path.join(source_dir_path, file_name)

        # skip large files
        # if os.path.getsize(video_file_path) > maxSize * 1000:
        #	continue
        
        # get frames
        cmd = 'ffmpeg -i \"{}\" -qscale:v 2 \"{}/{}_%d.{}\"'.format(video_file_path, dst_dir_path, name, img_ext)

        print(cmd)
        subprocess.call(cmd, shell=True)
        print('\n')
        
# create destination folder for images
img_ext = 'png'
dst_dir_path = f'/kaggle/working/{img_ext}_from_mp4/'
os.makedirs(dst_dir_path, exist_ok=True)

# source folder with videos
source_dir_path = './'

# allowed video types 
types = ['.mp4']

# convert
video_process(source_dir_path, dst_dir_path, types, img_ext)