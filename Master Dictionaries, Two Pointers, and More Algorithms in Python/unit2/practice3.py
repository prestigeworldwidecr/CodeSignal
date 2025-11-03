'''

You are developing an application that provides users with movie recommendations based on their past viewing history. The goal is to identify a list of popular movies the user has not yet watched. You are provided with three arrays (lists in Python): user_history, popular_movies, and unpopular_movies.

The user_history array consists of integers representing the IDs of movies the user has already watched. The popular_movies array contains integers representing the IDs of movies that are currently popular according to some source. The unpopular_movies array contains integers representing movies that are not popular according to some other source.

Your task is to develop a Python function named recommend_movies(user_history, popular_movies, unpopular_movies) that takes these three arrays as inputs and returns a new array. This array should contain the IDs of the popular movies that the user has not yet watched, and which are not included in the unpopular_movies array.

The resulting array should be sorted in ascending order, and each ID in the array should be unique (no repeats).

Note: The input arrays can contain between 1 and 1000000 elements (inclusive) and the elements are between 1 and 1000000 inclusive.

'''

def recommend_movies(user_history, popular_movies, unpopular_movies) :
# {
    # TODO: implement the function to recommend movies.
    s1 = set(user_history)
    s2 = set(popular_movies)
    s3 = set(unpopular_movies)

    return sorted(list(s2 - s1 - s3))
# }

user_history = [1, 2, 3, 4, 5]
popular_movies = [1, 2, 3, 6, 7, 8, 9, 10]
unpopular_movies = [4, 5, 11]
# expected = [6, 7, 8, 9, 10]

print(recommend_movies(user_history, popular_movies, unpopular_movies))

'''

***** BONEYARD *****

'''