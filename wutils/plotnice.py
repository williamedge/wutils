import numpy as np
import matplotlib.pyplot as plt

def save(fname, fig, format='png', transparent=True, dpi=300):
    fig.savefig(fname + '.' + format, format=format, transparent=transparent,\
                bbox_inches='tight', pad_inches=0, dpi=dpi)
    return fig

def saveclose(fname, fig):
    save(fname, fig)
    plt.close(fig)

def saveagu(fname, fig):
    save(fname, fig, format='jpg', transparent=False, dpi=600)

def plot_align(ax):
    x_lft = np.min([x.get_position().bounds[0] for x in ax])
    x_rgt = np.min([x.get_position().bounds[2] for x in ax])
    for xx in ax:
        xx.set_position([x_lft, xx.get_position().bounds[1], x_rgt, xx.get_position().bounds[3]])
