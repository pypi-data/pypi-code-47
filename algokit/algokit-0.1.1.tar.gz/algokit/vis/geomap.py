import folium
import webbrowser as web


def show_polyline(points, width=15, color='#8EE9FF'):
    m = folium.Map(zoom_start=8, control_scale=True)
    the_line = folium.PolyLine(points, width, color).add_to(m)
    m.save("tmp.html")
    web.open("tmp.html")


if __name__ == '__main__':
    m = folium.Map(location=[0.5, 100.5], zoom_start=8, control_scale=True)
    m.save("tmp.html")
    web.open("tmp.html")