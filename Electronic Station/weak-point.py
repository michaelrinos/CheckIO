"""
 While traveling, the spaceship endures quite a lot of stress. As a result, an important part of the maintenance is to check the outer hull. Stephan uses a digital durabilitimeter for this task. The device scans a portion of the spaceships hull and gives a durability map that is divided by small square fragments with measurements. Sometimes Stephan does not have much time and he can patch only couple points, so we need an algorithm to find the weak points.

The durability map is represented as a matrix with digits. Each number is the durability measurement for the cell. To find the weakest point we should find the weakest row and column. The weakest point is placed in the intersection of these rows and columns. Row (column) durability is a sum of cell durability in that row (column). You should find coordinates of the weakest point (row and column). The first row (column) is 0th row (column). If a section has several equal weak points, then choose the top left point.

weak-point

Input: A durability map as a list of lists with integers.

Output: The coordinates of the weak point as a list (tuple) of integers.

Precondition:
0 < len(matrix) ≤ 10
all(len(row) == len(matrix) for row in matrix)
all(all(0 < x < 10 for x in row) for row in matrix) 
"""


def weak_point(matrix):
    
    length = len(matrix)
    
    lst = [0 for i in range(length*2)]
    
    for i in range(length):
        for j in range(length):
            lst[i] += matrix[j][i]
            lst[i+length] += matrix[i][j]
            
    return lst[length:].index(min(lst[length:])), lst.index(min(lst[0:length]))   # [0, 0]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    #assert isinstance(weak_point([[1]]), (list, tuple)), "The result should be a list or a tuple"
    assert list(weak_point([[7, 2, 7, 2, 8],
                            [2, 9, 4, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [3, 3], "Example"
    assert list(weak_point([[7, 2, 4, 2, 8],
                            [2, 8, 1, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [1, 2], "Two weak point"
    assert list(weak_point([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]])) == [0, 0], "Top left"

