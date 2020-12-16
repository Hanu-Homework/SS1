from typing import Dict, List, Tuple

# Constant value for recommend_for_person function
# Represent how many people we want to take to generate recommendations
__PICK_COUNT = 3


def calculate_averages(
        book_titles: List[str],
        ratings: List[float]
) -> List[Tuple[float, str]]:
    """Calculate the average rating for each book

    Args:
        book_titles (List[str]): The first parameter.
        ratings (List[float]): The second parameter. Defaults to None.

    Returns:
        List[Tuple[float, str]]: A list that contains pairs of book rating and book title

    Raises:
        AssertionError: If the length of book_titles is not equals to the length of ratings
    """
    assert len(book_titles) == len(ratings)

    # Create a dictionary with:
    #   - book title (string) as key
    #   - that book' s total sum of rating and how many ratings it has received
    #   (to calculate avg in the next step)
    book_to_sum_and_count_dict = dict()

    for book_title, rating in zip(book_titles, ratings):
        if book_title not in book_to_sum_and_count_dict:
            book_to_sum_and_count_dict[book_title] = [rating, 1]
        else:
            book_to_sum_and_count_dict[book_title][0] += rating
            book_to_sum_and_count_dict[book_title][1] += 1

    # With the dictionary above, calculate the average rating for each book
    # Create a list that hold tuples (pairs),
    # with the first element as the average rating and the second as the book title
    book_rating_pairs = []
    for book_title, (sum_rating, rating_count) in book_to_sum_and_count_dict.items():
        average_rating = sum_rating / rating_count
        pair = (average_rating, book_title)

        book_rating_pairs.append(pair)

    # Sort these pairs according to their average rating in the descending order
    book_rating_pairs.sort(key=lambda tup: tup[0], reverse=True)

    return book_rating_pairs


def recommend_for_person(
        username: str,
        username_to_ratings_dict: Dict[str, List[float]],
        index_to_book_map: Dict[int, str]
) -> List[Tuple[float, str]]:

    """Recommends books to a particular person according to their friends' ratings

    Args:
        username (str): The name of the target user
        username_to_ratings_dict (Dict[str, List[float]]): dictionary that map username to their ratings
        index_to_book_map (Dict[int, str]): dictionary that map index to book title

    Returns:
        List[Tuple[float, str]]: A list that contains pairs of book rating and book title

    Raises:
        AssertionError: If username is not found in username_to_ratings_dict record
    """
    assert username in username_to_ratings_dict

    # Get the user ratings for all the book from the dictionary
    user_ratings: List[float] = username_to_ratings_dict[username]

    similarities: List[Tuple[float, str]] = []

    for username_key, ratings in username_to_ratings_dict.items():
        # If this is the target user
        if username_key == username:
            # Then skip this key and value pair
            continue

        # Else, makes dot product of the current user ratings and this other user
        dot_product = sum([this_rating * other_rating for this_rating, other_rating in zip(user_ratings, ratings)])

        # Add the result to the similarities array
        result_pair = (dot_product, username_key)
        similarities.append(result_pair)

    # Sort the similarities in the descending order
    similarities.sort(key=lambda tup: tup[0], reverse=True)

    # Pick the most similar pairs
    most_similar = similarities[:__PICK_COUNT]

    # With the users that share the most similarities with the target user,
    # calculate the average ratings for each book of those user
    book_count = len(index_to_book_map)

    # Create arrays to hold the total rating sum and count
    rating_sums = [0] * book_count
    rating_counts = [0] * book_count

    for _, username in most_similar:
        # Get this user rating
        user_ratings = username_to_ratings_dict[username]

        for index, user_rating in enumerate(user_ratings):
            if user_rating != 0:
                # Then update those sum and count arrays above
                rating_sums[index] += user_rating
                rating_counts[index] += 1
            # Else if the user rating is 0, then do nothing to avoid division by 0

    # From the total rating sum and rating count above, calculate the average rating for each books
    rating_averages = []
    for rating_sum, rating_count in zip(rating_sums, rating_counts):
        # To avoid division by 0
        if rating_count != 0:
            rating_averages.append(rating_sum / rating_count)
        else:
            rating_averages.append(0)

    # Now that we have the average ratings for each book
    # We will map this rating with the corresponding book title
    # by the input param index_to_book_map
    rating_and_book_pairs: List[Tuple[float, str]] = []

    for index, rating_average in enumerate(rating_averages):
        book_title = index_to_book_map[index]
        pair = (rating_average, book_title)
        rating_and_book_pairs.append(pair)

    # Sort the books by their rating in a descending order
    rating_and_book_pairs.sort(key=lambda tup: tup[0], reverse=True)

    return rating_and_book_pairs


if __name__ == '__main__':
    usernames = []
    book_titles = []
    ratings = []

    while True:
        # If any of the three next values is empty, break the loop right away
        username = input()
        if len(username) == 0:
            break

        book_title = input()
        if len(book_title) == 0:
            break

        try:
            rating = float(input())
        except ValueError:
            break

        # Else, add all 3 values to their corresponding array
        usernames.append(username)
        book_titles.append(book_title)
        ratings.append(rating)

    book_titles_set = set(book_titles)
    book_count = len(book_titles_set)

    # Create 2 dicts to map from the book title to its index and vice versa
    book_to_index_map = dict()
    index_to_book_map = dict()

    for index, book_title in enumerate(book_titles_set):
        book_to_index_map[book_title] = index
        index_to_book_map[index] = book_title

    username_to_ratings_dict = dict()
    for username, book_title, rating in zip(usernames, book_titles, ratings):
        if username not in username_to_ratings_dict:
            username_to_ratings_dict[username] = [0] * book_count

        index = book_to_index_map[book_title]
        username_to_ratings_dict[username][index] += rating

    print("""Welcome to the CSC110 Book Recommender. Type the word in the
    left column to do the action on the right.
    recommend : recommend books for a particular user
    averages  : output the average ratings of all books in the system
    quit      : exit the program""")

    result_average = calculate_averages(book_titles=book_titles, ratings=ratings)

    while True:
        print("next task? ", end="")
        task_name = input()

        if task_name == "recommend":
            username = input("user ? ")

            rating_and_book_pairs = recommend_for_person(
                username=username,
                username_to_ratings_dict=username_to_ratings_dict,
                index_to_book_map=index_to_book_map
            )

            for rating, book_title in rating_and_book_pairs:
                print(book_title, rating)

        elif task_name == "averages":

            for rating, book_title in result_average:
                print(book_title, rating)

        elif task_name == "quit":
            break

        print()
