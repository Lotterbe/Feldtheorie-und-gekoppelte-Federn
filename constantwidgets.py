import ipywidgets as widgets
from IPython.display import clear_output

kslider=widgets.FloatSlider(
    min=0, max=100, step=0.1, value=1, description='Federkonstante k', readout_format='.1f',
    style={'description_width': 'initial'}, layout=widgets.Layout(width='80%'))

Kslider=widgets.FloatSlider(
    min=0, max=10, step=0.01, value=1, description='Federkonstante K', readout_format='.2f',
    style={'description_width': 'initial'}, layout=widgets.Layout(width='80%'))

mslider=widgets.FloatSlider(
    min=0, max=50, step=0.5, value=1, description='Masse m', readout_format='.1f',
    style={'description_width': 'initial'}, layout=widgets.Layout(width='80%'))

dts=widgets.FloatSlider(
    min=0.005, max=1, step=0.005, value=0.01, description='Zeitschritt dt', readout_format='.3f',
    style={'description_width': 'initial'}, layout=widgets.Layout(width='80%'), disabled=False)

tnumber=widgets.IntSlider(
    min=100, max=100000, step=100, value=10000, description='Gesamtzahl der berechneten Zeitschritte NT',
    style={'description_width': 'initial'}, layout=widgets.Layout(width='80%'))

times=widgets.FloatSlider(
    min=10*dts.value, max=(tnumber.max+1)*dts.value, step=1, value=tnumber.value*dts.value, description='Gesamtzeit T', readout_format='.2f',
    style={'description_width': 'initial'}, layout=widgets.Layout(width='80%'), disabled=True)

def timeslider(x, y):
    T = tnumber.value  * x
    times.value = T
    times.max = round((tnumber.max +1) *x,2)

widgets.interactive(timeslider, x=dts, y=times);

tsaving=widgets.Dropdown(options=[('10', 1), ('20', 2), ('50', 3), ('100', 4)], description='Nach wie vielen Zeitschritten gespeichert werden soll (tsave)',
    style={'description_width': 'initial'}, layout=widgets.Layout(width='60%'))

nof=widgets.Dropdown(options= [('10', 1), ('5', 2), ('2', 3), ('1', 4)], description='Zahl der gespeicherten Bilder',
    style={'description_width': 'initial'}, layout=widgets.Layout(width='60%'))

def totaltimeslider(y):
    T = y*dts.value
    times.value = T
    NT = y
    datalistl = []
    datalistr = []
    datalist2l = []
    datalist2r = []
    divisor = [1, 2, 3, 4, 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 250, 300, 400, 500]
    for m in divisor:
        if NT%m == 0:
            if str(m) not in (datalistl and datalistr):
                datalistl.append(str(m))
                datalist2l.append(str(int(NT/m)))
    datalist = datalistl + datalistr
    datalist2 = datalist2l + datalist2r
    tsaving.options = tuple(zip(datalist, range(1, len(datalist)+1)))
    nof.options = tuple(zip(datalist2, range(1, len(datalist2)+1)))
    tsaving.value = datalist.index('10') + 1

w = widgets.link(
    (dts, 'value'),
    (times, 'min')
)

z = widgets.link(
    (tsaving, 'value'),
    (nof, 'value')
)

widgets.interact(totaltimeslider, y=tnumber);

data = widgets.Dropdown(options=[('Auslenkung', 1), ('Energie (normiert)', 2)], description='Daten zum Plotten:',
    style={'description_width': 'initial'}, layout=widgets.Layout(width='60%'))

start = widgets.Dropdown(options=[('Nach rechts laufender schmaler Puls', 1), ('Nach rechts laufender breiter Puls', 2),
('Dreiecksauslenkung ohne Anfangsgeschwindigkeit', 3)], description='Startwerte für die Auslenkung und Geschwindigkeit',
    style={'description_width': 'initial'}, layout=widgets.Layout(width='60%'))

file = widgets.Text(
    value='seilwelle',
    placeholder='Type something',
    description='Videoname:',
    disabled=False
)

#widgets.interact(plotting, f=start);

# otherwise the slider will also appear when loading the module for the first time
clear_output()
