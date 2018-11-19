import pandas as pd
import numpy as np
import matplotlib.pylab as plt

from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6

data = pd.read_excel('oclhv.xlsx',skiprows=2)
print data.head()
