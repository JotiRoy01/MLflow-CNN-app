import shutil
import imghdr
import os
import logging


import os
import tensorflow as tf


def validating_image(config:dict)->None: 
    PARENT_DIR =os.path.join(config["data"]["unzip_data_dir"],
                             config["data"]["parent_data_dir"])
    
    num_skipped = 0
    for folder_name in ("Cat","Dog"):
        folder_path = os.path.join(PARENT_DIR, folder_name)
        for fname in os.listdir(folder_path):
            fpath = os.path.join(folder_path, fname)
            try:
                fobj = open(fpath, "rb")
                is_jfif = tf.compat.as_bytes("JFIF") in fobj.peek(10)
            finally:
                fobj.close()

            if not is_jfif:
                num_skipped += 1
                # Delete corrupted image
                os.remove(fpath)

    print("Deleted %d images" % num_skipped)
                
                