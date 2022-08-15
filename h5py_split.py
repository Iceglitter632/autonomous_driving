# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 22:58:34 2022

@author: Jerry
"""

import os
import h5py
import numpy as np
from pathlib import Path


root = './train_data'
topfiles = os.listdir(root)
pathname = './training_data_new'
Path(pathname).mkdir(parents=True, exist_ok=True)
for tf in topfiles:
    second_level = os.path.join(root, tf)
    print(f'this is folder {tf}')
    files = os.listdir(second_level)
    for file in files:
        print(f'   this is file {file}')
        third_level = os.path.join(second_level, file)
        f = h5py.File(third_level, 'r')
        keys = list(f.keys())
        keys.remove('depth_front')
        keys.remove('rgb_front')
        
        if 'others' in f.keys():
            size = f['others'].shape[0]
        else:
            s1 = f['imu'].shape[0]
            s2 = f['speedometer'].shape[0]
            s3 = f['labels'].shape[0]
            s4 = f['command'].shape[0]
            size = min([s1, s2, s3, s4])
        try:
            for i in range(size):
                d = {}
                temp = f'{i}_{tf}_{file}'
                new_filename = os.path.join(pathname, temp)
                if os.path.exists(new_filename):
                    continue
                d['rgb_front/image'] = f['rgb_front/image'][i]
                d['depth_front/image'] = f['depth_front/image'][i]
                if 'others' in f.keys():
                    d['others'] = f['others'][i]
                else:
                    t1 = f['imu'][i]
                    t2 = f['speedometer'][i]
                    t2 = np.array(t2)
                    t2 = np.expand_dims(t2, axis=0)
                    t3 = f['command'][i]
                    t3 = np.array(t3)
                    t3 = np.expand_dims(t3, axis=0)
                    t4 = f['labels'][i]
                    
                    arr = np.concatenate([t1, t2, t3, t4], axis=0)
                    
                    d['others'] = arr
                with h5py.File(new_filename, "w") as new_file:
                    for k, v in d.items():
                        new_file.create_dataset(k, data=np.array(v), compression='gzip')
        except:
            print(f'error in file {file}')
        f.close()
            