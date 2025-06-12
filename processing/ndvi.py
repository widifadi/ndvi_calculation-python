"""
NDVI calculation functions.
"""

def calculate_ndvi(image):
    """
    Calculate NDVI from the given image.
    
    Args:
        image: input satellite image
    
    Returns:
        NDVI image
    """
    # Assuming image has bands 'NIR' and 'RED'
    # Example for GEE:
    # ndvi = image.normalizedDifference(['NIR', 'RED']).rename('NDVI')
    
    raise NotImplementedError("NDVI calculation function not implemented yet.")
