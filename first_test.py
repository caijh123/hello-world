import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def plot_corr(df, size=11):
    """
    Function plots a graphical correlation matrix for each pair of columns in the dataframe.
    Input:
        df: pandas DataFrame
        size: vertical and horizontal size of the plot
    """
    corr = df.corr()
    fig, ax = plt.subplots(figsize=(size, size))
    sns.heatmap(corr, cbar=True, annot=True, square=True, fmt='.2f',
                linewidths=.5, ax=ax)
    plt.show()

def plot_hist(df, bins=50, title=None):
    """
    Function plots histogram of each numerical column in the dataframe.
    Input:
        df: pandas DataFrame
        bins: number of bins
        title: title of the histogram
    """
    df.hist(bins=bins, color='steelblue', alpha=0.7, figsize=(12, 10))
    if title:
        plt.title(title)
    plt.show()
def plot_scatter(df, x, y, size=12, title=None):
    """
    Function plots a scatter plot of x vs y
    Input:
        df: pandas DataFrame
        x: name of the column for x-axis
        y: name of the column for y-axis
        size: size of the plot
    """
    if title:
        plt.figure(figsize=(size, size))
    sns.scatterplot(x=x, y=y, data=df)
    plt.show()

def plot_categorical_columns(df, size=12):
    """
    Function plots a count plot of all categorical columns.
    Input:
        df: pandas DataFrame
        size: size of the plot
    """
    categorical = df.select_dtypes(include=['object'])
    categorical.columns
    categorical.nunique()
    categorical.drop(['id', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)
    categorical.columns
    categorical.head()
    categorical.nunique()
    plt.figure(figsize=(size, size))
