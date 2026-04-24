s = input("Enter a string: ")

freq = {}

for ch in s:
    if ch in freq:
        freq[ch] = freq[ch] + 1  #here freq[ch] is the current count of the character ch, and we add 1 to it to update the count. Why we use freq[ch]=freq[ch]+1 because freq[ch] is the key and freq[ch]+1 is the value that we want to assign to that key. This way we are updating the count of the character ch in the dictionary freq.
    else:
        freq[ch] = 1

print("Character frequencies:", freq)

# Alternative way to count frequency of characters in a string using set() and count() method.

s = input("Enter a string: ")
for ch in set(s):      #we use set() to get unique characters from the string. This way we can avoid counting the frequency of the same character multiple times.
    print(ch, ":", s.count(ch))