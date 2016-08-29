def foo(*args, **kwargs):
  print ("Positional:", args)
  print ("Keywords:", kwargs)

# Postional args only
foo('one', 'two', 'three')

# Keyword args only
foo(a='one', b='two', c='three')


# both Postional and Keyword
foo('one', 'two', c='three', d='four')