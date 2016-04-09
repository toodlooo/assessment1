"""Skills Assessment: Lists

Edit the function bodies until all of the doctests pass when you run this file.
"""


def all_odd(number_list):
    """Return a list of only the odd numbers in the input list.

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []

    """

    all_odd = []

    for number in number_list:
        if number % 2 != 0:
            all_odd.append(number)

    return all_odd

    # This took about 2-5 minutes

def all_even(number_list):
    """Return a list of only the even numbers in the input list.

        >>> all_even([2, 6, -1, -2])
        [2, 6, -2]

        >>> all_even([-1, 3, 5])
        []

    """

    all_even = []

    for number in number_list:
        if number % 2 == 0:
            all_even.append(number)

    return all_even

    # This took about less than a minute because of the previous one


def print_indexes(my_list):
    """Print the index of each item in the input_list, followed by the item itself.

    Do this without using a counting variable---that is, don't do something like this:

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this:

        >>> print_indexes(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo

    """

    for item in my_list:
        index_number = my_list.index(item)
        index_and_item = "{} {}".format(index_number, item)
        print index_and_item

    # Took about 10-15 minutes (I gave up and went back to it later)

def long_words(word_list):
    """Return all words in input list that are longer than 4 characters.

        >>> long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

        >>> long_words(["all", "are", "tiny"])
        []

    """

    long_words = []

    for word in word_list:
        if len(word) > 4:
            long_words.append(word)

    return long_words

    # Took about 5-10 minutes

def smallest_int(number_list):
    """Find the smallest integer in a list of integers and return it.

    DO NOT USE the built-in function `min`!

        >>> smallest_int([-5, 2, -5, 7])
        -5


        >>> smallest_int([3, 7, 2, 8, 4])
        2

    If the input list is empty, return None:


        >>> smallest_int([]) is None
        True

    """

    if number_list != []:
        smallest_int = number_list[0]
        for item in number_list:
            if item < smallest_int:
                smallest_int = item
        return smallest_int
    elif number_list == []:
        return None

    # Took about 5-10 minutes

def largest_int(number_list):
    """Find the largest integer in a list of integers and return it.

    DO NOT USE the built-in function `max`!

        >>> largest_int([-5, 2, -5, 7])
        7

        >>> largest_int([3, 7, 2, 8, 4])
        8

    If the input list is empty, return None:

        >>> largest_int([]) is None
        True

    """

    if number_list != []:
        largest_int = number_list[0]
        for item in number_list:
            if item > largest_int:
                largest_int = item
        return largest_int
    elif number_list == []:
        return None

    # Took about 1 minute since I solved the previous one


def halvesies(number_list):
    """Return list of numbers from input list, each divided by two.

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are odd, make sure you don't round off the half:

        >>> halvesies([1, 5])
        [0.5, 2.5]

    """

    cut_in_half = []

    for item in number_list:
        item_in_half = float(item) / 2
        cut_in_half.append(item_in_half)

    return cut_in_half

    # Took about 10-20 minutes after coming back to this one later before it could work

def word_lengths(word_list):
    """Return the length of words in the input list.

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]

    """

    word_lengths = []

    for word in word_list:
        length = len(word)
        word_lengths.append(length)

    return word_lengths

    # Took about 2-5 minutes


def sum_numbers(number_list):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does this -- but for
    this exercise, you should not use it.

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero:

        >>> sum_numbers([])
        0

    """

    sum_numbers = 0

    if number_list != []:
        for number in number_list:
            sum_numbers += number
        return sum_numbers
    else:
        return 0

    # Took about 2-5 minutes


def mult_numbers(number_list):
    """Return product (result of multiplication) of the numbers in the list.

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in the input, the product will be zero:

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product, if the list is
    empty, the product should be 1:

        >>> mult_numbers([])
        1

    """

    mult_numbers = 1

    if number_list != []:
        for number in number_list:
            mult_numbers *= number
        return mult_numbers
    else:
        return 1

    # Took about 2-3 minutes because the previous one helped


def join_strings(word_list):
    """Return a string of all input strings joined together.

    Python has a built-in method on lists, `join`---but for this exercise, you
    should not use it.

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string:

        >>> join_strings([])
        ''

    """

    join_strings = ""
    
    if word_list != []:
        for word in word_list:
            join_strings += word
        return join_strings
    else:
        return ''

    # Gave up to return to later, which then took about 5-10 minutes


def average(number_list):
    """Return the average (mean) of the list of numbers given.

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty. It's fine if
    this raises an error when given an empty list.
    """

    if number_list != []:
        sum_numbers = 0
        mean = 0
        for number in number_list:
            sum_numbers += number
        input_count = len(number_list)
        mean = float(sum_numbers) / float(input_count)
        return mean
    else:
        return "You gotta give me numbers bruh"

    # Cam back after 5-10 min, then took about 5-10 more minutes to finish

def join_strings_with_comma(list_of_words):
    """Return ['list', 'of', 'words'] like "list, of, words".

        >>> join_strings_with_comma(["Labrador", "Poodle", "French Bulldog"])
        'Labrador, Poodle, French Bulldog'

    If there's only one thing in the list, it should return just that
    thing, of course:

        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'

    """

    join_strings_with_comma = ""

    if list_of_words != []:
        for word in list_of_words:
            if word == list_of_words[(len(list_of_words)-1)]: # I'd say this was the hardest part!
                join_strings_with_comma += word              
            else:
                join_strings_with_comma += word
                join_strings_with_comma += ", "
        return join_strings_with_comma
    else:
        return ''

    # Gave up to return to later, which then took about 10-20 minutes



##############################################################################
# END OF ASSIGNMENT: You can ignore everything below.


if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "*** %s TESTS PASSED. GOOD WORK!" % result.attempted
    print
