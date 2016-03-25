__author__ = 'AhmedA'

# sequences definitions
seq1 = "AAAAAA"
seq2 = "AAAAAA"
# parameters definitions
match = 2
misMatch = -1
gap = -2

# initializing the matrix to zero
matrix = []
for i in range(len(seq1)+1):
    matrix.append([])
    for j in range(len(seq2)+1):
        matrix[i].append(0)

# filling the score matrix
i = 0
while i < len(matrix):
    j = 0
    while j < len(matrix[i]):
        if i == 0 and j == 0:
            matrix[i][j] = 0
        elif i == 0:
            matrix[i][j] = matrix[i][j-1] + gap
        elif j == 0:
            matrix[i][j] = matrix[i-1][j] + gap
        else:
            diagonal = misMatch
            if seq1[i-1] == seq2[j-1]:
                diagonal = match
            matrix[i][j] = max(matrix[i-1][j-1] + diagonal, matrix[i-1][j] + gap, matrix[i][j-1] + gap)
        j += 1
    i += 1
maxScore = matrix[len(seq1)][len(seq2)]
# back tracking

for i in matrix:
    print(i)