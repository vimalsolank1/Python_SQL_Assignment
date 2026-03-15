''' 
1. Task 1 - Python Requests
a) Use the requests python package to fetch data from the following API link -
https://jsonplaceholder.typicode.com/posts
b) Fetch all posts and print them
c) Count the distinct number of users
d) Which user has the highest number of posts ?
e) What is average word length of post title ?
f) You may use pandas, numpy and any other packages for the above requirement'''

import requests
import pandas as pd
# fetch data from api
response=requests.get('https://jsonplaceholder.typicode.com/posts') 
# convert response to json 
json_data=response.json() 


# --->b) Fetch all posts and print them
print("All posts:-\n")
for post in json_data:
    print(post)


df=pd.DataFrame(json_data)
# ---> c) Count the distinct number of users
distinct_users = df['userId'].nunique()
print(f"distinct number of users are {distinct_users}")


# --> d) Which user has the highest number of posts ?
user_post_count = df['userId'].value_counts()
# find the user  who has the highest number of posts
top_user = user_post_count.idxmax()
print(f"user with highest number of posts is  {top_user}")


# --> e) What is average word length of post title ?

# function to calculate average word length in a title
def avg_word_length(title):
    words = title.split()

    lengths = [len(word) for word in words]
    return sum(lengths) / len(lengths)


# apply function to  all titles
df["word_length"] = df["title"].apply(avg_word_length)

# calculate overall average
overall_avg = df["word_length"].mean()
print("Average word length of post titles is  ", round(overall_avg,2))