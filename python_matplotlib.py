import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from pathlib import Path

mpl.rcParams['toolbar'] = 'None'
montserrat = Path('Montserrat-Regular.ttf')
montserrat_medium = Path('Montserrat-Medium.ttf')
montserrat_bold = Path('Montserrat-Bold.ttf')
xscale = 2560 # Pixel width from PDF
yscale = 1440 # Pixel height from PDF
fig = plt.figure(figsize=(16, 9)) # 16:9 ratio (xscale: yscale)
window_scale = 1 # TODO: Try to make this scale with window size (use for elements that do not scale automatically: font size and line sizes)
line_width = 1.5
border_color = '#e4e7f0'
line_color = '#a6a6a6'


def xy_float(x, y):
    '''X, Y from pixels to float values (0-1)'''
    x /= xscale
    y = yscale - y # Y is the wrong way around in matplotlib
    y /= yscale
    return (x, y)

def w_float(w):
    '''Width from pixels to float values (0-1)'''
    return w / xscale

def h_float(h):
    '''Height from pixels to float values (0-1)'''
    return h / yscale

def xywh_float(x, y, w, h):
    '''X, Y, width, height from pixels to float values (0-1)'''
    result = list(xy_float(x, y))
    result[1] -= h_float(h) # because Y is the wrong way around, the other side of the figure is the "Y"
    result.append(w_float(w))
    result.append(h_float(h))
    return result


def bg_block(*args):
    '''Draw background block'''
    ax = fig.add_axes(xywh_float(*args))
    ax.xaxis.set_tick_params(labelbottom=False)
    ax.yaxis.set_tick_params(labelleft=False)
    ax.spines['bottom'].set_color(border_color)
    ax.spines['top'].set_color(border_color)
    ax.spines['left'].set_color(border_color)
    ax.spines['right'].set_color(border_color)
    ax.patch.set_alpha(0.01)
    ax.set_xticks([])
    ax.set_yticks([])
    return ax


def graph(*args):
    '''Draw simple graph'''
    ax = fig.add_axes(xywh_float(*args))
    ax.xaxis.set_tick_params(labelbottom=False, length=0)
    ax.yaxis.set_tick_params(labelleft=False, length=0)
    ax.margins(x=0, y=0.05)
    return ax


def block1_graph(x, y, w, h, xvalues, yvalues, color='#000000', lines=[]):
    '''Line graph in block 1 with x values, y values, a color and a list of explicit lines'''
    ax = graph(x, y, w, h)
    ax.yaxis.set_tick_params(labelleft=True, length=0)
    ax.spines['left'].set_color(border_color)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    for l in lines:
        ax.plot(xvalues, [l for _ in xvalues], color=line_color, linewidth=2*window_scale)
    ax.set_yticks(lines)
    ax.set_yticklabels(lines, font=montserrat_bold, color=line_color)
    ax.plot(xvalues, yvalues, color=color, linewidth=3*window_scale)
    fig.add_axes(ax)
    return ax

def block2_graph(x, y, w, h, xvalues, yvalues, color='#000000', extrayvalues=[]):
    '''Line graph in block 2 with x values, y values, a color and a list of extra x/y values'''
    ax = graph(x, y, w, h)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    leftlabels = []
    rightlabels = []
    for extray in extrayvalues:
        ax.yaxis.set_tick_params(labelleft=True, length=0)
        ax.plot(xvalues, extray, color=line_color, linewidth=3*window_scale)
        leftlabels.append(int(extray.flat[0]))
        rightlabels.append(int(extray.flat[-1]))
    if (len(extrayvalues) > 0):
        ax.set_yticks(leftlabels)
        ax.set_yticklabels(leftlabels, font=montserrat_bold, color=line_color)
        twin_ax = ax.twinx()
        twin_ax.tick_params(labelright=True, length=0)
        twin_ax.set_yticks(rightlabels)
        twin_ax.set_yticklabels(rightlabels, font=montserrat_bold, color=line_color)
        twin_ax.set_ylim(ax.get_ylim())
        twin_ax.spines['left'].set_visible(False)
        twin_ax.spines['right'].set_visible(False)
        twin_ax.spines['top'].set_visible(False)
        twin_ax.spines['bottom'].set_visible(False)
    ax.plot(xvalues, yvalues, color=color, linewidth=3*window_scale)
    fig.add_axes(ax)
    return ax


def block3_graph(x, y, w, h, xvalues, yvalues, color='#000000'):
    '''Line graph in block 3 with x values, y values and a color'''
    ax = graph(x, y, w, h)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.plot(xvalues, yvalues, color=color, linewidth=2*window_scale)
    fig.add_axes(ax)
    return ax


def block1_labels(x, y, title, color='#000000', values={}):
    '''Add title and value labels to go with a graph in block 1'''
    labels = []
    labels.append(fig.text(*xy_float(x + 50, y + 70), title, fontsize=18*window_scale, font=montserrat, color=color))
    dy = 0
    for label in values:
        labels.append(fig.text(*xy_float(x + 220, y + 180 - dy), label, fontsize=12*window_scale, font=montserrat, color=color))
        labels.append(fig.text(*xy_float(x + 220, y + 240 - dy), values[label], fontsize=28*window_scale, font=montserrat_medium, color=color))
        dy += 120
    return labels


def block2_labels(x, y, title, value, color='#000000'):
    '''Add title and value labels to go with block 2 and 3'''
    labels = []
    labels.append(fig.text(*xy_float(x + 50, y + 70), title, fontsize=18*window_scale, font=montserrat, color=color))
    labels.append(fig.text(*xy_float(x + 50, y + 170), value, fontsize=40*window_scale, font=montserrat_medium, color=color))
    return labels


def block3_labels(x, y, title, color='#000000'):
    '''Add big label to go with block 3'''
    labels = []
    labels.append(fig.text(*xy_float(x + 750, y + 200), title, fontsize=80*window_scale, font=montserrat_medium, color=color, horizontalalignment='center', verticalalignment='center'))
    return labels


def button(x, y, w, h, title):
    '''Add button (just text for now)'''
    ax = bg_block(x, y, w, h)
    fig.text(*xy_float(x + (w / 2), y + h / 2 + 5), title, fontsize=28*window_scale, font=montserrat, horizontalalignment='center', verticalalignment='center')
    fig.add_axes(ax)


def draw_graphs():
    '''Draw all graphs'''

    # "Druk" graph
    x = np.linspace(0, 60, 300)
    y = (np.sin(x) + 1) * 10 + 7
    block1_graph(469, 43, 2049, 272, x, y, '#f30170', [25])
    block1_labels(43, 43, 'Druk', '#f30170', {'PEEP': 7, 'PIP': 26})

    # "Flow" graph
    x = np.linspace(0, 60, 300)
    y = np.sin(x)
    block1_graph(469, 315, 2049, 272, x, y, '#000000', [0])
    block1_labels(43, 315, 'Flow', '#000000', {'Resp': 56})

    # "Terugvolume" graph
    x = np.linspace(0, 60, 300)
    y = np.sin(x) * 2.5 + 6
    block1_graph(469, 587, 2049, 272, x, y, '#0c2074', [4, 8])
    block1_labels(43, 587, 'Terugvolume', '#0c2074', {'Vti': 11})
    
    # FiO2 / SpO2 labels
    block2_labels(43, 911, 'FiO2', '21%', '#7000ff')
    block2_labels(43, 1183, 'SpO2', '84%', '#00a5da')

    # Block 2 graph #1 (SpO2?)
    x = np.linspace(0, 20, 300)
    y = np.sqrt(x) * 10 + 40
    ymin = np.sqrt(x) * 5 + 20
    ymax = np.sqrt(x) * 15 + 60
    block2_graph(414, 911, 750, 300, x, y, '#00a5da', [ymin, ymax])

    # Block 2 graph #2 (???)
    x = np.linspace(0, 60, 300)
    y = np.sin(x)
    block2_graph(414, 1261, 750, 100, x, y, '#00a5da')

    # Pluse / Leak labels + mini graphs
    block2_labels(1307, 911, 'Pluse', '144', '#0fd208')
    block2_labels(1307, 1183, 'Leak', '18%', '#ff9900')
    x = np.linspace(0, 20, 100)
    y = np.sin(x)
    block3_graph(1557, 1011, 160, 80, x, y, '#0fd208')
    block3_graph(1557, 1283, 160, 80, x, y, '#ff9900')
    

    # Block 3 label (timer)
    block3_labels(1307, 911, '08:32')

    # Buttons (just text for now)
    button(1795, 1248, 245, 112, 'Reset')
    button(2093, 1248, 245, 112, 'Stop')

    # 3 different blocks
    bg_block(43, 43, 2475, 816)
    bg_block(43, 911, 1211, 491)
    bg_block(1307, 911, 1211, 491)


draw_graphs()
plt.get_current_fig_manager().window.state('zoomed') # Maximize window
plt.show()