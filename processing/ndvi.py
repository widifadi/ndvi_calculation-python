"""
NDVI calculation functions.
"""

def calculate_ndvi(nir_band, red_band, source='landsat8'):
    """
    Calculate NDVI from NIR and Red bands for given satellite source.
    
    Args:
        nir_band (np.ndarray): NIR band array.
        red_band (np.ndarray): Red band array.
        source (str): Data source.

    Returns:
        np.ndarray: NDVI image.
    """
    if source == 'landsat8':
        # Landsat 8: NIR = Band 5, Red = Band 4
        # ndvi = (nir_band - red_band) / (nir_band + red_band + 1e-10)
        ndvi = nir_band.substract(red_band).divide(nir_band.add(red_band).add(1e-10))
        return ndvi
    elif source == 'planetscope':
        raise NotImplementedError("NDVI calculation for PlanetScope not implemented.")
    else:
        raise ValueError(f"Unknown source: {source}")
