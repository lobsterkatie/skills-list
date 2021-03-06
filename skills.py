"""Skills Assessment: Lists.

To work on an item, uncomment the entire function (including the docstring)
and then run this script. It should output an error that the newly-uncommented
function is now failing its tests.

Edit the function body until you have a solution and the test passes, and then
move on to the next function.

This assessment is DUE TO YOUR ADVISOR BY SUNDAY EVENING.
"""


def all_odd(number_list):
    """Return a list of only the odd numbers in the input list.

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []

    """

    odds = []

    for num in number_list:
        if (num % 2) == 1:
            odds.append(num)

    return odds


def all_even(number_list):
    """Return a list of only the even numbers in the input list.

        >>> all_even([2, 6, -1, -2])
        [2, 6, -2]

        >>> all_even([-1, 3, 5])
        []

    """

    evens = []

    for num in number_list:
        if (num % 2) == 0:
            evens.append(num)

    return evens


def print_indeces(my_list):
    """Print the index of each list item, followed by the item itself.
    Do this without using a counting variable. I.e. don't do something
    like this:

    count = 0
    for item in list:
        print count
        count = count + 1

    Output should look like this:

    >>> print_indeces(["Toyota", "Jeep", "Volvo"])
    0 Toyota
    1 Jeep
    2 Volvo

    """

    for i, item in enumerate(my_list):
        print i, item

    #not sure if using an enumeration is cheating, however, so if I were going
    #to do it just with lists I'd go all Java on you and do:

    # for i in range(len(my_list)):
    #     print i, my_list[i]


def long_words(word_list):
    """Return all words in input list that are longer than 4 characters.

        >>> long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

        >>> long_words(["all", "are", "tiny"])
        []

    """

    at_least_five = []

    for word in word_list:
        if len(word) >= 5:
            at_least_five.append(word)

    return at_least_five


def smallest_int(number_list):
    """Find the smallest integer in a list of integers and return it.

        >>> smallest_int([-5, 2, -5, 7])
        -5

    If the input list is empty, return None:

        >>> smallest_int([]) is None
        True

    """

    if len(number_list) == 0:
        return None

    # I get that an 'else' is not strictly necessary here (since this part of the
    # code will never be hit if we're passed an empty list), but IMHO it makes it
    # just a micron clearer/easier to read because the else makes that explicit
    else:
        smallest_so_far = number_list[0]

        for num in number_list:
            if num < smallest_so_far:
                smallest_so_far = num

        return smallest_so_far  # now smallest_over_all!


def largest_int(number_list):
    """Find the largest integer in a list of integers and return it.

        >>> largest_int([-5, 2, -5, 7])
        7

    If the input list is empty, return None:

        >>> largest_int([]) is None
        True

    """

    if len(number_list) == 0:
        return None

    # same caveat with the 'else' as above
    else:
        biggest_so_far = number_list[0]

        for num in number_list:
            if num > biggest_so_far:
                biggest_so_far = num

        return biggest_so_far  # now biggest_over_all!


def halvesies(number_list):
    """Return list of numbers from input list, each divided by two.

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are, make sure you don't round off the half:

        >>> halvesies([1, 5])
        [0.5, 2.5]

    """

    halves = []

    for num in number_list:
        half = num / 2.0
        halves.append(half)

    return halves


def word_lengths(word_list):
    """Return the length of words in the input list.

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]

    """

    lengths = []

    for word in word_list:
        lengths.append(len(word))

    return lengths


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

    if len(number_list) == 0:
        return 0

    # same caveat with the 'else' as above
    else:
        return reduce(lambda x, y: x + y, number_list)

        # hey, it worked! (to be fair, it's the example in the documentation)
        # but again, if that's cheating, here you go:

        # running_total = 0

        # for num in number_list:
        #     running_total += num

        # return running_total


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

    if len(number_list) == 0:
        return 1

    # same caveat with the 'else' as above
    else:
        return reduce(lambda x, y: x * y, number_list)

        # hey, it worked again!
        # but as before, if that's cheating, here you go:

        # running_product = 1

        # for num in number_list:
        #     running_product *= num

        # return running_product


def join_strings(word_list):
    """Return a string of all input strings joined together.

    Python has a built-in method on lists, `join` -- but this exercise, you
    should not use it.

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string:

        >>> join_strings([])
        ''

    """

    if len(word_list) == 0:
        return ""

    # same caveat with the 'else' as above
    else:
        return reduce(lambda x, y: x + y, word_list)

        # cool! and here's the other version:

        # german_word = ""  # because that's how they seem to make words

        # for word in word_list:
        #     german_word += word

        # return german_word


def average(number_list):
    """Return the average (mean) of the list of numbers given.

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty. It's fine if
    this raises an error when given an empty list.
    """

    if len(number_list) == 0:
        return "That list is empty!"

    # same caveat with the 'else' as above
    else:
        return (float(sum_numbers(number_list)) / len(number_list))

        # again, don't know if that's cheating, so...

        # running_total = 0

        # for num in number_list:
        #     running_total += num

        # return (float(running_total) / len(number_list))


#############################################################################
# END OF SKILLS TEST: You can stop here, or read on to work on advanced problem.

# Uncomment the function below to work on the advanced problem.
# Tip: To comment or uncomment blocks of code, highlight what you want to
#    comment or uncomment, and then CMD+"/" or CTRL-"/"

def advanced_join_strings(list_of_words):
    """Return a single string with each word from the input list
    separated by a comma.

        >>> advanced_join_strings(["Labrador", "Poodle", "French Bulldog"])
        'Labrador, Poodle, French Bulldog'

    If there's only one thing in the list, it should return just that
    thing, of course:

        >>> advanced_join_strings(["Pretzel"])
        'Pretzel'

    """

    if len(list_of_words) == 0:
        return ""

    # same caveat with the 'elif' as the 'else's above
    elif len(list_of_words) == 1:
        return list_of_words[0]

    else:
        return reduce(lambda x, y: x + ", " + y, list_of_words)

        # okay, I don't know if real programmers consider this reduce-with-a-
        # lambda-function business a party trick, but I like it!

        # in any case, here's the other version:

        # csv_string = list_of_words.pop(0)

        # for word in list_of_words:
        #     csv_string += ", "
        #     csv_string += word

        # return csv_string


# END OF ASSIGNMENT: You can ignore everything below.
##############################################################################

if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "*** %s TESTS PASSED. GOOD WORK!" % result.attempted
    print
