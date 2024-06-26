Revers String

Reverse a string without affecting special characters. Given a string S, containing special characters and all the alphabets, reverse the string without affecting the positions of the special characters.



Input:

A&B
 
Output:

B&A

Explanation: As we ignore '&' and

As we ignore '&' and then reverse, so answer is "B&A".





For example:



Input	Result

A&x#

x&A#



def reverse_string(s):

    s = list(s)

    l, r = 0, len(s) - 1



    while l < r:

        if not s[l].isalpha():

            l += 1

        elif not s[r].isalpha():

            r -= 1

        else:

            s[l], s[r] = s[r], s[l]

            l += 1

            r -= 1



    return ''.join(s)

