# -*- coding: utf-8 -*-


import sys
from joint_feature_extractor import preprocess
from create_train_test_and_val_sets import create_test_train_val_sets
from expand_audio_files import expand_audio
from only_audio import only_audio
from only_vid_classifier import only_video
from joint_model_with_concat import joint_cat
from probe_network import probe
from joint_mlp_on_img import joint_mlp
from joint_loss_classifier import joint_loss


model = 'only_video'
if __name__ == "__main__":
    audio_dataset = "C:\\Dataset\\Audio"
    video_dataset = "C:\\Dataset\\Video"
    tmpdir = "S:\\"
    model = sys.argv[1]
    
    ## DO ALL THE PRE-PROCESSING ON THE DATA
    preprocess(audio_dataset, video_dataset, tmpdir)
    create_test_train_val_sets(tmpdir)
    expand_audio(tmpdir)
    # Train and test on the user specified version of the model
    if model == 'only_video':
        only_video(tmpdir)
    elif model == 'joint_cat':
        joint_cat(tmpdir)
    else:
        print('Invalid argument! Please try again. Refer to README for instructions on how to run')
    
    
    
    print("Complete")
