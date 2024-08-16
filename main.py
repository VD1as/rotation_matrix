import math
import numpy as np

def get_input_coordinates():
    coordinates = []
    for i in range(3):
        coordinates.append(float(input(f"Insert coordinate {i + 1}: ")))
    return coordinates

def get_rotation_matrix(axis, degrees):
    radians = math.radians(degrees)
    cosine = math.cos(radians)
    sine = math.sin(radians)

    if axis == 'x':
        return np.array([[1, 0, 0], [0, cosine, sine], [0, -sine, cosine]])
    elif axis == 'y':
        return np.array([[cosine, 0, -sine], [0, 1, 0], [sine, 0, cosine]])
    elif axis == 'z':
        return np.array([[cosine, sine, 0], [-sine, cosine, 0], [0, 0, 1]])

def rotate_coordinates(coordinates, rotation_matrix):
    return np.dot(rotation_matrix, np.array(coordinates).reshape(3, 1))

def main():
    choose_option = int(input('''Select the option for the calculation: 
                            [1] - Calculation of inertial coordinates
                            [2] - Calculation of moving coordinates
                            Choose: '''))

    if choose_option not in [1, 2]:
        print("Invalid option selected.")
        return

    coordinates_input = get_input_coordinates()
    raw_degrees_of_rotation = float(input("Insert the degrees: "))

    axis_rotation = ''
    if coordinates_input[0] == 0:
        axis_rotation = 'x'
    elif coordinates_input[1] == 0:
        axis_rotation = 'y'
    elif coordinates_input[2] == 0:
        axis_rotation = 'z'
    else:
        print("At least one coordinate must be zero to define an axis of rotation.")
        return

    rotation_matrix = get_rotation_matrix(axis_rotation, raw_degrees_of_rotation)

    if choose_option == 1:
        inverse_rotation_matrix = np.linalg.inv(rotation_matrix)
        result_matrix = rotate_coordinates(coordinates_input, inverse_rotation_matrix)
        print(f"Resulting inertial coordinates:\n X = {result_matrix[0][0]:.6f} \n Y = {result_matrix[1][0]:.6f} \n Z = {result_matrix[2][0]:.6f}")
    else:
        result_matrix = rotate_coordinates(coordinates_input, rotation_matrix)
        print(f"Resulting moving coordinates:\n X = {result_matrix[0][0]:.6f} \n Y = {result_matrix[1][0]:.6f} \n Z = {result_matrix[2][0]:.6f}")

if __name__ == "__main__":
    main()
