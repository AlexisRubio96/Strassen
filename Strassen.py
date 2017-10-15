"""
Ernesto Aelejandro Cervantes Villa  A01370793
Jorge Alexis Rubio Sumano   A01372074

Strassen Algorithm Implementation
"""
import csv

"""
****************************File reading************************************
This method takes care of the csv file reading.
Returns a multidimensional array of size [n][n], i.e. a matrix nxn
"""
def matrix_reader(file):
    # File read
    # File is open
    with open(file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        # Matrix creation
        matrix = []
        row_number = 0
        for row in reader:
            matrix.append([])
            # rowxrow = nxn
            for i in range(len(row)):
                matrix[row_number].append(int(row[i]))
                # print row[i]
                # for j in range(len(row)):
                #   matrix[row_number][j]
            row_number += 1
    csv_file.close()
    return matrix


"""
****************************File writing***********************************
File writing for the result matrix
"""
def file_writing(file):
    return


"""
****************************Matrix multiplication type 1**************************************
This resolves the first part of the activity(III.1): matrix multiplication defined in any linear algebra text book.
Take both global matrices A and B, and the result matrix of text book.
"""
def text_book_matrix_multiplication():
    global matrixA, matrixB, result_matrix_tb
    lenght = len(matrixA)
    for i in range(lenght):
        for j in range(lenght):
            for k in range(lenght):
                result_matrix_tb[i][k] = result_matrix_tb[i][k] + (matrixA[i][j] * matrixB[j][k])

    print result_matrix_tb


"""
****************************Matrix multiplication type 2**************************************
This resolves the second part of the activity(III.2): implement the Strassen algorithm for the multiplication of matrices of order n.
"""
def strassen_algorithm():
    print result_matrix_strassen


"""
Global variables
"""
result_matrix_strassen = []
result_matrix_tb = []
matrixA = []
matrixB = []


def main():
    global matrixA, matrixB
    """
    ##########Implementar al final###############
    input_matrixA = input("Enter the csv file name of the MatrixA: ")
    input_matrixB = input("Enter the csv file name of the MatrixB: ")
    input_matrixRes = input("Enter the csv file to save the result: ")
    """
    matrixA = matrix_reader('Matriz_A_16_2_4.csv')
    print matrixA
    matrixB = matrix_reader('Matriz_B_16_2_4.csv')
    print matrixB
    text_book_matrix_multiplication()


main()
