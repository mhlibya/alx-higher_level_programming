def square_matrix_simple(matrix=[]):
    square_matrix = []
    for i in range(len(matrix)):
        row = list(map(square, matrix[i]))
        square_matrix.append(row)
    return square_matrix
def square(i):
    return i**2
