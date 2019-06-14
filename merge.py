import pandas as pd
from tqdm import tqdm
data_files = ['2018-02/2018-02','2018-03/2018-03','2018-04/2018-04','2018-05/2018-05','2018-06/2018-06','2018-07/2018-07','2018-08/2018-08','2018-09/2018-09','2018-10/2018-10','2018-11/2018-11','2018-12/2018-12','2019-01/2019-01']
df_list = []
for data_file in tqdm(data_files):
    df = pd.read_csv(data_file+'-tmp.csv')
    df_list.append(df[['TimeStamp','StationId','wtc_GenBeGTm_min','wtc_GenBeGTm_max','wtc_GenBeGTm_mean','wtc_GenBeRTm_min','wtc_GenBeRTm_max','wtc_GenBeRTm_mean']])

fianl_df = pd.concat(df_list)


file = open('formated.csv','w+')
file.write(fianl_df.to_csv(index=False))
file.close()
