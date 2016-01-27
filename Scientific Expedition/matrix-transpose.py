"""
 In linear algebra, the transpose of a matrix A is another matrix AT (also written A′, Atr,tA or At) created by any one of the following equivalent actions:

    reflect A over its main diagonal (which runs from top-left to bottom-right) to obtain AT
    write the rows of A as the columns of AT
    write the columns of A as the rows of AT

Formally, the ith row, jth column element of AT is the jth row, ith column element of A:

[AT]i j = [A]j i

If A is an m × n matrix then AT is an n × m matrix.

You have been given a matrix as a 2D list with integers. Your task is to return a transposed matrix based on input.

transposed-matrix

Input: A matrix as a list of lists with integers.

Output: The transposed matrix as a list/tuple of lists/tuples with integers.

Precondition:
0 < len(matrix) < 10
all(0 < len(row) < 10 for row in matrix) 
"""

eckio(data):
    if data:
        print(len(data[0]))
        result = [[0 for i in range(len(data))] for i in range(len(data[0]))]
        
    for i in range(len(data)):
        for j in range(len(data[i])):
            result[j][i] = data[i][j]
    
    
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert isinstance(checkio([[0]]).pop(), list) is True, "Match types"
    assert checkio([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]) == [[1, 4, 7],
                                    [2, 5, 8],
                                    [3, 6, 9]], "Square matrix"
    assert checkio([[1, 4, 3],
                    [8, 2, 6],
                    [7, 8, 3],
                    [4, 9, 6],
                    [7, 8, 1]]) == [[1, 8, 7, 4, 7],
                                    [4, 2, 8, 9, 8],
                                    [3, 6, 3, 6, 1]], "Rectangle matrix"

