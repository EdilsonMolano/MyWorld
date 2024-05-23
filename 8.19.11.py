import sys

def test(did_pass):
    """ Print the result of a test."""
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def count(sub, word):
    count = 0
    if sub in word:
        for m in range(len(word)):
            new_word = ""
            for n in range(len(sub)):
                if m + n >= len(word): break
                new_word += word[m + n]
            if new_word == sub:
                count += 1
    return(count)

def test_suite():
    """ Run the suite of tests for code in this module (this file)
    """
    test(count("is", "Mississippi") == 2)
    test(count("an", "banana") == 2)
    test(count("ana", "banana") == 2)
    test(count("nana", "banana") == 1)
    test(count("nanan", "banana") == 0)
    test(count("aaa", "aaaaaa") == 4)

test_suite()
    
print(count("is", "Mississipi"))