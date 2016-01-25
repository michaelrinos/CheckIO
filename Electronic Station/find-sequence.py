"""
 You are given a matrix of NxN (4≤N≤10). You should check if there is a sequence of 4 or more matching digits. The sequence may be positioned horizontally, vertically or diagonally (NW-SE or NE-SW diagonals).
find-sequence

Input: A matrix as a list of lists with integers.

Output: Whether or not a sequence exists as a boolean.

Precondition:
0 ≤ len(matrix) ≤ 10
all(all(0 < x < 10 for x in row) for row in matrix) 

"""

def recurse(matrix, num, i, j, a, b):
    try:
        
        
        
                return True
                
    except IndexError:
        return False
    return False

def checkio(matrix):
    count = 1
    num = -1
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):                     #We give the first point
            num = matrix[i][j]
            for a in range(-1,2):                           #We check the immediate neighbors
                for b in range(-1,2):                       #We skip checking ourselves
                    if a == 0 and b == 0:
                        continue
                    else:
                        try:
                            if matrix[i+a][j+b] == num:
                                if i < 3 and a < 0 or  j < 3 and b < 0:         #Because of negative indexing
                                    continue
                                    
                                if recurse(matrix, num, i, j, a, b):  #I check non-imediate neighbors
                                    if matrix[i+(2*a)][j+(2*b)] == num:
                                        if matrix[i+(3*a)][j+(3*b)] == num:
                                            return True
                        except IndexError:
                            continue
    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
    
    assert checkio([
        [2,6,2,2,7,6,5],
        [3,4,8,7,7,3,6],
        [6,7,3,1,2,4,1],
        [2,5,7,6,3,2,2],
        [3,4,3,2,7,5,6],
        [8,4,6,5,2,9,7],
        [5,8,3,1,3,7,8]
        ]) == False, "Ballz"
    
    assert checkio([
        [1,9,7,8,9,3,6,5,6,2],
        [4,9,4,8,3,4,8,8,5,9],
        [2,8,5,5,7,8,6,1,3,6],
        [6,4,7,6,9,1,4,5,7,8],
        [4,7,7,9,8,8,8,8,4,4],
        [3,7,3,2,1,9,1,8,9,1],
        [4,7,2,4,8,1,2,3,6,2],
        [4,4,1,3,3,3,9,2,6,7],
        [8,6,1,9,3,5,8,1,7,5],
        [7,3,6,5,3,6,6,4,8,2]
    ]) == True, "Diagonal"


