def check_sudoku(sudoku):
    for i in range(9):
        row_set = set()
        column_set = set()
        for j in range(9):
            if sudoku[i][j] in row_set or sudoku[j][i] in column_set:
                return 'No'
            row_set.add(sudoku[i][j])
            column_set.add(sudoku[j][i])

    for i in range(3):
        for j in range(3):
            subgrid_set = set()
            for x in range(i * 3, (i + 1) * 3):
                for y in range(j * 3, (j + 1) * 3):
                    if sudoku[x][y] in subgrid_set:
                        return 'No'
                    subgrid_set.add(sudoku[x][y])

    return 'Yes'


sudoku = []
for i in range(9):
    row = list(map(int, input(f"Enter numbers for row {i+1}: ").split()))
    sudoku.append(row)

print(check_sudoku(sudoku))
