# build a machine learning model to predict the average price of a house in Boston

# import the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_errorOps
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler


# load the data
train_df = pd.read_csv("train.csv")
test_df = pd.read_csv("test.csv")
train_df.head()
train_df.info()
train_df.describe()       
train_df.columns
train_df.shape()
train_df.isnull().sum()
train_df.isnull().sum()
train_df.isnull().sum()
train_df.isnull().sum()






