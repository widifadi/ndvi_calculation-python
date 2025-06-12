"""
Main script to run automatic pipeline of imagery processing.
Loads environment variables, initializes data loaders and pipeline,
and executes the processing workflow.  
"""
import os
from dotenv import load_dotenv
from data_loaders.landsat_loader import LandsatLoader
from pipeline import NDVIPipeline

def main():
    """
    Main function
    """
    # Load .env and read variables
    load_dotenv()

    # Dynamicly set the credentials
    PLANET_API_KEY = os.getenv('PLANET_API_KEY')
    PLANET_USERNAME = os.getenv('PLANET_USERNAME')
    PLANET_PASSWORD = os.getenv('PLANET_PASSWORD')

    GEE_CREDENTIALS_PATH = os.getenv('GEE_CREDENTIALS_PATH')
    
    LANDSAT_API_KEY = os.getenv("LANDSAT_API_KEY")

    landsat_loader = LandsatLoader(api_key=LANDSAT_API_KEY)

    # Define time range and area of interest (AOI)
    start_date = "2023-01-01"
    end_date = "2023-03-31"
    aoi = {
        "type": "Polygon",
        "coordinates": [
            [
                [-120.0, 37.0],
                [-119.0, 37.0],
                [-119.0, 38.0],
                [-120.0, 38.0],
                [-120.0, 37.0]
            ]
        ]
    } # Change to .geojson file

    # Initialize the pipeline
    pipeline = NDVIPipeline()

    images = landsat_loader.get_images(start_date, end_date, aoi)
    results = pipeline.process(images)

    print("Processing complete.")

    # Save RGB Mosaic Image, NDVI Image, MultiSpectral Image and its metadata

if __name__ == "__main__":
    main()







