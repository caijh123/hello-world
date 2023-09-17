import pandas as pd
import numpy as np


def data(file_name):
    """
    Reads the data from the file and returns a dataframe
    :param file_name: name of the file
    :return: dataframe
    """
    df = pd.read_csv(file_name)
    return df