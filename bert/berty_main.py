# main.py
from model import load_model_and_tokenizer
from utils import encode_text
from similarity import compute_similarity

import pandas as pd
from fuzzywuzzy import fuzz
import time

from tqdm import tqdm 


def main():
    # Load pre-trained model and tokenizer
    tokenizer, model = load_model_and_tokenizer()

    # read excel files
    df_p_ice = pd.read_excel("data/pronto-icebreaker-master.xlsx",header=0)
    df_ice = pd.read_excel("data/ice.xlsx", header=0)

    # get first row
    first_row_df_ice = df_ice.iloc[[0]]

    # Prepare a list to store results
    results = []


    # loop through each row in df_ice and look for similarities 
    # for row in first_row_df_ice.itertuples(index=True, name='Row'):
    for row in tqdm(df_ice.itertuples(index=True, name='Row'), total=len(df_ice), desc="Processing ICE Products", leave=False):
        for p_ice_row in tqdm(df_p_ice.itertuples(index=True, name='Row'), total=len(df_p_ice), desc="Comparing with P-ICE Products", ):
         

            # print(f"running on {row.Style_Name}")

            # extract strings
            ice_string = row.Style_Name
            p_string = p_ice_row.Style 
            # Calculate similarity
            similarity_score = fuzz.token_set_ratio(ice_string, p_string)

            # print(f"Processing icebreaker master row {p_ice_row.Index}:")
            # print(f"style: {row.Style_Name}, colour: {row.Color_Name}, size: {row.Size}")
            # print(f"p_style: {p_ice_row.Style}, p_colour: {p_ice_row.Colour}, size: {p_ice_row.Size}")

            if similarity_score > 50 and row.Color_Name == p_ice_row.Colour and row.Size == p_ice_row.Size and row.gender == p_ice_row.gender:

                print(f"Similarity score: {similarity_score}")
                print(f"style: {row.Style_Name}, colour: {row.Color_Name}, size: {row.Size}")
                print(f"p_style: {p_ice_row.Style}, p_colour: {p_ice_row.Colour}, size: {p_ice_row.Size}")

                # Example texts
                text1 = "560 ELEMENTAL LS ZIP JKT "
                text2 = "Merino 560 RealFleece Elemental II LS Zip"

                text3 = "560 ELEMENTAL LS ZIP JKT W"
                text4 = "Merino 560 RealFleece Elemental II LS Zip"

                # Encode texts
                embedding1 = encode_text(tokenizer, model, row.Style_Name)
                embedding2 = encode_text(tokenizer, model, p_ice_row.Style)

                # Compute similarity
                bert_similarity_score = compute_similarity(embedding1, embedding2)
                print(f"Similarity score: {bert_similarity_score}, {row.Style_Name}, {p_ice_row.Style}")
                # time.sleep(4)

                results.append({
                    "Ice_SKU": row.SKU,
                    "ice_style": row.Style_Name,
                    "pronto_sku": p_ice_row.Item_Code,
                    "fuzzy_score": similarity_score,
                    "bert_score": bert_similarity_score
                })

    # Convert results to DataFrame
    results_df = pd.DataFrame(results)

    # Write results to a new Excel file
    results_df.to_excel("data/related_products.xlsx", index=False)


if __name__ == "__main__":
    main()
