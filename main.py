import math
import numpy as np

choose_option = int(input('''select the option for the calculation: 
                            [1] - Calculation of inertial coordinates
                            [2] - Calculation of moving coordinates
                            [3] - Identify rotation on a given axis
                            Choose: '''))

coordinates_input = []

if choose_option == 1 or choose_option == 2:
    for i in range(1,4):
        coordinates = float(input("Insert the coordinates: "))
        coordinates_input.append(coordinates)

    raw_degrees_of_rotation = float(input("Insert the degrees: "))
    degrees_of_rotation = math.radians(raw_degrees_of_rotation)

    cosine_degrees = math.cos(degrees_of_rotation)
    sine_degrees = math.sin(degrees_of_rotation)


    matrix_rotation_x = np.array([[cosine_degrees,sine_degrees],[-sine_degrees,cosine_degrees]])
    matrix_rotation_y = np.array([[cosine_degrees,-sine_degrees],[sine_degrees,cosine_degrees]])
    matrix_rotation_z = np.array([[cosine_degrees,sine_degrees],[-sine_degrees,cosine_degrees]])

    if choose_option == 1:
        if coordinates_input[0] == 0:
            print("Rotação no eixo X")

            coordinates_matrix = np.array([[coordinates_input[1]],[coordinates_input[2]]])

            moving_coordinates_matrix = np.array([[coordinates_input[1]],coordinates_input[2]])
            inverse_matrix_rotation_x = np.linalg.inv(matrix_rotation_x)
            
            result_matrix = np.dot(inverse_matrix_rotation_x,moving_coordinates_matrix)
            print(f" X = {result_matrix[0][0]:.6f} \n Y = {result_matrix[1][0]:.6f}")


        elif coordinates_input[1] == 0:
            print("Rotação no eixo Y")

            coordinates_matrix = np.array([[coordinates_input[0]],[coordinates_input[2]]])

            moving_coordinates_matrix = np.array([[coordinates_input[0]],coordinates_input[2]])
            inverse_matrix_rotation_y = np.linalg.inv(matrix_rotation_y)

            result_matrix = np.dot(inverse_matrix_rotation_y,moving_coordinates_matrix)
            print(f" X = {result_matrix[0][0]:.6f} \n Y = {result_matrix[1][0]:.6f}")


        elif coordinates_input[2] == 0:
            print("Rotação no eixo Z")

            coordinates_matrix = np.array([[coordinates_input[0]],[coordinates_input[1]]])

            moving_coordinates_matrix = np.array([[coordinates_input[0]],[coordinates_input[1]]])
            inverse_matrix_rotation_z = np.linalg.inv(matrix_rotation_z)
         
            result_matrix = np.dot(inverse_matrix_rotation_z,moving_coordinates_matrix)
            print(f" X = {result_matrix[0][0]:.6f} \n Y = {result_matrix[1][0]:.6f}")

    elif choose_option == 2:
        
        if coordinates_input[0] == 0:
            print("Rotação no eixo X")

            coordinates_matrix = np.array([[coordinates_input[1]],[coordinates_input[2]]])

            moving_coordinates_matrix = np.array([[coordinates_input[1]],coordinates_input[2]])
            
            result_matrix = np.dot(matrix_rotation_x,moving_coordinates_matrix)
            print(f" X = {result_matrix[0][0]:.6f} \n Y = {result_matrix[1][0]:.6f}")


        elif coordinates_input[1] == 0:
            print("Rotação no eixo Y")

            coordinates_matrix = np.array([[coordinates_input[0]],[coordinates_input[2]]])

            moving_coordinates_matrix = np.array([[coordinates_input[0]],coordinates_input[2]])

            result_matrix = np.dot(matrix_rotation_y,moving_coordinates_matrix)
            print(f" X = {result_matrix[0][0]:.6f} \n Y = {result_matrix[1][0]:.6f}")


        elif coordinates_input[2] == 0:
            print("Rotação no eixo Z")

            coordinates_matrix = np.array([[coordinates_input[0]],[coordinates_input[1]]])

            moving_coordinates_matrix = np.array([[coordinates_input[0]],[coordinates_input[1]]])
        
            result_matrix = np.dot(matrix_rotation_z,moving_coordinates_matrix)
            print(f" X = {result_matrix[0][0]:.6f} \n Y = {result_matrix[1][0]:.6f}")

elif choose_option == 3:
    matrix_numbers = []
    for i in range(1,10):
        numbers = int(input("Insert the numbers for the matrix: "))
        matrix_numbers.append(numbers)

    rotation_matrix = [
            [matrix_numbers[0],matrix_numbers[1],matrix_numbers[2]],
            [matrix_numbers[3],matrix_numbers[4],matrix_numbers[5]],
            [matrix_numbers[6],matrix_numbers[7],matrix_numbers[8]]]

    print(rotation_matrix)

    def check_matrix(matrix):
        flat_list = [item for sublist in matrix for item in sublist]
        zero_count = flat_list.count(0)
        one_count = flat_list.count(1)
        
        if zero_count == 4 and one_count == 1 and len(flat_list) == zero_count + one_count + flat_list.count(flat_list[flat_list.index(1) + 1]):
            return True
        return False

    final_rotation_matrix = check_matrix(rotation_matrix)

    print(final_rotation_matrix)