# Geospatial Data Analysis with GeoPandas and Shapely  

## Project Overview  
This project focuses on analyzing geospatial data using **GeoPandas**, **Shapely**, and **Folium**. It involves reading and visualizing shapefiles (`.shp`) and GeoJSON files, extracting specific district data, working with geometries, and exploring web mapping.  

## Features  
✔ Read and analyze municipality boundary data from **Shapefile** and **GeoJSON**  
✔ Plot municipality boundaries and color maps based on attributes  
✔ Filter and visualize specific districts (e.g., Rupandehi)  
✔ Work with geometric objects (**Point, LineString, Polygon**)  
✔ Perform geometric operations like `contains()`, `within()`, and `overlaps()`  
✔ Use **Folium** for interactive web mapping  

## Requirements  
Install the required Python libraries before running the code:  

```bash
pip install geopandas shapely folium mapclassify matplotlib
Usage
1️⃣ Read and Display Geospatial Data
python
Copy
Edit
import geopandas as gpd

file_path = r"C:\Users\admin\Desktop\Projects\Data Pipelines\Data\municipality.shp"
municipality = gpd.read_file(file_path)
print(municipality.head())
2️⃣ Plot Municipality Boundaries
python
Copy
Edit
import matplotlib.pyplot as plt

municipality.plot()
plt.show()
3️⃣ Filter a Specific District
python
Copy
Edit
rupandehi = municipality[municipality['DISTRICT'] == 'RUPANDEHI']
rupandehi.plot()
4️⃣ Work with Geometries in Shapely
python
Copy
Edit
from shapely.geometry import Point, LineString, Polygon

point = Point(85.324, 27.717)  # Example: Kathmandu
line = LineString([(85.324, 27.717), (85.330, 27.720), (85.340, 27.730)])
polygon = Polygon([(85.324, 27.717), (85.330, 27.720), (85.340, 27.730), (85.324, 27.717)])

print(polygon.contains(point))  # Check if the point is within the polygon
5️⃣ Web Mapping with Folium
python
Copy
Edit
import folium

m = rupandehi.explore(column="PALIKA")
m.save("rupandehi_map.html")
Results
Static maps using Matplotlib
Interactive web maps using Folium
Geometric computations using Shapely
Author
👤 Festus Mutie

License
This project is open-source and can be used freely.

🔹 Future Improvements: Add spatial analysis, clustering, and web-based dashboards.








# MAP-VISUALIZATION-USING-GEOPANDAS-AND-FOLIUM
