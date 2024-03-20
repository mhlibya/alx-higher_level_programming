def square_matrix_simple(matrix=[]):
    square_matrix = []
    for i in matrix:
        row = map(lambda num: num**2, i)
        square_matrix.append(list(row))
    return square_matrix
