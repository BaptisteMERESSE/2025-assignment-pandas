"""Visualization of referendum results in France using pandas and geopandas."""
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


def load_data():
    """Load data from the CSV files referendum/regions/departments."""
    referendum = pd.DataFrame({})
    regions = pd.DataFrame({})
    departments = pd.DataFrame({})
    return referendum, regions, departments


def merge_regions_and_departments(regions, departments):
    """Merge regions and departments in one DataFrame.

    The columns in the final DataFrame should be:
    ['code_reg', 'name_reg', 'code_dep', 'name_dep']
    """
    return pd.DataFrame({})


def merge_referendum_and_areas(referendum, regions_and_departments):
    """Merge referendum and regions_and_departments in one DataFrame.

    Drop lines relative to DOM-TOM-COM departments and French living abroad,
    which have a code containing 'Z'.
    """
    return pd.DataFrame({})


def compute_referendum_result_by_regions(referendum_and_areas):
    """Return a table with the absolute count for each region.

    The returned DataFrame should be indexed by 'code_reg' and have columns:
    ['name_reg', 'Registered', 'Abstentions', 'Null', 'Choice A', 'Choice B']
    """
    return pd.DataFrame({})


def plot_referendum_map(referendum_result_by_regions):
    """Plot a map with the results from the referendum.

    * Load the geographic data with geopandas from 'regions.geojson'.
    * Merge with 'referendum_result_by_regions'.
    * Display the map showing the rate of 'Choice A' over expressed ballots.
    * Return a GeoDataFrame with a column 'ratio' containing the results.
    """
    return gpd.GeoDataFrame({})


if __name__ == "__main__":
    referendum, df_reg, df_dep = load_data()
    regions_and_departments = merge_regions_and_departments(df_reg, df_dep)
    referendum_and_areas = merge_referendum_and_areas(referendum, regions_and_departments)
    referendum_results = compute_referendum_result_by_regions(referendum_and_areas)
    print(referendum_results)
    plot_referendum_map(referendum_results)
    plt.show()
