"""
Main pipeline classes integrating data acquisition and processing steps.
"""

from processing.cloud_masking import mask_clouds
from processing.atmospheric_correction import atmospheric_correction
from processing.ndvi import calculate_ndvi

class NDVIPipeline:
    """
    Main NDVI pipeline class integrating data acquisition and processing steps.
    """
    def __init__(self):
        pass

    def process(self, images):
        """
        Run the entire processing pipeline:
        1. Atmospheric correction
        2. Cloud masking
        3. NDVI calculation
        4. Mosaicking and saving results (to be implemented)
        
        Args:
            images: input images (could be ee.ImageCollection or list)
        
        Returns:
            Processed results (e.g. NDVI mosaics)
        """
        # Example (pseudocode):
        corrected = []
        for img in images:
            atm = atmospheric_correction(img)
            cloud_free = mask_clouds(atm)
            ndvi_img = calculate_ndvi(cloud_free)
            corrected.append(ndvi_img)

        # TODO: mosaic images, save output files
        return corrected
