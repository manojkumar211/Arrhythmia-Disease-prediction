import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# Load the data:

df=pd.read_csv("C:/AI&ML Engineer/Projects/Apple/Apple Arrhythmia Prediction/Arrhythmia.csv")
df.head()
df.shape
df.tail()
df.columns
df.describe()
df.dtypes
df.duplicated().sum()
df.isnull().sum()
df.nunique()

continuous_variables=['0_pPeak','0_tPeak','0_rPeak','0_sPeak','0_qPeak','0_qrs_morph0','0_qrs_morph1','0_qrs_morph2','0_qrs_morph3','0_qrs_morph4',
                      '1_pPeak','1_tPeak','1_rPeak','1_sPeak','1_qPeak','1_qrs_morph0','1_qrs_morph1','1_qrs_morph2','1_qrs_morph3','1_qrs_morph4']
discrete_categorical=['record','type']

discrete_count=['0_pre-RR','0_post-RR','0_qrs_interval','0_pq_interval','0_qt_interval','0_st_interval','1_pre-RR','1_post-RR','1_qrs_interval',
                '1_pq_interval','1_qt_interval','1_st_interval']

df[continuous_variables].plot()
plt.title("Countinuous Variables Plot")
plt.savefig("C:/AI&ML Engineer/Projects/Apple/Apple Arrhythmia Prediction/plots/countinuous_variables.png")

df[discrete_count].plot()
plt.title("Discrete Count Variables Plot")
plt.savefig("C:/AI&ML Engineer/Projects/Apple/Apple Arrhythmia Prediction/plots/discrete_count.png")
