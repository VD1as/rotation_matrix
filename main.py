matrix_numbers = []
for i in range(1,10):
    numbers = int(input("Insert the numbers for the matrix: "))
    matrix_numbers.append(numbers)

rotation_matrix = [
        [matrix_numbers[0],matrix_numbers[1],matrix_numbers[2]],
        [matrix_numbers[3],matrix_numbers[4],matrix_numbers[5]],
        [matrix_numbers[6],matrix_numbers[7],matrix_numbers[8]]]

print(rotation_matrix)
