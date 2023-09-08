import pandas as pd
import matplotlib.pylab as plt
import numpy as np
plt.style.use('bmh')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/emrec/Downloads/wandb_export_2023-06-30T09_03_17.604-04_00.csv')

arr_s = df['VR Small 50epoch - metrics/mAP_0.5:0.95'].values[~np.isnan(df['VR Small 50epoch - metrics/mAP_0.5:0.95'].values)]
arr_m = df['VR Med 35 epoch - metrics/mAP_0.5:0.95'].values[~np.isnan(df['VR Med 35 epoch - metrics/mAP_0.5:0.95'].values)]
arr_l = df['VR Large 15 epoch - metrics/mAP_0.5:0.95'].values[~np.isnan(df['VR Large 15 epoch - metrics/mAP_0.5:0.95'].values)]
arr_ncl = df['vr_nocl100 - metrics/mAP_0.5:0.95'].values[~np.isnan(df['vr_nocl100 - metrics/mAP_0.5:0.95'].values)]
perfs = np.concatenate((arr_l, arr_m, arr_s))
plt.figure(dpi=200)
plt.plot(range(len(arr_l)), arr_l, 'r', label='Large')
plt.plot(range(len(arr_l), len(arr_l)+len(arr_m)), arr_m, 'b', label='Medium')
plt.plot(range(len(arr_l)+len(arr_m), len(arr_l)+len(arr_m)+len(arr_s)), arr_s, 'k', label='Small')
plt.plot(range(len(arr_ncl)), arr_ncl, 'g--', label='No CL')  # 'g--' will make the line green and dashed.
plt.legend()
plt.xlabel('epoch')
plt.ylabel('mAP_0.5:0.95')


# Display the plot
plt.show()
