import folium

map = folium.Map(location=[37.49790265303061, 127.02760683861852],
           zoom_start=17)
map.save("./강남역.html")