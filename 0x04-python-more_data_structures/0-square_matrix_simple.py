def square_matrix_simple(matrix=[]):
    square_matrix = []
    for i in matrix:
        row = list(map(lambda num: num**2, i))
        square_matrix.append(row)
    return square_matrix
