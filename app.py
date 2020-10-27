#app.py

import pandas as pd
import folium

corona_map = folium.Map(location=[14.4974,-14.4524], zoom_start=2)
confirmed_stats = pd.read_csv('Blog_corona.csv')
for column, row in confirmed_stats.iterrows():
    _, country, latitude, longitude, confirmed = row
    popup_text = country + '\n' + str(confirmed) + ' cases'
    folium.CircleMarker(location=[latitude,longitude], radius=10, popup=popup_text, color='#3186cc', fill=True, fill_color='#3186cc').add_to(corona_map)

corona_map.save('co-viz.html')
