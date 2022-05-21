import csv

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

from plotly.graph_objs import Layout
import plotly.graph_objs as go
import plotly.express as px

from datetime import datetime


filename = 'MODIS_C6_1_Global_7d.csv'
with open(filename) as f:
    reader = csv.reader(f)
    reader_row = next(reader)

    contents = []
    lons = []
    lats = []
    for row in reader:
        content = float(row[3])
        lat = float(row[0])
        lon = float(row[1])

        contents.append(content)
        lats.append(lat)
        lons.append(lon)

example1 = contents[:5]

data = [Scattergeo(lon=lons, lat=lats)]
fig = {'data': data}
offline.plot(data, filename='global_fires.html')







# data = [{
#     'type': 'scattergeo',
#     'longitude': lon,
#     'latitude': lat,
#     'brightness': brig
# }]
#
#
# my_layout = Layout(title=content[3])
#
# fig = go.Figure(go.Scattergeo())
#
# fig.update_geos(
#     resolution=110,
#     showcoastlines=True, coastlinecolor='RebeccaPurple',
#     showland=True, landcolor='LightGreen',
#     showocean=True, oceancolor='LightBlue',
#     showlakes=True, lakecolor='Blue',
#     showrivers=True, rivercolor='Blue'
# )
# fig = {'data': data, 'layout': my_layout}
#
# fig.update_layout(height=300, margin={'r': 0,
#                                       't': 0,
#                                       'l': 0,
#                                       'b': 0
#                                       })
# fig.write_html('global_fires.html')
#
# # df = px.data.gapminder().query('year == 2017')
# # fig = px.scatter_geo(df, locations='iso_alpha',
# #                       size='pop')
# fig.show()
#
#
# # offline.plot(fig, filename='global_fires.html')



