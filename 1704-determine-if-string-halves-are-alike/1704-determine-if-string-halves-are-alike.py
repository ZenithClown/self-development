from collections import Counter

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()  # convert the whole string into lowercase
        
        # let split the string into two halves
        a_ = Counter([s_ for s_ in s[:len(s)//2] if s_ in 'aeiou'])
        b_ = Counter([s_ for s_ in s[len(s)//2:] if s_ in 'aeiou'])
        
        # initial simple check can be performed by
        # checking if the total number of vowels is odd then
        # always return false, else need to check
        # total_vowel = 0
#         for vowel in 'aeiou':
#             # also calculate if the vowel count is
#             # same in both the two string parts
#             num_vowel_in_a = a_.get(vowel, 0)
#             num_vowel_in_b = b_.get(vowel, 0)
#             print(vowel, num_vowel_in_a, num_vowel_in_b)
            
#             if num_vowel_in_a != num_vowel_in_b:
#                 return False
            
#         return True

        return sum(a_.values()) == sum(b_.values())