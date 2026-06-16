# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as mp

airbnb_nyc=pd.read_csv('Airbnb_ratings_NYC_2019.csv') #This line of code loads the data set

# Task 1: Provides Values.
#a. What is the median price for hotel listings in “Manhattan" (neighbourhood group)?

median_price_manhattan_hotel = airbnb_nyc[
    (airbnb_nyc["neighbourhood_group"] == "Manhattan")]["price"].median()

#b.How many entire homes/apartments are listed in the "SoHo" (neighbourhood)?

number_homes_apart_soHo = airbnb_nyc[
    (airbnb_nyc["neighbourhood"] == "SoHo") &
    (airbnb_nyc["room_type"] == "Entire home/apt")
].shape[0] #Shape helps count the number of rows

#c.How many hosts (based on host_id) in "Williamsburg" (neighbourhood) have listed more than
#two entire homes/apartments?

williamsburg_entire = airbnb_nyc[
    (airbnb_nyc["neighbourhood"] == "Williamsburg") &
    (airbnb_nyc["room_type"] == "Entire home/apt")
]

host_counts = williamsburg_entire.groupby("host_id")["id"].count()
hosts_more_than_2 = host_counts[host_counts > 2].shape[0]

#Task 2: 
#a.filters the hotel reviews DataFrame based on user-given parameters: ‘neighbourhood’,
#‘minimum_price’, and ‘minimum_number_of_reviews’. The function should return the filtered
#DataFrame that includes only columns [‘host_name’, ‘neighbourhood’, ‘price’,
#‘number_of_reviews’].


    # print("Enter your neighbourhood")
    # neighbour_hood = input().strip()
    
    # print("Enter minimum price")
    # min_price = int(input())
    
    # print("Enter the minimum number of reviews")
    # min_num_reviews = int(input())
    
def hotel_review(df, neighbourhood, minimum_price, minimum_number_of_reviews,
                  price_strict=False, reviews_strict=False):
    # """
    # Filters a hotel DataFrame based on neighbourhood, minimum price, and minimum number of reviews.
    # Prints top 10 hotels by number_of_reviews, total hotels, and unique hosts.
    
    # Parameters:
    # - df: pandas DataFrame containing hotel data
    # - neighbourhood: str or None
    # - minimum_price: int or float
    # - minimum_number_of_reviews: int
    # - price_strict: bool, if True, filter price strictly greater than minimum_price
    # - reviews_strict: bool, if True, filter number_of_reviews strictly greater than minimum_number_of_reviews
    # """
    filtered = df.copy()
    
    # Filter by neighbourhood
    if neighbourhood:
        filtered = filtered[filtered['neighbourhood'] == neighbourhood]
        
    # Filter by price
    if price_strict:
        filtered = filtered[filtered['price'] > minimum_price]
    else:
        filtered = filtered[filtered['price'] >= minimum_price]
    
    # Filter by number_of_reviews
    if reviews_strict:
        filtered = filtered[filtered['number_of_reviews'] > minimum_number_of_reviews]
    else:
        filtered = filtered[filtered['number_of_reviews'] >= minimum_number_of_reviews]
    
    # Keep only required columns
    filtered = filtered[['host_name', 'neighbourhood', 'price', 'number_of_reviews']]
    
    # Check if any results
    if filtered.empty:
        print("No matching results")
        return None
    
    # Print top 10 hotels by number_of_reviews
    top_10 = filtered.sort_values(by='number_of_reviews', ascending=False).head(10)
    print("Top hotels based on number of reviews:")
    print(top_10)
    
    # Print total hotels and unique hosts
    total_hotels = filtered.shape[0]
    unique_hosts = filtered['host_name'].nunique()
    print(f"\nTotal hotels meeting criteria: {total_hotels}")
    print(f"Unique hosts managing these hotels: {unique_hosts}")
    
    return filtered

result =hotel_review(airbnb_nyc,"Hell's Kitchen", 150, 5,  price_strict=True, reviews_strict=False)


#Task 3: Create a summary table for hotels in all neighbourhoods based on ‘minimum price’ = 50 and
#‘minimum_number_of_reviews’ = 5. You can use the function from Question 2 to help aggregating data:
#a. For each neighbourhood in this summary table, calculate:
#The total number of hotels listed.
# The average price of hotels
#According to the summary, which neighbourhood has the highest and lowest average prices? Provide
#the values.

new_min_price=50
new_min_num_reviews=5

#Creating an array to contain the data from the loop.
summary_data=[]

# Loop through each neighbourhood in the dataset
for hood in airbnb_nyc["neighbourhood"].unique():
    filtered_df = hotel_review(airbnb_nyc, hood, new_min_price, new_min_num_reviews,
                      price_strict=False, reviews_strict=False)
    
    if filtered_df is not None:
        total_hotels = len(filtered_df)
        avg_price = filtered_df["price"].mean()
        
        summary_data.append({
            "neighbourhood": hood,
            "total_hotels": total_hotels,
            "average_price": avg_price
        })


#Converting the summary table to a dataframe
summary_table=pd.DataFrame(summary_data)

#Getting the highest and lowest average price respectively
highest_avg = summary_table.loc[summary_table["average_price"].idxmax()]
lowest_avg = summary_table.loc[summary_table["average_price"].idxmin()]

#Task 4: Summarize the hotel data by price categories and visualize the results: 
#a. Create price categories for the hotels: - Low: Hotels with prices less than $100. 
#- Medium: Hotels with prices between $100 and $200. - High: Hotels with prices over $200. 
#For each price category, 
#calculate: 
#- The total number of hotels. 
#- The average number of reviews per hotel.


#First we need to create a function that sorts out the prices to the three different categories based on their specified
#criteria.

def category_price(price):
    if price < 100:
        return "Low"
    elif 100<=price<=200:
        return "Medium"
    else:
         return "High"
     
 # Now, we need to create a new column to the current data set that indicates whether a price is low, medium, or high.
 
airbnb_nyc["price_category"]=airbnb_nyc["price"].apply(category_price)
 
 #Aggregate summary 
summary_price = airbnb_nyc.groupby("price_category").agg(
    total_hotels=("host_name", "count"),
    avg_reviews=("number_of_reviews", "mean")
).reset_index()

print("Price Category Summary")
print(summary_price)
 

#Let us visualise the result we got.
#A bar chart showing the total number of hotels in each price category

#We use the matplotlib library we loaded as mp
fig, ax1 = mp.subplots(figsize=(8,5))

ax1.bar(summary_price["price_category"], summary_price["total_hotels"], alpha=0.8)
ax1.set_xlabel("Price Category")
ax1.set_ylabel("Total number of Hotels", color="blue")

#Line plot for the average reviews per hotels
ax2=ax1.twinx()
ax2.plot(summary_price["price_category"], summary_price["avg_reviews"], color="red", marker="o", linewidth=2)
ax2.set_ylabel("Average Number of Reviews")
ax2.tick_params(axis="y", labelcolor="red")

# Enhancing the visual appearance
mp.title("Hotel Summary by Price Category")
mp.tight_layout()
mp.show()


     
        