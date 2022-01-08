# String of each vowel
vowels = "aeiou"
ip_str = "Hello, welcome at wecodeinpython"
# Make it suitable for caseless comparisons
ip_str = ip_str.casefold()
# Make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels,0)
# count the vowels
for char in ip_str:
    if char in count:
        count[char] += 1
print(count)