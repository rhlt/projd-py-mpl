import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from pathlib import Path

# Geen toolbar
mpl.rcParams['toolbar'] = 'None'

# Lettertype inladen uit bestand
montserrat_bold = Path('Montserrat-Bold.ttf')

# Genereer een "figure" en teken "axes" (assen voor grafiek) en stel stijl in (onnodige informatie verborgen) 
fig = plt.figure()
ax = fig.add_axes((0.1, 0, 1, 1)) # Links wat ruimte voor label
ax.xaxis.set_tick_params(labelbottom=False, length=0)
ax.yaxis.set_tick_params(labelleft=False, length=0)
ax.margins(x=0, y=0.05)
ax.spines['left'].set_color('#e4e7f0') # Dunne rand links
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# Genereer wat testdata (sinusgolf) en plot die met kleur en lijndikte
xvalues = np.linspace(0, 30, 300)
yvalues = (np.sin(xvalues) + 1) * 10 + 7 # Aangepast aan referentielijn
ax.plot(xvalues, yvalues, color='#f30170', linewidth=3)

# Genereer data van referentielijn en labels 
ax.plot(xvalues, [25 for _ in xvalues], color='#a6a6a6', linewidth=2) # Y waarde overal 25
ax.yaxis.set_tick_params(labelleft=True, length=0) # Links wel label
ax.set_yticks([25]) # Streepje bij positie 25
ax.set_yticklabels([25], font=montserrat_bold, color='#a6a6a6') # Label bij dat streepje op positie 25

plt.show()
