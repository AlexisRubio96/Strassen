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
CSV file writing for the result matrix
"""
def file_writing(file):
    global result_matrix_tb
    with open(file,'w') as new_csv:
        writer = csv.writer(new_csv)

        writer.writerows(result_matrix_tb)
        print "File create at " + file
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
                number_tb_multiplication += 1   ##Checar la posicion
    return

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
number_strassen_multiplication = 0
result_matrix_tb = []
number_tb_multiplication = 0
matrixA = []
matrixB = []


def main():
    global matrixA, matrixB
    """
    ##########Implementar al final###############
    input_matrixA = input("Enter the csv file name of the MatrixA: ")
    input_matrixB = input("Enter the csv file name of the MatrixB: ")
    """
    input_matrixRes = raw_input("Enter the route for the new csv file to save the result: ")

    matrixA = matrix_reader('Matriz_A_16_2_4.csv')
    print matrixA
    matrixB = matrix_reader('Matriz_B_16_2_4.csv')
    print matrixB
    text_book_matrix_multiplication()
    print result_matrix_tb
    print "Number of scalar multiplications in the text book method: " + str(number_tb_multiplication)
    file_writing(input_matrixRes)


main()
