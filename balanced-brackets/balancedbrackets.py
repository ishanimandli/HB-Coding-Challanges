"""Does a given string have balanced pairs of brackets?

Given a string, return True or False depending on whether the string
contains balanced (), {}, [], and/or <>.

Many of the same test cases from Balance Parens apply to the expanded
problem, with the caveat that they must check all types of brackets.

These are fine::

   >>> has_balanced_brackets("<ok>")
   True

   >>> has_balanced_brackets("<{ok}>")
   True

   >>> has_balanced_brackets("<[{(yay)}]>")
   True

These are invalid, since they have too many open brackets::

   >>> has_balanced_brackets("(Oops!){")
   False

   >>> has_balanced_brackets("{[[This has too many open square brackets.]}")
   False

These are invalid, as they close brackets that weren't open::

   >>> has_balanced_brackets(">")
   False

   >>> has_balanced_brackets("(This has {too many} ) closers. )")
   False

Here's a case where the number of brackets opened matches
the number closed, but in the wrong order::

    >>> has_balanced_brackets("<{Not Ok>}")
    False

If you receive a string with no brackets, consider it balanced::

   >>> has_balanced_brackets("No brackets here!")
   True

"""


def has_balanced_brackets(phrase):
    """Does a given string have balanced pairs of brackets?

    Given a string as input, return True or False depending on whether the
    string contains balanced (), {}, [], and/or <>.
    """

    bracket_stack = []
    opening_bracketes = {'(', '[', '{', '<'}
    closing_brackets = {')', ']', '}', '>'}
    for element in phrase:
       if element in opening_bracketes:
          bracket_stack.append(element)
       if element in closing_brackets:
          if not bracket_stack :
             return False
          if element == ')':
             if bracket_stack.pop() is not '(':
                return False
          if element == ']':
             if bracket_stack.pop() is not '[':
                return False
          if element == '}':
             if bracket_stack.pop() is not '{':
                return False
          if element == '>':
             if bracket_stack.pop() is not '<':
                return False
    if bracket_stack:
       return False
    return True

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU CAUGHT ALL THE STRAY BRACKETS!\n")
