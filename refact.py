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
    lst_of_words = title.lower().split()
    print (lst_of_words)
    print (lst_of_words[0])
    cap = lst_of_words[0]
    lst_of_words[0] = cap.capitalize()


   # num_of_words = len(lst_of_words)
   # if num_of_words < 1:
   #     return ''

  #  test = lst_of_words.upper(0)
  #  print (test)

    #new_title = lst_of_words.pop(0)
    #print (new_title)
    #new_title = new_title[0].upper() + new_title[1:]
    #print (new_title)
    new_title = lst_of_words.pop(0)
    # tpl_of_words = tuple(lst_of_words)

    # print (tpl_of_words)

    for word in lst_of_words:
        if word in small_words:
            new_title = new_title + ' '
            new_title = new_title + word
            
        else:
            new_title = new_title + ' '
            new_title = new_title + word[0].upper()
            new_title = new_title + word[1:]


    #for word in tpl_of_words:
    #    prep_word = False
    #    for prep in small_words:
    #        if prep == word:
    #            new_title = new_title + ' '
    #            new_title = new_title + word
    #            prep_word = True
    #            break
    #    if prep_word == True:
     #       continue
     #   new_title = new_title + ' '
     #   new_title = new_title + word[0].upper()
     #   new_title = new_title + word[1:]
        print (new_title)

# def _test():
 #   import refactory
  #  return doctest.testmod(refactory)

if __name__ == "__main__":
    book_title("the WORKS OF AleXANDer dumas")