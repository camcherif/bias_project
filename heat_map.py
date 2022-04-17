import geopandas as gpd, pandas as pd, matplotlib as plt, geoplot as gplot, mapclassify

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world = world.drop(columns=['gdp_md_est', "pop_est", "iso_a3", "continent"])