import json
import itertools
from msilib import sequence

import array
from bokeh.models import ColumnDataSource, LabelSet, ranges
from bokeh.plotting import figure, show

json_data=open('election.json').read()
dat = sorted(json.loads(json_data), key=lambda x: x['share'], reverse=True)
data = dat[:15]
p = figure(x_range=(0, len(data)))
shareList = []
colorList = []
titleList = []
j = ' '

for i in data:
    if 'short' in i:
        titleList.append(i['short'])
    else:
        titleList.append(str(j))
        j += ' '
    shareList.append(i['share'])
    if 'color' in i:
        colorList.append(i['color'])
    else:
        colorList.append("#000000")
source = ColumnDataSource(dict(x=titleList, y=shareList))

x_label = ""
y_label = "% hlasov"
title = "Výsledky volieb."
plot = figure(plot_width=1000, plot_height=300, tools="save",
              x_axis_label=x_label,
              y_axis_label=y_label,
              title=title,
              x_minor_ticks=2,
              x_range=source.data["x"],
              y_range=ranges.Range1d(start=0, end=100))

labels = LabelSet(x='x', y='y', text='y', level='glyph',
                  x_offset=-13.5, y_offset=0, source=source, render_mode='canvas')

plot.vbar(source=source, x='x', top='y', bottom=0, width=0.35)

plot.add_layout(labels)
show(plot)
