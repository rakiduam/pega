import numpy as np
import pandas as pd
import datetime
import math
import matplotlib.pyplot as plt
np.random.seed(19680801)

# data frame de datos aleatorios.
df_test = pd.DataFrame(index=pd.date_range(start='2020-01-01', end='2020-12-31', freq='1D'))
df_test['tx'] = [math.cos((n - 1)*math.pi/172) for n in np.arange(1, 367)]

# matplotlib
fig, ax = plt.subplots()

ax.plot(df_test['tx'])
ax.set_xlabel('x titulo')
ax.set_xlabel('x titulo')
ax.set_ylabel('y titulo')
ax.set_title('titulo grafico')
# plt.xticks([pd.DataFrame(index=pd.date_range(start='2020-01-01', end='2020-12-31', freq='15D')).to_numpy],
#            [pd.DataFrame(index=pd.date_range(start='2020-01-01', end='2020-12-31', freq='15D')).to_numpy])
plt.grid()



#varios subplots con ejes en mismas unidades
fig, ax = plt.subplots(3,2, sharex=True, sharey=True)