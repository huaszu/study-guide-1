"""List Practice
Edit the functions until all of the doctests pass when
you run this file.
"""


def print_list(items):
    """Print each item in the input list.
    
    For example::
    
        >>> print_list([1, 2, 6, 3, 9])
        1
        2
        6
        3
        9
    """

    for element in items:
        print(element)


def long_words(words):
    """Return words in input list that longer than 4 characters.
    
    For example::
    
        >>> long_words(["hello", "a", "b", "hi", "muffin", "muffin"])
        ['hello', 'muffin', 'muffin']
    
    (If there are duplicates, show both --- notice "muffin" appears
    twice in output)
    
    If no words are longer than 4 characters, return an empty list::
    
        >>> long_words(["all", "are", "tiny"])
        []
    """

    long_words_list = []
    
    for word in words:
        if len(word) > 4:
            long_words_list.append(word)

    return long_words_list


def n_long_words(words, n):
    """Return words in list longer than `n` characters.
    
    For example::
    
        >>> n_long_words(
        ...     ["hello", "hey", "spam", "spam", "muffin", "muffin"],
        ...     3
        ... )
        ['hello', 'spam', 'spam', 'muffin', 'muffin']
        >>> n_long_words(["I", "like", "apples", "bananas", "you"], 5)
        ['apples', 'bananas']
    """

    n_long_words_list = []

    for word in words:
        if len(word) > n:
            n_long_words_list.append(word)

    return n_long_words_list


def smallest_int(numbers):
    """Find the smallest integer in a list of integers and return it.
    **DO NOT USE** the built-in function `min()`!
    
    For example::
    
        >>> smallest_int([-5, 2, -5, 7])
        -5
        >>> smallest_int([3, 7, 2, 8, 4])
        2
    
    If the input list is empty, return `None`::
    
        >>> smallest_int([]) is None
        True
    """
    
    smallest_number = None

    for number in numbers:
        if smallest_number is None or number < smallest_number:
        # Order matters. `if number < smallest_number or smallest_number is None:` led to an error.
            smallest_number = number

    return smallest_number


def largest_int(numbers):
    """Find the largest integer in a list of integers and return it.
    **DO NOT USE** the built-in function `max()`!
    
    For example::
    
        >>> largest_int([-5, 2, -5, 7])
        7
        >>> largest_int([3, 7, 2, 8, 4])
        8
    
    If the input list is empty, return None::
    
        >>> largest_int([]) is None
        True
    """

    largest_number = None

    for number in numbers:
        if largest_number is None or number > largest_number:
            largest_number = number

    return largest_number


def halvesies(numbers):
    """Return list of numbers from input list, each divided by two.
    
    For example::
    
        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]
   
    If any of the numbers are odd, make sure you don't round off
    the half::
   
        >>> halvesies([1, 5])
        [0.5, 2.5]
    """

    halved = []
    
    for number in numbers:
        halved.append(number / 2)

    return halved


def word_lengths(words):
    """Return the length of words in the input list.
    
    For example::
    
        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]
    """
    
    lengths = []

    for word in words:
        lengths.append(len(word))

    return lengths


def sum_numbers(numbers):
    """Return the sum of all of the numbers in the list.
    Python has a built-in function, `sum()`, which already does
    this --- but for this exercise, you should not use it.
    
    For example::
    
        >>> sum_numbers([1, 2, 3, 10])
        16
    
    Any empty list should return the sum of zero::
    
        >>> sum_numbers([])
        0
    """

    total = 0

    for number in numbers: 
        total = total + number
    
    return total


def mult_numbers(numbers):
    """Return product (result of multiplication) of numbers in list.
    
    For example::
    
        >>> mult_numbers([1, 2, 3])
        6
    
    Obviously, if there is a zero in input, the product is zero::
    
        >>> mult_numbers([10, 20, 0, 50])
        0
    
    As explained at http://en.wikipedia.org/wiki/Empty_product,
    if the list is empty, the product should be 1::
    
        >>> mult_numbers([])
        1
    """

    product = 1

    # How to have function return 0 quicker if 0 exists in the list?
    # What if the list contains 0.0?  Or 0.00?  The function should return 0.
    # Will `if 0 in numbers` help us know if 0.0 is in the list?
    # if 0 in numbers:
    #     product = 0
    #     return product 
    
    for number in numbers:
        product = product * number
    
    return product


def join_strings(words):
    """Return a string of all input strings joined together.
    Python has a built-in method, `list.join()` --- but for
    this exercise, **you should not use it**.
    
    For example::
    
        >>> join_strings(["spam", "spam", "muffin", "balloonicorn"])
        'spamspammuffinballoonicorn'
    
    For an empty list, you should return an empty string::
    
        >>> join_strings([])
        ''
    """

    joint_string = ""

    for word in words:
        joint_string = joint_string + word
    
    return joint_string


def average(numbers):
    """Return the average (mean) of the list of numbers given.
    
    For example::
    
        >>> average([2, 4])
        3.0
    
    This should handle cases where the result isn't an integer::
    
        >>> average([2, 12, 3])
        5.666666666666667
    
    There is no defined answer if the list given is empty;
    it's fine if this raises an error when given an empty list.
    (Think of the best way to handle an empty input list, though,
    a feel free to provide a good solution here.)
    """

    empty_list = []
    
    if numbers == empty_list:
        return(print("Please provide a list of numbers."))
        # Wrote return the print statement so that user not only sees the
        # error message printed, but we also end the execution of the
        # function.  We should not proceed to the next line of code, which
        # would raise an error because len(numbers) would be 0.

    return sum_numbers(numbers) / len(numbers)


def join_strings_with_comma(words):
    """Return ['list', 'of', 'words'] like "list, of, words".
    
    For example::
     
        >>> join_strings_with_comma(
        ...     ["Labrador", "Poodle", "French Bulldog"]
        ...     )
        'Labrador, Poodle, French Bulldog'
    
    If there's only one thing in the list, it should return just that
    thing, of course::
   
        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'
    """

    string_with_comma = ""

    for word in words:
        if string_with_comma == "":
            string_with_comma = word
        else:
            string_with_comma = string_with_comma + ", " + word
    
    return string_with_comma


def reverse_list(items):
    """Return the input list, reversed.
    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.
    
    For example::
    
        >>> reverse_list([1, 2, 3])
        [3, 2, 1]
        >>> reverse_list(["cookies", "love", "I"])
        ['I', 'love', 'cookies']
    
    You should do this without changing the original list::
    
        >>> orig = ["apple", "berry", "cherry"]
        >>> reverse_list(orig)
        ['cherry', 'berry', 'apple']
        >>> orig
        ['apple', 'berry', 'cherry']
    """

    reversed_list = []
    position = -1
    
    for element in items:
        reversed_list.append(items[position])
        position = position - 1
    
    return reversed_list
    
#   Above is simpler because we don't have to use `-abs()`.  `position` is a
#   better variable name for the concept at hand. 

#   count = 1

#     for element in items:
#         reversed_list.append(items[-abs(count)])
#         count = count + 1  

    # Alternative:
    # return items [::-1]

    # Alternative:
    # reversed_list = []

    # for i in range(len(items), 0):
    #     reversed_list.append(items[i-1])
    
    # return reversed_list

    # Considered another solution of creating another list that has the
    # same elements as items, in the same order.  Then move elements within 
    # this other list such that the order becomes reversed.  Seems
    # inefficient, versus populating another list from the get-go with
    # elements in the desired reversed order. 


def reverse_list_in_place(items):
    """Reverse the input list `in place`.
    Reverse the input list given, but do it "in place" --- that is,
    do not create a new list and return it, but modify the original
    list.
    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.
    
    For example::
    
        >>> orig = [1, 2, 3]
        >>> reverse_list_in_place(orig)
        >>> orig
        [3, 2, 1]
        >>> orig = ["cookies", "love", "I"]
        >>> reverse_list_in_place(orig)
        >>> orig
        ['I', 'love', 'cookies']
    """
    
    # position = 0
    # stored_element = None
    # position_to_place_stored_element = -1 - position
  
    # for element in items:
    #     if position >= int(len(items) / 2): # Remembering that int rounds down
    #         break
    #     stored_element = items[position] # Store this element for later use
    #     # because we are about to put another element at the index where
    #     # this element currently is.  Example: orig = ["a", "b", "c", "d"].
    #     # Assign stored_element to "a"
    #     items[position] = items[position_to_place_stored_element] # Example: 
    #     # orig now looks like ["d", "b", "c", "d"]
    #     items[position_to_place_stored_element] = stored_element # Example: 
    #     # orig now looks like ["d", "b", "c", "a"].  Through these steps, we
    #     # swapped "a" and "d".  In the next iteration, let's swap "b" and "c"
    #     position = position + 1
    #     # The if statement in the for loop is so that we stop making swaps
    #     # once we have already made swaps for all respective pairings on 
    #     # either side of the middle of the input list, at which point our 
    #     # input list has been reversed. 

    # Better written solution:
    for i in range(len(items) // 2): # Note A: if len(items) / 2 evaluates to
        # 2.5, for example, 2 will be the last number in the range because
        # range() increments by 1 by default and stops before 2.5
        # Note B: error message if we have `for i in range(len(items) / 2)`:
        # `TypeError: 'float' object cannot be interpreted as an integer`.
        # range() works with integers.  Let's do integer division instead, 
        # which rounds down by the way. 
        position_to_place_stored_element = (i + 1) * -1 # `position` and
        # `position_to_place_stored_element` respectively give us the index of
        # each element in the pairing we intend to make a swap        
        stored_element = items[i] 
        items[i] = items[position_to_place_stored_element] 
        items[position_to_place_stored_element] = stored_element 

    # return items
    # Problem did not say to return anything. 

    # A solution that uses the function reverse_list(items) created above?:
    # items = reverse_list(items)


def duplicates(items):
    """Return list of words from input list which were duplicates.
    Return a list of words which are duplicated in the input list.
    The returned list should be in ascending order.
   
    For example::
   
        >>> duplicates(
        ...     ["apple", "banana", "banana", "cherry", "apple"]
        ... )
        ['apple', 'banana']
        >>> duplicates([1, 2, 2, 4, 4, 4, 7])
        [2, 4]
   
    You should do this without changing the original list::
   
        >>> orig = ["apple", "apple", "berry"]
        >>> duplicates(orig)
        ['apple']
        >>> orig
        ['apple', 'apple', 'berry']
    """

    dups = []

    items = sorted(items)

    for i in range(len(items) - 1):
        if items[i] == items[i + 1]:
            if items[i] not in dups:
                dups.append(items[i])

    return dups

    # Alternative:
    
    # dups = []
    # counts_of_elements = dict()

    # for element in items:
    #     counts_of_elements[element] = counts_of_elements.get(element, 0) + 1

    # for key, value in counts_of_elements.items():
    #     if value > 1:
    #         dups.append(key)
    
    # return dups

def find_letter_indices(words, letter):
    """Return list of indices where letter appears in each word.
    Given a list of words and a letter, return a list of integers
    that correspond to the index of the first occurrence of the letter
    in that word.
    **DO NOT** use the `list.index()` method.
    
    For example::
    
        >>> find_letter_indices(['odd', 'dog', 'who'], 'o')
        [0, 1, 2]
    
    ("o" is at index 0 in "odd", is at index 1 in "dog", and at
    index 2 in "who")
    
    If the letter doesn't occur in one of the words, use `None` for
    that word in the output list. For example::
    
        >>> find_letter_indices(['odd', 'dog', 'who', 'jumps'], 'o')
        [0, 1, 2, None]
    
    ("o" does not appear in "jumps", so the result for that input is
    `None`.)
    """

    letter_indices = []
    
    for word in words:
        letter_index = None
        for i in range(len(word)):
            if word[i] == letter:
                letter_index = i
                break
        letter_indices.append(letter_index) 

    return letter_indices


#####################################################################
# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print("\nALL TESTS PASSED. GOOD WORK!\n")