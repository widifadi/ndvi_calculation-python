"""
Functions to perform cloud masking on satellite images.
"""
import numpy as np

def mask_clouds(image_array, mask_array, source='landsat8'):
    """
    Applies a cloud mask based on source-specific logic.
    
    Args:
        image_array (np.ndarray): The input image array.
        mask_array (np.ndarray): The cloud mask array.
        source (str): Source tag (e.g., 'landsat8').
    
    Returns:
        np.ndarray: The cloud-masked image.
    """
    if source == 'landsat8':
        # Assuming last band is pixel_qa (for testing)
        # For Landsat 8, mask_array should contain cloud confidence bitmask
        pixel_qa = image_array[:, :, -1].astype(np.uint16)

        # Bit masks: 3 (cloud shadow), 5 (cloud)
        cloud_shadow = np.bitwise_and(pixel_qa, 1 << 3) != 0
        cloud = np.bitwise_and(pixel_qa, 1 << 5) != 0
        combine_mask = ~(cloud | cloud_shadow) # Invert: True for clear
        
        # Apply mas to all bands except pixel_qa
        masked_image = np.where(combine_mask[:, :, None], image_array[:, :, :-1], np.nan)
        return masked_image
    elif source == 'planetscope':
        raise NotImplementedError("PlanetScope cloud masking not yet implemented.")
    else:
        raise ValueError(f"Unknown source: {source}")
