"""
Module for PlanetScope data acquisition.
To be implemented.
"""

class PlanetScopeLoader:
    """
    Loader class for PlanetScope satellite imagery
    """
    def __init__(self, api_key=None, userName=None, passWord=None):
        # TODO: Implement auth process and initialization
        pass

    def get_images(self, start_date, end_date, aoi):
        """
        TODO: Acquire PlanetScope images for the given time range and area

        Args:
            start_date (string): image acquisition start date
            end_date (string): image acquisition end date
            aoi (string): area of interest in .geojson file
        """
        raise NotImplementedError("PlanetScope data acquisition is not yet imlemented.")