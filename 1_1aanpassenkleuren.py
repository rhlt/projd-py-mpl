import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

# Geen toolbar
mpl.rcParams['toolbar'] = 'None'

# Genereer een "figure" en teken "axes" (assen voor grafiek) en stel stijl in (onnodige informatie verborgen) 
fig = plt.figure()
ax = fig.add_axes((0, 0, 1, 1))
ax.xaxis.set_tick_params(labelbottom=False, length=0)
ax.yaxis.set_tick_params(labelleft=False, length=0)
ax.margins(x=0, y=0.05)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# Genereer wat testdata (sinusgolf) en plot die met kleur en lijndikte
xvalues = np.linspace(0, 30, 300)
yvalues = np.sin(xvalues)
ax.plot(xvalues, yvalues, color='#f30170', linewidth=3)

plt.show()
