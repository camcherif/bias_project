import geopandas as gpd, pandas as pd, matplotlib.pyplot as plt, geoplot as gplot, mapclassify, pycountry, pandas as pd
from yahoo_bias import yahoo_autosugg
from google_query import google_q
from sentiment import senti 

##to remove once implemented with mother script

def heat_map(country, var, google_score, yahoo_score):
        google_score = pd.DataFrame(google_score, columns=['google_idx','alpha_2'])
        yahoo_score = pd.DataFrame(yahoo_score, columns=['yahoo_idx','alpha_2'])
        world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
        world = world.drop(columns=['gdp_md_est', "pop_est", "iso_a3", "continent"])
        world = world.replace(to_replace='United States of America', value='United States')
        world = world.loc[world['name'].isin(country)]
        world['alpha_2'] = world['name'].apply(lambda x: pycountry.countries.get(name=x).alpha_2)

        world_google = world.loc[world['alpha_2'].isin(google_score['alpha_2'])]
        google_score = google_score.loc[google_score['alpha_2'].isin(world['alpha_2'])]
        world_google = pd.merge(world_google, google_score, on='alpha_2')

        world_yahoo = world.loc[world['alpha_2'].isin(yahoo_score['alpha_2'])]
        yahoo_score = yahoo_score.loc[yahoo_score['alpha_2'].isin(world['alpha_2'])]
        world_yahoo = pd.merge(world_yahoo, yahoo_score, on='alpha_2')

        var = var.title()
        colour_scheme = plt.cm.get_cmap('jet').reversed()

        fig, ax = plt.subplots(figsize = (10,4), facecolor = plt.cm.Blues(.2))
        fig.suptitle('Google Bias by Country for ' + var,
                fontsize = 'xx-large',  
                fontweight = 'bold')
        ax.set_facecolor(plt.cm.Blues(.2))
        world_google.plot(column = 'google_idx',
                cmap = colour_scheme,
                ax = ax,
                legend = True,
                vmin = min([min(world_google['google_idx']), min(world_yahoo['yahoo_idx'])]),
                vmax = max([max(world_google['google_idx']), max(world_yahoo['yahoo_idx'])]))

        plt.show()


        fig, ax = plt.subplots(figsize = (10,4), facecolor = plt.cm.Blues(.2))
        fig.suptitle('Yahoo Bias by Country for ' + var,
                fontsize = 'xx-large',  
                fontweight = 'bold')
        ax.set_facecolor(plt.cm.Blues(.2))
        world_yahoo.plot(column = 'yahoo_idx',
                cmap = colour_scheme,
                ax = ax,
                legend = True,
                vmin = min([min(world_google['google_idx']), min(world_yahoo['yahoo_idx'])]),
                vmax = max([max(world_google['google_idx']), max(world_yahoo['yahoo_idx'])]))

        plt.show()
        return