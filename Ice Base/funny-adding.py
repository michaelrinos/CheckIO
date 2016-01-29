"""
We have an array of two positive integers. Add these two numbers together.

Input: A list of two elements. Each element is a positive integer.

Output: The sum of two numbers.
"""

def checkio(data):
    return sum(data)
    
if __name__ == '__main__':
    assert checkio([5, 5]) == 10, 'First'
    assert checkio([7, 1]) == 8, 'Second'
    print('All ok')
