import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import pandas as pd
import patsy

import itertools as it
import collections as co
import functools as ft
import os.path as osp

import glob
import textwrap

import warnings
warnings.filterwarnings("ignore")
def warn(*arg, **kwargs): pass
warnings.warn = warn

np.set_printoptions(precision=4,
                    suppress=True)
pd.options.display.float_format = '{:20,.4f}'.format
np.random.seed(42)
mpl.rcParams['figure.figsize'] = [4.0, 3.0]

markers = it.cycle(['+', '^', 'o', '_', '*', 'd', 'x', 's'])

from IPython.display import Image, display

from sklearn import (cluster,
                     datasets,
                     decomposition,
                     discriminant_analysis,
                     dummy,
                     ensemble,
                     feature_selection as ftr_sel,
                     linear_model,
                     metrics,
                     model_selection as skms,
                     multiclass as skmulti,
                     naive_bayes,
                     neighbors,
                     pipeline,
                     preprocessing as skpre,
                     svm,
                     tree)

