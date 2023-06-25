import mlflow
import argparse
import os
import shutil
from tqdm import tqdm
import logging

import random


STAGE = "MAIN" ## <<< change stage name 

logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )


def main():
    with mlflow.start_run() as run :
        mlflow.run(".","get_data",env_manager="local")
        mlflow.run(".","base_model_creation",env_manager="local")
        mlflow.run(".","training",env_manager="local")



if __name__ == '__main__':
    
    try:
        logging.info("\n********************")
        logging.info(f">>>>> stage {STAGE} started <<<<<")
        main()
        logging.info(f">>>>> stage {STAGE} completed!<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e
