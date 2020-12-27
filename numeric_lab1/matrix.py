def main():
    matrix = [[8.3, 3.2, 4.1, 1.9],
              [3.92, 8.45, 7.2, 2.46],
              [3.77, 7.79, 8.04, 2.28],
              [2.21, 3.07, 1.69, 6.69]]
    matrix_l = [[0 for _ in range(4)] for _ in range(4)]
    matrix_u = [[0 for _ in range(4)] for _ in range(4)]
    matrix_b = [-10.23, 12.21, 15.03, -8.35]
    matrix_y = [0, 0, 0, 0]
    matrix_x = [0, 0, 0, 0]


    for k in range(0, 4):
        for i in range(k, 4):
            matrix_l[i][k] = matrix[i][k] - sum([matrix_l[i][m] * matrix_u[m][k] for m in range(0, k - 1)])
        for j in range(k + 1, 4):
            matrix_u[k][j] = (matrix[k][j] - sum([matrix_l[k][m] * matrix_u[m][j] for m in
                              range(0, k - 1)])) / matrix_l[k][k]

    matrix_y[0] = matrix_b[0] / matrix_l[0][0]
    for i in range(1, 4):
        matrix_y[i] = (matrix_b[i] - sum([matrix_l[i][m] * matrix_y[m] for m in range(0, k - 1)])) / matrix_l[i][i]

    matrix_x[3] = matrix_y[3]
    for i in reversed(range(0, 3)):
        matrix_x[i] = (matrix_y[i] - sum([matrix_u[i][m] * matrix_x[m] for m in range(i + 1, 4)])) / matrix_l[i][i]


    return matrix_x

    def read_input():
        matrix_a = [[]]
        matrix_b = [[]]
        for i in range(4):
            matrix_b[i] = float(input("Enter element for matrix B: "))
            for j in range(4):
                matrix_a[i][j] = float(input("Enter element for matrix A: "))



if __name__ == '__main__':
    matrix_x = main()
    k = 20
    p = 21
    s = 0.02 * k
    B = 0.02 * p

    a = [[8.3, 2.62 + s, 4.1, 1.9],
         [3.92, 8.45, 7.78 - s, 2.46],
         [3.77, 7.21 + s, 8.04, 2.28],
         [2.21, 3.65 - s, 1.69, 6.69]]

    b = [-10.65 + B, 12.21, 15.45 - B, -8.35]

    print(matrix_x)
    print(a)

    sums = []
    for equation in a:
        sum = 0
        for iterator in range(len(equation)):
            sum += equation[iterator] * matrix_x[iterator]
        sums.append(sum)
    print(sums)
    print(b)


