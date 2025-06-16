"""
Functions to perform atmospheric correction on satellite images.
"""

def atmospheric_correction(image_array, source='landsat8'):
    """
    Applies atmospheric correction based on the satellite source.
    
    Args:
        image_array (np.ndarray): Image data to correct.
        source (str): Source tag.
    
    Returns:
        np.ndarray: Atmospherically corrected image.
    """
    if source == 'landsat8':
        # TOA to surface reflectance estimation placeholder
        # In reality, you would use something like LEDAPS or LaSRC outputs if available
        return image_array / 10000.0  # Landsat scaling factor
    elif source == 'planetscope':
        raise NotImplementedError("PlanetScope atmospheric correction not yet implemented.")
    else:
        raise ValueError(f"Unknown source: {source}")
    