#Functions with mysterious names/variables given to us in class
#Our job is to figure out what the functions do and write docstrings


def round_to_int(number):
    
    """Takes argument number as any numerical type"""
    """Rounds argument to the nearest integer"""

    number_as_int = int(number)
    if number_as_int - number >= 0.5:
        return number_as_int+1
    else:
        return number_as_int


def count_lines(text):

    """Takes a string, text"""
    """Returns the number of lines in the text"""

    if not text:
        return 0
    counter = 1
    for character in text:
        if character == "\n":
           counter  += 1    
    return counter


def pythagorean(a, b):

    """Take two numbers that represent shorter two sides of a triangle"""
    """Calculates and returns the length of the hypotenuse"""
    """Can be used to calculate distance between a and b, if a and b represent the distance from the origin"""

    c = a * a + b * b
    return Math.sqrt(c)


def reverse(string):

    """Take either a string or a list"""
    """Reverse the order and return it"""

    length_of_string = len(string)
    for pos in range(len(string)/2):
        temp = string[pos]
        string[pos] = string[length_of_string - pos - 1]
        string[length_of_string - pos - 1] = temp

    return string


def count_words():

    """Opens a text file"""
    """Creates a dictionary of all the distinct words, and counts how many times each occurs"""
    """Prints out the word count, for each word"""

    my_file = open("sample_input.txt")
    list_of_words = my_file.split()
    word_count = dict()
    for word in list_of_words:        
        current_count = word_count.get(word, 0)
        current_count += 1
        word_count[word] = current_count
    
    for k, v in word_count.iteritems():
        print "%s:\t%d"%(k, v)


def sort_smallest_to_largest(ls):

    """Takes a list of numbers or letters"""
    """Sorts it in order from smallest to largest"""
    """Doesn't return anything, just modifies the original list"""

    swapped = True
    while swapped == True:
        swapped = False
        for i in range(len(ls)-1):
            if ls[i] > ls[i+1]:
                temp = ls[i]
                ls[i] = ls[i+1]
                ls[i+1] = temp
                swapped = True

def fibonacci(n):
    """Takes a number n as input"""
    """Calculates the nth Fibonacci number and returns it"""

    a, b = 0, 1
    for i in range(n): #input is a number
        a, b = b, a + b
    return a 


def fibonacci2(n):  
    """Takes a number n as input"""
    """Calculates the nth Fibonacci number and returns it"""
    """Uses recursion to calculate the nth fibonacci number; alternative to fibonacci()"""

    if n <= 0:    #if n is negative return 0
        return 0
    if n == 1:      # if n is 1 return 1
        return 1
    return fibonacci2(n - 1) + fibonacci2(n - 2)


def compare_strings(string1, string2):
    
    """Takes two strings"""
    """Compares all the characters in the strings"""
    """If strings match, return True. If strings do not match, return False"""

    if len(string1) == len(string2):
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                return False
        return True
    return False



def combine_dictionaries(dict1, dict2):
    """Takes two dictionaries"""
    """Creates a third combined dictionary"""
    """Fills the combined dictionary with keys that exist in both dict1 and dict2"""
    """Sums the occurrences of the matching keys across both dict1 and dict2"""
    """Returns the combined dictionary"""

    combined = {}
    for k, v in dict1.items():
        if k in dict2:
            combined[k] = v + dict2[k]
    return combined


def create_alphabetical_index(word_list):

    """Takes a list of words"""
    """Creates a new dictionary
            key = the first letter of all the words
            value = all the words that have those first letters, stored as a list"""
    """Returns the dictionary"""

    outp = {}
    for word in word_list:
        if word: #if s is not null or True
            outp.setdefault(word[0], []).append(word)
    return outp


def find_palindrome(inp):

    """Takes inp which is a string or a sentence"""
    """Searches for the longest palindrome in the inp, and returns it"""

    best_i, best_j = 0, 0
    for i in range(len(inp)):
        for j in range(len(inp), i, -1):
            if inp[i:j] == inp[i:j][::-1]:
                if j - i > best_j - best_i:
                    best_i = i
                    best_j = j
    return inp[best_i:best_j]


def binary_search(mylist, item):

    """Takes a list, which must be sorted in ascending order"""
    """Checks to see if item is in the list, using a binary search algorithm"""

    while len(mylist) > 1:
        if item == mylist[len(mylist) / 2]:
            return True
        elif item < mylist[len(mylist) / 2]:
            mylist = mylist[:len(mylist) / 2]
        else:
            mylist = mylist[len(mylist) / 2 + 1:]

    return len(mylist) > 0 and item == mylist[0]



def merge_two_sorted_lists(one, two):

    """Takes two lists sorted in ascending order, called one and two"""
    """Combines the two lists with elements from both lists in ascending order"""
    """Returns the combined list"""

    i, j = 0, 0
    outp = []
    while i < len(one) and j < len(two):
        if one[i] <= two[j]:
            outp.append(one[i])
            i += 1
        if one[i] >= two[j]:
            outp.append(two[j])
            j += 1
    if i < len(one):
        outp.extend(one[i:])
    elif j < len(two):
        outp.extend(two[j:])

    return outp



def merge_sort(inp):

    """Takes a list and sorts it in ascending order"""
    """Uses merge sort algorithm:
            Split list in half
            Sort each half
            Combine the two halves in sorted order
            Do this recursively"""

    if len(inp) < 2:
        return inp

    first_half_sorted = merge_sort(inp[:len(inp) / 2])
    second_half_sorted = merge_sort(inp[len(inp) / 2:])

    return merge_two_sorted_lists(first_half_sorted, second_half_sorted)




