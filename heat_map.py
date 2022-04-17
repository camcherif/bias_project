import geopandas as gpd, pandas as pd, matplotlib as plt, geoplot as gplot, mapclassify, pycountry, pandas as pd


##to remove once implemented with mother script
countries = ['Canada', 'United States', 'Mexico', 'Singapore', 'New Zealand', 'Australia', 'France', 'United Kingdom', 'Japan', 'South Africa']

def heat_map(countries, google_score, yahoo_score):
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    world = world.drop(columns=['gdp_md_est', "pop_est", "iso_a3", "continent"])
    world = world.loc[world['name'].isin(countries)]
    world['alpha_2']=world['name'].apply(lambda x: pycountry.countries.get(name=x).alpha_2)


    fig, ax = plt.subplots(figsize = (10,4), facecolor = plt.cm.Blues(.2))
    fig.suptitle('Country ',
                fontsize = 'xx-large',  
                fontweight = 'bold')
    ax.set_facecolor(plt.cm.Blues(.2))
    world.plot(column = 'pop_est',
            cmap = 'Greens',
            ax = ax,
            legend = True)

    plt.show()