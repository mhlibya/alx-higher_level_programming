def square_matrix_simple(matrix=[]):
    square_matrix = []
    for i in range(len(matrix)):
        row = list(map(lambda num : num**2, matrix[i]))
        square_matrix.append(row)
    return square_matrix
