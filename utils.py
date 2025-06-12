"""
Utility functions for file I/O, metadata handling, and other helpers.
"""

import rasterio

def save_geotiff(image_array, profile, output_path):
    """
    Save a numpy array as GeoTIFF using rasterio.

    Args:
        image_array (np.ndarray): Image data array.
        profile (dict): Rasterio profile metadata.
        output_path (str): Output file path.
    """
    with rasterio.open(output_path, 'w', **profile) as dst:
        dst.write(image_array, 1)
