import pandas as pd
from fuzzywuzzy import fuzz



df_p_ice = pd.read_excel("data/pronto-icebreaker-master.xlsx",header=0)


# ice = pd.read_excel("./data/ICE Wi24 Indent Internal w Targets 26.06.23.xlsx")
df_ice = pd.read_excel("data/ice.xlsx", header=0)
print(df_ice.columns)

# get first row
first_row_df_ice = df_ice.iloc[[0]]

# Loop through each row in df_ice
# for row in first_row_df_ice.itertuples(index=True, name='Row'):
for row in df_ice.itertuples(index=True, name='Row'):
    print(f"Processing row {row.Index}:")
    # print(f"style: {row.Style_Name}, colour: {row.Color_Name}, size: {row.Size}")


    for p_ice_row in df_p_ice.itertuples(index=True, name='Row'):

        # extract strings
        ice_string = row.Style_Name
        p_string = p_ice_row.Style 
        # Calculate similarity
        similarity_score = fuzz.token_set_ratio(ice_string, p_string)



        # print(f"Processing icebreaker master row {p_ice_row.Index}:")
        # print(f"style: {row.Style_Name}, colour: {row.Color_Name}, size: {row.Size}")
        # print(f"p_style: {p_ice_row.Style}, p_colour: {p_ice_row.Colour}, size: {p_ice_row.Size}")

        if similarity_score > 60 and row.Color_Name == p_ice_row.Colour and row.Size == p_ice_row.Size and row.gender == p_ice_row.gender:

            print(f"Similarity score: {similarity_score}")
            print(f"style: {row.Style_Name}, colour: {row.Color_Name}, size: {row.Size}")
            print(f"p_style: {p_ice_row.Style}, p_colour: {p_ice_row.Colour}, size: {p_ice_row.Size}")

