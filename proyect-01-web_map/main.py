import folium
import pandas


#definimos la coordenadas del lugar que queremos mostrar cuando se abra la aplicación en el navegador
mapa_jujuy = [-23.17, -65.79]
#obtenemos algunos datos de nuestro archivo csv
datos_jujuy = pandas.read_csv("../resources/Investigación.csv")
nombres_picos = datos_jujuy["Nombre del Pico"]
altitudes = datos_jujuy["Altitud (m)"]
latitudes = datos_jujuy["Latitud"]
longitudes = datos_jujuy["Longitud"]
descripciones = datos_jujuy["Descripción para el Popup"]

#creamos el objeto principal de folium
mapa = folium.Map(location=mapa_jujuy, zoom_start=8, tiles="OpenStreetMap")

#agregamos elementos/objects al mapa definido
for nm, al, lt, ln, dsc in zip(nombres_picos, altitudes, latitudes, longitudes, descripciones):
    mapa.add_child(folium.Marker(location=(lt,ln), popup=f"{nm} + {al}", icon=folium.Icon(color="green")))

mapa.save("Map1.html")