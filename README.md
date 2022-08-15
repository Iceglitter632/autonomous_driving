# autonomous_driving
1. create conda environment (mine is with python3.9) and execute `pip install -r requirements.txt`
1. Download data from google drive
    * file structure should be like
 ```
project
│   README.md
│   requirements.txt
│   commands.ipynb
│   h5py_split.py
│   utils.py 
└───ros-msg
│   │   CarlaEgoVehicleControl.msg
│   │   CarlaEgoVehicleStatus.msg
│      
└───train_data
│   │   dataset1.zip
│   │   dataset2.zip ...
│    
└──app-ras
│   │   calc_h5params.py
│   │   helper.py
│   │   move_files.ipynb
│   │   network.py
│   │   dataloader.py


```
3. Read data from the downloaded files from google drive via `commands.ipynb`.
    * change range of for loop at the bottom of the file to meet the names datasets
    * check pathname of input data
    * check output directory of the processed data `save_dir=<path you want to save the datas>`
    * after executing `commands.ipynb`, you will have multiple datasets in the new directory
5. execute `h5py_split.py` in terminal with `python h5py_split.py`
    * change the directory of `root` to the dataset you saved on the last command
    * `root = <pathname in save_dir>`
    * (optional) change new directory of split files, if not changed, default is `./training_data_new`

4. move data to training_folder, val_folder and testing folder. Execute following commands
    * `cd app-ras`
    * execute `move_files.ipynb`
    * could change the directories of split files with 
     ```
    for f in files[:test_size]:
        shutil.move(f'../training_data_new/{f}', '<path-you-want>')
    ```
5. calculate norms
    * calculate the min and max values of the inputs
    * make sure that line 6 of `calc_hparams.py` is your training dir you just created
    * execute `calc_hparams.py` with `python clac_hparams.py`
    * you will get a file named values.txt after you finish running the code
    * copy the values and paste them inside `helper.py`


6. execute network
    * inside `network.py` lines 296~300, there are the directories of the datas you saved from step 4
    * change hyperparameters as you like in lines 285~287
    * change the name of the model you save at line 322
