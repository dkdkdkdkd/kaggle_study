
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import random
from scipy.stats import mode
from imblearn.under_sampling import RandomUnderSampler
from tqdm import tqdm
plt.style.use("ggplot")


def data_hist(df, col, row, n):
    plt.figure(figsize=(20, 20))
    cols = df.columns
    for i in range(len(cols)):
        plt.subplot(col, row, i+1)
        plt.title(cols[i], fontsize=20)
        if len(df[cols[i]].unique()) > n:
            plt.hist(df[cols[i]], bins=20, color='b', alpha=0.7)
        else:
            temp = df[cols[i]].value_counts()
            plt.bar(temp.keys(), temp.values, width=0.5, alpha=0.7)
            plt.xticks(temp.keys())
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()
