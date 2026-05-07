python
import pandas as pd
import geopandas as gpd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

# Load the dataset
def load_data(file_path):
    return pd.read_excel(file_path)

# Function to geocode addresses
def geocode_address(address):
    geolocator = Nominatim(user_agent="geoapiExercises")
    try:
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except GeocoderTimedOut:
        return None, None

# Apply geocoding to the dataset
def add_geocode_data(df):
    latitudes = []
    longitudes = []
    for address in df["Address"]:
        lat, lon = geocode_address(address)
        latitudes.append(lat)
        longitudes.append(lon)
    df["Latitude"] = latitudes
    df["Longitude"] = longitudes
    return df

# Save the cleaned dataset
def save_data(df, output_file):
    df.to_csv(output_file, index=False)

# Main function
if __name__ == "__main__":
    input_file = "Address (1)_Address_part_1_0.xlsx"
    output_file = "Cleaned_Business_License_Data.csv"

    # Load the data
    data = load_data(input_file)

    # Clean and enrich the data
    cleaned_data = add_geocode_data(data)

    # Save the cleaned dataset
    save_data(cleaned_data, output_file)
    print(f"Cleaned data saved to {output_file}")
