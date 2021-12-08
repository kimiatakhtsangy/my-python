from random import choice
n_rows = int(input("tell me the number of rows:"))
m_columns = int(input("tell me the number of columns:"))


gold = []
print("tell me the entries:")

for i in range(n_rows):
    a = []

    for j in range(m_columns):
        a.append(int(input()))

    gold.append(a)


for i in range(n_rows):

    for j in range(m_columns):

        print(gold[i][j], end=" ")

    print( )


def maxgold(gold, m_columns, n_rows):

    dynamictable = [[0 for i in range(m_columns)]
                    for j in range(n_rows)]

    for col in range(m_columns - 1, -1, -1):
        for row in range(n_rows):

            if col == m_columns - 1:
                right = 0
            else:
                right = dynamictable[row][col + 1]

            if row == 0 or col == m_columns - 1:
                right_up = 0
            else:
                right_up = dynamictable[row - 1][col + 1]

            if row == n_rows - 1 or col == m_columns - 1:
                right_down = 0
            else:
                right_down = dynamictable[row + 1][col + 1]

            dynamictable[row][col] = gold[row][col] + max(max(right, right_up), right_down)
    res = dynamictable[0][0]
    for i in range(1, n_rows):
        res = max(res, dynamictable[i][0])

    return res


print("The maximum gold you can pick:\n")
print(maxgold(gold, m_columns, n_rows))
