import numpy as np
import pandas as pd
def survival_chance(titanic_df,start_age,end_age):

    all_df = titanic_df[ ~titanic_df.Age.isna() ]
    df = all_df[ (start_age <= all_df.Age) & (all_df.Age <= end_age)]
    male_df = df[ df.Sex == "male"] 
    survived_male = male_df[ male_df.Survived == 1]
    female_df = df[ df.Sex == "female"]
    survived_female = female_df[ female_df.Survived == 1]
    
    count_male = 0
    count_female = 0
    dic = {}
    if len(male_df) == 0:
        dic["male"] = -1
    else:
        dic["male"] = round( len(survived_male)/len(male_df), 3)
        
    if len(female_df) == 0:
        dic["female"] = -1
    else:
        dic["female"] = round( len(survived_female)/len(female_df), 3)
        
    return dic