

small_words = ('into', 'the', 'a', 'of', 'at', 'in', 'for', 'on')

def book_title(title):
    """ Takes a string and returns a title-case string.
    All words EXCEPT for small words are made title case
    unless the string starts with a preposition, in which
    case the word is correctly capitalized.

    >>> book_title('DIVE Into python')
    'Dive into Python'

    >>> book_title('the great gatsby')
    'The Great Gatsby'

    >>> book_title('the WORKS OF AleXANDer dumas')
    'The Works of Alexander Dumas'
    """
 # Extract the input list of words into a list

    lst_of_words = title.lower().split()

 # Capitalize the first word of the list and insert it into the new_title list 
    cap = lst_of_words[0]
    lst_of_words[0] = cap.capitalize()
  
    new_title = lst_of_words.pop(0)

# Loop through the words in the lst list and compare them to the defined small words. If true write them to the new_title list
# If not true capitalize the word and write it to the new_title list

    for word in lst_of_words:
        if word in small_words:
            new_title = new_title + ' '
            new_title = new_title + word
            
        else:
            new_title = new_title + ' '
            new_title = new_title + word[0].upper()
            new_title = new_title + word[1:]

    return new_title
            
def _test():
    import doctest, refactory
    return doctest.testmod(refactory)

if __name__ == "__main__":
    _test()