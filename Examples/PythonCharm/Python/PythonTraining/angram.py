def is_anagram(a_word, b_word):
    return sorted(a_word) == sorted(b_word)


def test_anagram():
    # print('## Start test ##')
    #
    # assert is_anagram("abc", "acb")
    # assert is_anagram("silent", "listen")
    # assert is_anagram('abc','bbc')
    # assert not is_anagram("one", "two")
    a = "abcde"
    b= "edcba"
    l = len(a) - 1

    for char in a :
        assert len(a) == len(b)
        index = a.index(char)
        char_from_b = b[l-index]
        assert char_from_b == char , "one or more letter is not as ingram"