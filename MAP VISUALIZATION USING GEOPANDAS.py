#!/usr/bin/env python
# coding: utf-8

# In[42]:


import geopandas as gpd
import matplotlib.pyplot as plt


# In[43]:


# Define the file path
file_path = r"C:\Users\admin\Desktop\Projects\Data Pipelines\Data\municipality.shp"  # Replace with the correct file extension

# Read the geospatial file
municipality = gpd.read_file(file_path)

# Display the first few rows
print(municipality.head())


# In[44]:


# Define the file path
file_path = r"C:\Users\admin\Desktop\Projects\Data Pipelines\Data\municipality.geojson"

# Read the GeoJSON file
municipality_geojson = gpd.read_file(file_path)

# Display the first few rows
print(municipality_geojson.head())


# In[45]:


len(municipality)#we have 775 municipalities


# In[46]:


municipality.geom_type


# In[47]:


municipality.shape


# In[48]:


municipality.crs


# In[49]:


municipality.plot()


# In[50]:


municipality.boundary.plot()# show only the boundary of the map


# In[51]:


municipality.plot('PR_NAME',cmap='magma', legend=True)# coloring the map according to province name, and user color parameter as magma


# In[52]:


ax=municipality.plot('PR_NAME',cmap='magma',figsize=(15,15))
ax.set_axis_off()# plot the map without the boundary


# In[54]:


rupandehi = municipality[municipality['DISTRICT'] == 'RUPANDEHI']
rupandehi.plot()
#show only the selected district


# In[55]:


len(rupandehi)


# In[56]:


rupandehi.head()


# In[58]:


rupandehi.plot('PALIKA',cmap='magma')


# In[ ]:


#working with geometry in python-contains,touches,overlap


# In[67]:


import shapely
from shapely.geometry import Point, LineString, Polygon


# In[70]:


#creating a geometric point # we start with a point

point = Point(85.324, 27.717)  # Example: Kathmandu, Nepal
point


# In[71]:


# Create a LineString (sequence of points forming a line)
line = LineString([(85.324, 27.717), (85.330, 27.720), (85.340, 27.730)])
line


# In[72]:


polygon = Polygon([(85.324, 27.717), (85.330, 27.720), (85.340, 27.730), (85.324, 27.717)])
polygon


# In[73]:


point.within(polygon)


# In[74]:


polygon.contains(point)


# In[78]:


point=Point(85.324, 27.717)
point.within(polygon)


# In[ ]:


#WEB MAPPING USING FOLIUM


# In[ ]:


import mapclassify
import folium
import matpotlib


# In[80]:


rupandehi.explore()


# In[81]:


rupandehi.explore(column="PALIKA")


# In[ ]:




