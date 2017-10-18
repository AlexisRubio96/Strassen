"""
Ernesto Alejandro Cervantes Villa  A01370793
Jorge Alexis Rubio Sumano   A01372074

Strassen Algorithm Implementation

"""
import csv

"""
****************************File reading************************************
This method takes care of the csv file reading.
Returns a multidimensional array of size [n][n], i.e. a matrix nxn
matrix_reader(file): file = csv file to be read
"""


def matrix_reader(file_name):
    # File read
    # File is open
    with open(file_name, 'r') as csv_file:
        reader = csv.reader(csv_file)
        # Matrix creation
        matrix = []
        row_number = 0
        for row in reader:
            matrix.append([])
            # rowxrow = nxn
            for i in range(len(row)):
                matrix[row_number].append(int(row[i]))
            row_number += 1
    csv_file.close()
    return matrix


"""
****************************File writing***********************************
CSV file writing for the result matrix
"""


def file_writing(file_name):
    global result_matrix_tb
    with open(file_name, 'w') as new_csv:
        writer = csv.writer(new_csv)

        writer.writerows(result_matrix_tb)
        print "File create at " + file_name
    return


"""
****************************Matrix multiplication type 1**************************************
This resolves the first part of the activity(III.1): matrix multiplication defined in any linear algebra text book.
Take both global matrices A and B, and the result matrix of text book.
"""


def text_book_matrix_multiplication():
    global matrixA, matrixB, result_matrix_tb, number_tb_multiplication
    length = len(matrixA)
    for i in range(length):
        result_matrix_tb.append([])
        for j in range(length):
            result_matrix_tb[i].append(0)
            for k in range(length):
                result_matrix_tb[i][j] = result_matrix_tb[i][j] + (matrixA[i][k] * matrixB[k][j])
                number_tb_multiplication += 1  ##Checar la posicion
    return


"""
****************************Matrix multiplication type 2**************************************
This resolves the second part of the activity(III.2): implement the Strassen algorithm for the multiplication of matrices of order n.
It divides in four methods:
    -strassen_algorithm(temp_matrix_a, temp_matrix_b): temp_matrix_a, temp_matrix_b = matrices which will be multiplied. hola
        --THis method is recursive
        --Seven Strassen multiplications
            m1 = (a12-a22) * (b21+b22)
            m2 = (a11+a22) * (b11+b22)
            m3 = (a21-a11) * (b11+b12)
            m4 = (a11+a12) * b22
            m5 = a11 * (b12-b22)
            m6 = a22 * (b12-b11)
            m7 = (a21+a22) * b11
        --Four sums for the resultant matrices
            c11 = m1 + m2 - m4 + m6
            c12 = m4 + m5
            c21 = m6 + m7
            c22 = m2 - m3 + m5 - m7
    -divide_matrix(temp_matrix_a, temp_matrix_b): temp_matrix_a, temp_matrix_b = matrices which will be divided into quarters.
    -matrix_sum(temp_matrix_a, temp_matrix_b): temp_matrix_a, temp_matrix_b = matrices which will be sum.
    -matrix_sub(temp_matrix_a, temp_matrix_b): temp_matrix_a, temp_matrix_b = matrices which will be substract.
"""


def matrix_sum(temp_matrix_a, temp_matrix_b):
    temp_matrix = []
    length = len(temp_matrix_a)
    for i in range(length):
        temp_matrix.append([])
        for j in range(length):
            temp_matrix[i].append(temp_matrix_a[i][j] + temp_matrix_b[i][j])
    return temp_matrix


def matrix_sub(temp_matrix_a, temp_matrix_b):
    temp_matrix = []
    length = len(temp_matrix_a)
    for i in range(length):
        temp_matrix.append([])
        for j in range(length):
            temp_matrix[i].append(temp_matrix_a[i][j] - temp_matrix_b[i][j])

    return temp_matrix


def divide_matrix(temp_matrix, quarter):
    matrix_quarter = []
    length = len(temp_matrix) / 2
    for row in range(length):
        matrix_quarter.append([])
        if quarter == 1:
            matrix_quarter[row] = temp_matrix[row][:len(temp_matrix) / 2]
        if quarter == 2:
            matrix_quarter[row] = temp_matrix[row][len(temp_matrix) / 2:]
        if quarter == 3:
            matrix_quarter[row] = temp_matrix[length + row][:len(temp_matrix) / 2]
        if quarter == 4:
            matrix_quarter[row] = temp_matrix[length + row][len(temp_matrix) / 2:]
    return matrix_quarter


def strassen_algorithm(temp_matrix_a, temp_matrix_b):
    global number_strassen_multiplication
    length = len(temp_matrix_a)

    # Base case 1x1 matrix
    if length == 1:
        matrix_c = [[0]]
        matrix_c[0][0] = temp_matrix_a[0][0] * temp_matrix_b[0][0]
        number_strassen_multiplication += 1     #Checar la posicion
        return matrix_c
    else:
        # Matrices quarters
        a11 = divide_matrix(temp_matrix_a, 1)
        a12 = divide_matrix(temp_matrix_a, 2)
        a21 = divide_matrix(temp_matrix_a, 3)
        a22 = divide_matrix(temp_matrix_a, 4)
        b11 = divide_matrix(temp_matrix_b, 1)
        b12 = divide_matrix(temp_matrix_b, 2)
        b21 = divide_matrix(temp_matrix_b, 3)
        b22 = divide_matrix(temp_matrix_b, 4)

        # Seven multiplications of order n/2, solves recursively  
        m1 = strassen_algorithm(matrix_sub(a12, a22), matrix_sum(b21, b22))
        m2 = strassen_algorithm(matrix_sum(a11, a22), matrix_sum(b11, b22))
        m3 = strassen_algorithm(matrix_sub(a21, a11), matrix_sum(b11, b12))
        m4 = strassen_algorithm(matrix_sum(a11, a12), b22)
        m5 = strassen_algorithm(a11, matrix_sub(b12, b22))
        m6 = strassen_algorithm(a22, matrix_sub(b21, b11))
        m7 = strassen_algorithm(matrix_sum(a21, a22), b11)

        # Matrix sums
        c11 = matrix_sum(matrix_sub(matrix_sum(m2, m6), m4), m1)
        c12 = matrix_sum(m5, m4)
        c21 = matrix_sum(m7, m6)
        c22 = matrix_sum(matrix_sub(matrix_sum(m2, m5), m7), m3)

        # Fill temporal matrix with 0
        temp_matrix = []
        for row in range(length):
            temp_matrix.append([])
            for column in range(length):
                temp_matrix[row].append(0)

        for i in range(len(c11)):
            for j in range(len(c11)):
                temp_matrix[i][j] = c11[i][j]
                temp_matrix[i][j + len(c11)] = c12[i][j]
                temp_matrix[i + len(c11)][j] = c21[i][j]
                temp_matrix[i + len(c11)][j + len(c11)] = c22[i][j]

        return temp_matrix


"""
Global variables
"""
result_matrix_strassen = []
number_strassen_multiplication = 0
result_matrix_tb = []
number_tb_multiplication = 0
matrixA = []
matrixB = []


def main():
    global matrixA, matrixB

    input_matrixA = raw_input("Enter the name of the csv file of the MatrixA: ")
    input_matrixB = raw_input("Enter the name ot the csv file of the MatrixB: ")
    input_matrixRes = raw_input("Enter the name of the csv file to save the result: ")


    matrixA = matrix_reader(input_matrixA)
    print matrixA
    matrixB = matrix_reader(input_matrixB)
    print matrixB
    text_book_matrix_multiplication()
    print result_matrix_tb
    print "Number of scalar multiplications in the text book method: " + str(number_tb_multiplication)
    file_writing(input_matrixRes)
    print strassen_algorithm(matrixA, matrixB)
    print "Number of scalar multiplications in Strassen method: " + str(number_strassen_multiplication)


main()
