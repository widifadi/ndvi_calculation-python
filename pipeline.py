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
    def __init__(self, source="landsat8", start_date=None, end_date=None, region=None):
        self.source = source
        self.start_date = start_date
        self.end_date = end_date
        self.region = region

    # def run(self):
    #     """_summary_

    #     Raises:
    #         NotImplementedError: not implemented 

    #     Returns:
    #         _type_: _description_
    #     """
    #     print(f"Running pipeline for source: {self.source}")
        
    #     if self.source == "landsat8":
    #         loader = LandsatLoader(self.start_date, self.end_date, self.region)
    #         collection = loader.load_data()
    #         processed = collection.map(self._process_landsat8)
    #         return processed
    #     else:
    #         raise NotImplementedError(f"Source '{self.source}' not supported yet.")

    def process(self, image_collection):
        """Process the image collection with appropriate functions"""
        print(f"Processing pipeline for source: {self.source}")
        if self.source == "landsat8":
            return image_collection.map(self._process_landsat8)
        else:
            raise NotImplementedError(f"Source '{self.source}' not supported yet.")

    def _process_landsat8(self, image):
        image = atmospheric_correction(image, source="landsat8")
        cloud_mask = image.select('pixel_qa') # QA band
        masked_image = mask_clouds(image, cloud_mask, source="landsat8")

        # Extract NIR (Band 5) and Red (Band 4)
        nir = masked_image[:, :, 3]
        red = masked_image[:, :, 4]
        image = calculate_ndvi(nir, red, source="landsat8")
        return image
