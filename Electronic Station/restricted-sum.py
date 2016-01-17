"""
 Our new calculator is censored and as such it does not accept certain words. You should try to trick by writing a program to calculate the sum of numbers.

Given a list of numbers, you should find the sum of these numbers. Your solution should not contain any of the banned words, even as a part of another word.

The list of banned words are as follows:

    sum
    import
    for
    while
    reduce

Input: A list of numbers.

Output: The sum of numbers.

Precondition: The small amount of data. Let's creativity win! 
"""

def recursive(data, i_cant_be_named_s_u_m):
    if not data:
        return i_cant_be_named_s_u_m
    else:
        i_cant_be_named_s_u_m += data.pop()
        return recursive(data, i_cant_be_named_s_u_m)
    
def checkio(data):
    return recursive(data,0)

if __name__ == '__main__':
	assert checkio([43,-10,68,84,91,71,-10,-80,38]) == 295
	assert checkio([42])  == 42
	assert checkio([96,26,54,21,4]) == 201
	assert checkio([1,37,-64,57,-78,57,64,-38,-91,61,53,-89,41]) == 11
	assert checkio([42,-24,-74,96,-62,5,-47])  == -64

