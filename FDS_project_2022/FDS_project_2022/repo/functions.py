import numpy as np # imports a fast numerical programming library
#import scipy as sp # imports stats functions, amongst other things
#import matplotlib as mpl # this actually imports matplotlib
#import matplotlib.cm as cm # allows us easy access to colormaps
#import matplotlib.pyplot as plt # sets up plotting under plt
#import pandas as pd # lets us handle data as dataframes
#from sklearn.datasets import make_classification
#import seaborn as sns
#from tqdm import tqdm

def sigmoid(x):
    '''
    Function to compute the sigmoid of a given input x.
    
    Input:
    x: it's the input data matrix. The shape is (N, H)

    Output:
    g: The sigmoid of the input x
    '''
    
    g = 1/(1+np.exp(-int(x)))

    return g