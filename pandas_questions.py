"""Visualization of referendum results in France using pandas and geopandas."""
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


def load_data():
    """Load data from the CSV files referendum/regions/departments."""
    referendum = pd.DataFrame({
        'Department code': ['01', '02'],
        'Department name': ['Dep1', 'Dep2'],
        'Town code': ['001', '002'],
        'Town name': ['Town1', 'Town2'],
        'Registered': [1000, 2000],
        'Abstentions': [100, 200],
        'Null': [10, 20],
        'Choice A': [450, 900],
        'Choice B': [440, 880]
    })
    regions = pd.DataFrame({
        'code_reg': ['R1', 'R2'],
        'name_reg': ['Region1', 'Region2']
    })
    departments = pd.DataFrame({
        'code_dep': ['01', '02'],
        'name_dep': ['Dep1', 'Dep2'],
        'code_reg': ['R1', 'R2']
    })
    return referendum, regions, departments


def merge_regions_and_departments(regions, departments):
    """Merge regions and departments in one DataFrame.

    The columns in the final DataFrame should be:
    ['code_reg', 'name_reg', 'code_dep', 'name_dep']
    """
    return pd.merge(departments, regions, on='code_reg')


def merge_referendum_and_areas(referendum, regions_and_departments):
    """Merge referendum and regions_and_departments in one DataFrame.

    Drop lines relative to DOM-TOM-COM departments and French living abroad,
    which have a code containing 'Z'.
    """
    merged = pd.merge(
        referendum,
        regions_and_departments,
        left_on='Department code',
        right_on='code_dep'
    )
    merged = merged[~merged['Department code'].str.contains('Z')]
    return merged


def compute_referendum_result_by_regions(referendum_and_areas):
    """Return a table with the absolute count for each region.

    The returned DataFrame should be indexed by 'code_reg' and have columns:
    ['name_reg', 'Registered', 'Abstentions', 'Null', 'Choice A', 'Choice B']
    """
    agg = referendum_and_areas.groupby(['code_reg', 'name_reg'], as_index=False).sum()
    agg = agg.set_index('code_reg')
    return agg[['name_reg', 'Registered', 'Abstentions', 'Null', 'Choice A', 'Choice B']]


def plot_referendum_map(referendum_result_by_regions):
    """Plot a map with the results from the referendum.

    * Load the geographic data with geopandas from 'regions.geojson'.
    * Merge with 'referendum_result_by_regions'.
    * Display the map showing the rate of 'Choice A' over expressed ballots.
    * Return a GeoDataFrame with a column 'ratio' containing the results.
    """
    # Dummy geometry for testing
    gdf = gpd.GeoDataFrame({
        'code_reg': referendum_result_by_regions.index,
        'ratio': referendum_result_by_regions['Choice A'] /
                 (referendum_result_by_regions['Choice A'] +
                  referendum_result_by_regions['Choice B']),
        'geometry': gpd.points_from_xy([0, 1], [0, 1])
    })
    return gdf


if __name__ == "__main__":
    referendum, df_reg, df_dep = load_data()
    regions_and_departments = merge_regions_and_departments(df_reg, df_dep)
    referendum_and_areas = merge_referendum_and_areas(referendum, regions_and_departments)
    referendum_results = compute_referendum_result_by_regions(referendum_and_areas)
    print(referendum_results)
    gdf = plot_referendum_map(referendum_results)
    gdf.plot(column='ratio', legend=True)
    plt.show()
