pattern = 'abbccbbcc'
# while there is - (e.g -2,-4) the num indicate from the end
print (pattern[-2])
print (pattern[-3])
print (pattern[-2:])
print(pattern[:3])
print(pattern[:-1])
print (pattern.__contains__('bb'))
pattern_to_trim = ' avvv   nnnnn '
pattern_to_trim = pattern_to_trim.strip() # trim
print('$' + pattern_to_trim + '$')
pattern_to_trim = ' avvv   nnnnn '
pattern_to_trim = pattern_to_trim.replace(' ','') # trim
print('$' + pattern_to_trim + '$')