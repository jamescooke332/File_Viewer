from tkinter import *
from turtle import left
import geopandas as gpd
from tkinter import filedialog
from shapely.geometry import Point
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import folium
from folium.plugins import MarkerCluster


root = Tk()
blank_space = " "
root.title(50* blank_space + "Data Viewer")
root.resizable(width=FALSE, height = FALSE)
root.geometry("438x5573+460+40")

# create a canvas widget to display the map
# create a canvas widget to display the map
map_frame = Frame(root)
map_frame.pack(side=BOTTOM, fill=BOTH, expand=1)

global gdf
gdf=None 

def import_file():
    #define global gdf
    global gdf
    #make open file function 
    file_path = filedialog.askopenfilename()
    #create geodataframe
    gdf = gpd.read_file(file_path)
     # create figure and axes
    fig, ax = plt.subplots(figsize=(5,5))
    # plot the geodataframe
    gdf.plot(ax=ax)
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side="left", fill=BOTH, expand=1)


      # create map centered on the first point in the geodataframe
    map_center = gdf.geometry.centroid.iloc[0].coords[0][::-1]
    my_map = folium.Map(location=map_center, zoom_start=10)

    
def unload():
    global gdf
    if gdf is not None:
        del gdf
    


def export_file():
    global gdf
    file_path = filedialog.asksaveasfilename(defaultextension=".shp")
    # do something to create the geodataframe to export
    gdf.to_file(file_path)

button1 = Button(root, text="Import",  width=10, height=3, font=("Helvetica", 12), bg="lightblue", command=import_file)
button1.pack()

button2 = Button(root, text="Export", command=export_file)
button2.pack()

button3 = Button(root, text="Unload", command=unload)
button3.pack()

root.mainloop()





