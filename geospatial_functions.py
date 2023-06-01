import geopandas
from geodatasets import get_path
import shapely
import os
import pandas

def read_file(filename)
  path_to_data = get_path(filename)
  gdf = geopandas.read_file(path_to_data)

  gdf

class write_file(layer):

  def __init__(self, layer):
    self.layer = layer
  def write_file(layer):
    layer.to_file("my_file.geojson", driver="GeoJSON")