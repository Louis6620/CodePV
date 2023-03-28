import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import stats
from datetime import datetime
dateparse = lambda x: datetime.strptime(x, '%m/%d/%Y %H:%M')
import plotly.express as px
import plotly.graph_objects as go
df = pd.read_csv('D:/OneDrive - Hanoi University of Science and Technology/Me/Code/DatainHUST/CodePV/t5inverter1.csv',
                encoding="utf-8-sig",
                header=0,
                infer_datetime_format=True,
                parse_dates={'datetime':[0]},##lấy thời gian từ cột [0]##
                index_col=['datetime']
                )
df.head()
df.describe()