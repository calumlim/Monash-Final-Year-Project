#goodreads data preprocessing

import pandas as pd
import math
import time

df = pd.read_csv('br_gk.csv', header=0)
column_bookID = df['bookID']
column_title = df['title']
column_author = df['author']
column_avg_rating = df['rating']
column_ratings_count = df['ratingsCount']
column_reviews_count = df['reviewsCount']
column_reviewer_name = df['reviewerName']
column_user_rating = df['reviewerRatings']
column_text_review = df['review']

def mean_rating(arr):
    n = len(arr)
    mean_val = 0
    count = 0
    for i in range(n):
        if math.isnan(arr[i])!=True:
            mean_val+=float(arr[i])
            count+=1
    mean_val = mean_val/count
    return mean_val

def review_avg_text_count(arr):
    n = len(arr)
    avg_len = 0
    count = 0
    for i in range(n):
        if type(arr[i])!=float:
            avg_len+=len(arr[i].split(" "))
            count+=1
    avg_len = avg_len/count
    return avg_len
def count_unique_users():
    f = open("unique_users.txt", "w")
    n = len(column_reviewer_name)
    unique_users_arr = []
    count = 0
    user_arr = return_array(column_reviewer_name)
    for i in range(n):
        current_user = str(user_arr[i])
        if current_user!='None':
            if i%250==0:
                print("Current progress: ", i, current_user)
            f.write(str(current_user)+"\n")
            for j in range(0,n):
                #unique_users_arr.append(current_user)
                count+=1
                next_user = str(user_arr[j])
                if current_user==next_user:
                    user_arr[j] = None
    f.write(str(count))
    f.close()
    return len(unique_users_arr)
def count_unique_books():
    # n = len(column_title)
    n = 200
    title_arr = return_array(column_title)
    review_arr = return_array(column_text_review)
    count_books = []
    duplicate_index = []

    for i in range(n):
        duplicate_index_tmp = []
        current_book = str(title_arr[i])
        if current_book!='None':
            duplicate_index_tmp.append(current_book)
            start_time = time.time()
            count_duplicate = 0
            for j in range(0,n):
                next_book = str(title_arr[j])
                if next_book==current_book:
                    count_duplicate+=1
                    duplicate_index_tmp.append(j+2)
                    title_arr[j]=None
            count_books.append([current_book, count_duplicate])
            duplicate_index.append(duplicate_index_tmp)
            # print(duplicate_index_tmp)
        # print([current_book, count_duplicate], "Time taken: "+ str(time.time()-start_time), len(title_arr))
    return [count_books, duplicate_index]

def min_max(arr):
    min_val = int(arr[0])
    max_val = int(arr[0])

    for i in range(len(arr)):
        if int(arr[i])<min_val:
            min_val = int(arr[i])
        if int(arr[i])>max_val:
            max_val = int(arr[i])
    return [min_val, max_val]

def return_array(arr):
    new_arr = []
    for i in range(len(arr)):
        new_arr.append(arr[i])
    return new_arr

def print_duplicate_info(arr):
    # book_arr = return_array(column_bookID)
    # author_arr = return_array(column_author)
    # avg_rating_arr = return_array(column_avg_rating)
    # rating_count_arr = return_array(column_ratings_count)
    # review_count_arr = return_array(column_reviews_count)
    # reviewer_arr = return_array(column_reviewer_name)
    review_text_arr = return_array(column_text_review)

    for i in range(len(arr)):
        if len(arr[i])-1>1:
            print("Title: ", arr[i][0], "Count: ", len(arr[i])-1, arr[i])
            for j in range(1,len(arr[i])):
                if type(review_text_arr[arr[i][j]-2])==float:
                    print(review_text_arr[arr[i][j]-2])
                else:
                    if len(review_text_arr[arr[i][j]-2])>50:
                        print(review_text_arr[arr[i][j]-2][0:50])
            print("\n")
# print(len(column_bookID))
# print(min_max(column_bookID))
# print_duplicate_info(count_unique_books()[1])
print(count_unique_users())
# count_unique_books()
# print("Mean rating: ",mean_rating(column_user_rating))
# print("Avg. length of review: ",review_avg_text_count(column_text_review))
