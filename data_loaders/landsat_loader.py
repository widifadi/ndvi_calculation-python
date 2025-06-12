"""
Module to load Landsat data from Google Earth Engine (GEE) API for testing.
"""

import ee

class LandsatLoader:
    """
    Loader class for landsat satellite imagery
    """
    def __init__(self, api_key=None):
        # Initialize GEE (required auth)
        ee.Initialize()

    def get_images(self, start_date, end_date, aoi):
        """
        Fetch Landsat 8 images within date range and AOI, 
        filter cloud cover, and return image collection or 
        list of images.

        Args:
            start_date (string): image acquisition start date
            end_date (string): image acquisition end date
            aoi (string): area of interest in .geojson file
        """
        collection = (
            ee.ImageCollection("LANDSAT/LC08/C01/T1_SR")
            .filterDate(start_date, end_date)
            .filterBounds(ee.Geometry(aoi))
            .filter(ee.Filter.lt('CLOUD_COVER', 10)) # Filter <10% cloud
        )

        return collection