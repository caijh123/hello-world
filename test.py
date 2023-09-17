import pandas as pd
import numpy as np


def get_data(file_path):
    """
    :param file_path: 文件路径
    :return: 返回一个dataframe
    """
    df = pd.read_csv(file_path, encoding='utf-8')
    return df
    


def data(file_name):
    """
    Reads the data from the file and returns a dataframe
    :param file_name: name of the file
    :return: dataframe
    """
    df = pd.read_csv(file_name)
    return df

