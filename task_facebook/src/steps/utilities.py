import time
from os.path import dirname

import yaml
import logging

ROOT_DIR = dirname(dirname(dirname(__file__)))


def get_timestamp():
    return time.strftime("%Y%m%d-%H%M%S")


def create_logger(file=""):
    """creates log file with time stamp filename under log directory"""
    filepath = time.strftime("%Y%m%d")
    filepath = f"{ROOT_DIR}/logs/{file}{filepath}.log"
    logging.basicConfig(filename=filepath,
                        level=logging.INFO,
                        format='%(levelname)s %(asctime)s - %(message)s',
                        filemode='a')
    return logging.getLogger()


def yaml_loader(filepath):
    """Loads a yaml file"""
    with open(filepath, 'r') as file_descriptor:
        data = yaml.load(file_descriptor)
    return data


def yaml_dump(filepath, data):
    """Dumps data to a yaml file"""
    with open(filepath, 'w') as file_descriptor:
        yaml.dump(data, file_descriptor)
