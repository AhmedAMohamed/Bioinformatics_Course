__author__ = 'AhmedA'


def backTrack(matrix, seq1, seq2, currentI, currentJ, result, maxScore):
    if currentI == 0 and currentJ == 0:
        print("done")
        return
        #return result
    if matrix[currentI-1][currentJ-1] <= matrix[currentI][currentJ]:
        print("diagonal")
        print(seq1[currentI-1],seq2[currentJ-1])
        #result[0] = result[0]+seq1[currentI-1]
        #result[1] = result[1]+seq2[currentJ-1]
        backTrack(matrix, seq1, seq2, currentI-1, currentJ-1, result, matrix[currentI-1][currentJ-1])
    elif matrix[currentI-1][currentJ] <= matrix[currentI][currentJ]:
        print("-",seq2[currentJ-1])
        #result[0] = result[0]+"-"
        #result[1] = result[1]+seq2[currentJ]
        backTrack(matrix, seq1, seq2, currentI-1, currentJ, result, matrix[currentI-1][currentJ])
    elif matrix[currentI][currentJ-1] <= matrix[currentI][currentJ]:
        print(seq1[currentI-1],"-")
        #result[0] = result[0]+seq1[currentI-1]
        #result[1] = result[1]+"-"
        backTrack(matrix, seq1, seq2, currentI, currentJ-1, result, matrix[currentI-1][currentJ])


# sequences definitions
seq1 = "gaattcagtta"
seq2 = "ggatcga"
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
            matrix[i][j] = 0#matrix[i][j-1] + gap
        elif j == 0:
            matrix[i][j] = 0#matrix[i-1][j] + gap
        else:
            diagonal = misMatch
            if seq1[i-1] == seq2[j-1]:
                diagonal = match
            matrix[i][j] = max(matrix[i-1][j-1] + diagonal, matrix[i-1][j] + gap, matrix[i][j-1] + gap)
        j += 1
    i += 1
for i in matrix:
    print(i)
maxScore = matrix[len(seq1)][len(seq2)]
# back tracking
result = ["",""]
r = backTrack(matrix, seq1, seq2, len(seq1), len(seq2), result, maxScore)
