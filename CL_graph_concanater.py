import pandas as pd
import matplotlib.pylab as plt
import numpy as np
plt.style.use('bmh')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/emrec/Downloads/wandb_export_2023-06-02T18_12_40.119-04_00.csv')

arr_s = df['10Small(70-20-10) - val/box_loss'].values[~np.isnan(df['10Small(70-20-10) - val/box_loss'].values)]
arr_m = df['20medium(70-20-10) - val/box_loss'].values[~np.isnan(df['20medium(70-20-10) - val/box_loss'].values)]
arr_l = df['70Large(70-20-10) - val/box_loss'].values[~np.isnan(df['70Large(70-20-10) - val/box_loss'].values)]
perfs = np.concatenate((arr_l, arr_m, arr_s))
plt.figure(dpi=200)
plt.plot(range(len(arr_l)), arr_l, 'r', label='Large')
plt.plot(range(len(arr_l), len(arr_l)+len(arr_m)), arr_m, 'b', label='Medium')
plt.plot(range(len(arr_l)+len(arr_m), len(arr_l)+len(arr_m)+len(arr_s)), arr_s, 'k', label='Small')
plt.legend()
plt.xlabel('epoch')
plt.ylabel('val/box_loss')


# Display the plot
plt.show()

