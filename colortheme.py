import matplotlib.pyplot as plt
import numpy as np

def colortheme(mode='dark'):
    if mode == 'light':
        fc = 'white'
        lc = 'black'
        pc = '#880e4f'
        bhc = '#fce4ec'
        bc = '#f8bbd0'
        rc1 = plt.cm.Blues(np.linspace(0.45, 0, 4))
        rc2 = plt.cm.Greens(np.linspace(0.45, 0, 4))    
    else:
        fc = 'black'
        lc = 'white'
        pc = '#ff5722'
        bhc ='#ff8a65'
        bc = '#ff7043'
        rc1 = plt.cm.Blues(np.linspace(1, 0.6, 4))
        rc2 = plt.cm.Greens(np.linspace(1, 0.6, 4))
    return fc, lc, pc, bhc, bc, rc1, rc2
