import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'eq_data_1_day_m1.json'
with open(filename) as f:
    contents = json.load(f)


all_features = contents['features']
mags = []
lons = []
lats = []
hover_texts = []
for content in all_features:
    mags.append(content['properties']['mag'])
    lons.append(content['geometry']['coordinates'][0])
    lats.append(content['geometry']['coordinates'][1])
    hover_texts.append(content['properties']['title'])


# data = [Scattergeo(lon=lons, lat=lats)]

# Нанесение данных на карту.
# Настройка цвета маркеров
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'}
    }
}]

my_layout = Layout(title=contents['metadata']['title'])

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
