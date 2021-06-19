import numpy as np
from numba import jit
import matplotlib.pyplot as plt

@jit(nopython=True)
def start_triangle(massnumber):
    n = massnumber
    s = np.zeros(n, np.float64)
    v = np.zeros(n, np.float64)

    s[101:151]=0.25*np.arange(0,50)
    s[151:201]=0.25*np.arange(50,0,-1)
    #v[101:151]= -0.25*np.ones(50)
    #v[151:201]= +0.25*np.ones(50)

    return s, v

@jit(nopython=True)
def start_pulse(massnumber, mass, coupling, wavelength):
    n = massnumber
    #period = n/realwl
    if int(coupling) == 0:
        massquad = 0
    else:
        massquad = mass/coupling
    wl = wavelength
    s = np.zeros(n, dtype=np.float64)
    v = np.zeros(n, dtype=np.float64)
    x = np.arange(1, n+1, dtype=np.int64)
    mid = int(n/2) - int(wl/2)

    s[mid:int(wl)+mid] = 1-np.cos(2*np.pi*x[0:int(wl)]/wl)
    v[mid:int(wl)+mid] = -np.sqrt((2*np.pi/wl)**2 + massquad)* np.sin(2*np.pi/wl*x[0:int(wl)])

    return s, v




def plottingsv(t1, t2, t3, L, dx):

    fig, axs = plt.subplots(2, 2, constrained_layout=True, figsize=(9, 5))

    axs[0, 0].plot(np.arange(0, L, dx), t1[0], label='Auslenkung')
    axs[0, 0].plot(np.arange(0, L, dx), t1[1], label='Geschwindigkeit')
    axs[0, 0].legend()
    axs[0, 0].set_title('Nach rechts laufender schmaler Puls', fontsize=10)

    axs[0, 1].plot(np.arange(0, L, dx), t2[0], label='Auslenkung')
    axs[0, 1].plot(np.arange(0, L, dx), t2[1], label='Geschwindigkeit')
    axs[0, 1].legend()
    axs[0, 1].set_title('Nach rechts laufender breiter Puls', fontsize=10)

    axs[1, 0].plot(np.arange(0, L, dx), t3[0], label='Auslenkung')
    axs[1, 0].plot(np.arange(0, L, dx), t3[0], label='Geschwindigkeit')
    axs[1, 0].legend()
    axs[1, 0].set_title('Dreiecksauslenkung ohne Anfangsgeschwindigkeit', fontsize=10)

    axs[1, 1].remove()

    return fig, axs

def plottingsande(s, E, nof, tsave, dt, L, dx):

    fig, axs = plt.subplots(2, 1, constrained_layout=True, figsize=(9, 5))
    fig.suptitle('Vergleich der Auslenkung und Energie (normiert) zu zwei Zeitpunkten', fontsize=15)

    axs[0].plot(np.arange(0, L, dx), s[0], label='Auslenkung')
    axs[0].plot(np.arange(0, L, dx), E[0], label='Energie (normiert)')
    axs[0].legend()
    axs[0].set_title('Startwerte (t=0)', fontsize=10)

    timestep = int(nof/2) + 1
    axs[1].plot(np.arange(0, L, dx), s[timestep], label='Auslenkung')
    axs[1].plot(np.arange(0, L, dx), E[timestep], label='Energie (normiert)')
    axs[1].legend()
    axs[1].set_title(label='Nach ca. der Hälfte an Zeitschritten (t=%.2f)' %(timestep * tsave * dt + dt), fontsize=10)


    return fig, axs
