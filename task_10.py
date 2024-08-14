def count_words(i_string):
    i_string = i_string.lower().translate((str.maketrans('', '', '.,!?,--')))
    words = i_string.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

print(count_words("A man, a plan, a canal -- Panama"))
print(count_words("Doo bee doo bee doo"))