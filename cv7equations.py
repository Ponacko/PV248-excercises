import numpy as np


def parse_line(line):
    equation1sides = line.split('=')
    left_side = equation1sides[0].split(' ')
    x = left_side[left_side.index('x') - 1]
    y = left_side[left_side.index('x') - 1]
    right_side = equation1sides[1].strip()
    row = [x, y, right_side]
    return row


a = np.array([[1, 2], [3, 4]])
print('Determinant: ', np.linalg.det(a))
print('Inversion: ', np.linalg.inv(a))
print('Solution: (x,y) = ', np.linalg.solve(a, np.array([1,2])))
firstLine = input('Enter first line:')
secondLine = input('Enter second line:')

row1 = parse_line(firstLine)
row2 = parse_line(secondLine)
matrix = np.array([row1, row2])

print('Solution: (x,y) = ', np.linalg.solve(a, np.array([1,2])))


