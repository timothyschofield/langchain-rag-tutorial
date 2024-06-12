"""

    File : ny_dataframe_query.py

    Author: Tim Schofield
    Date: 12 June 2024


"""
import pandas as pd
import os
from dotenv import load_dotenv
from helper_functions_langchain_rag import get_file_timestamp, is_json, cleanup_json, create_and_save_dataframe
from pathlib import Path
from openai import OpenAI

MODEL = "gpt-4o" # Context window of 128k max_tokens 4096

project_name = "ny_geo_authority_dataframe"

# The file to be compared against the authority database
input_folder = "ny_hebarium_location_csv_input"

input_transcibed_file = "NY_specimens_transcribed.csv" # ###### Note: this is the one that they gave us ######
input_transcibed_path = Path(f"{input_folder}/{input_transcibed_file}")

input_authority_file = "NY_Geopolitical_Lookup_Lists_50000.csv"
input_authority_path = Path(f"{input_folder}/{input_authority_file}")

output_folder = "ny_hebarium_location_csv_output"

batch_size = 20 # saves every
time_stamp = get_file_timestamp()


load_dotenv()
try:
    my_api_key = os.environ['OPENAI_API_KEY']          
    client = OpenAI(api_key=my_api_key)
except Exception as ex:
    print("Exception:", ex)
    exit()

df_authority = pd.read_csv(input_authority_path)
print(df_authority.head())
















