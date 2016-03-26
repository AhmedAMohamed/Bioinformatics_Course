__author__ = 'AhmedA'


def getMaxMove(matrix, currentI, currentJ, match, mismatch, gap, seq1, seq2):
    matchOrmis = mismatch
    if seq1[currentI-1] == seq2[currentJ-1]:
        matchOrmis = match
    if (matrix[currentI-1][currentJ-1] + matchOrmis) >= (matrix[currentI-1][currentJ] + gap)\
        and  (matrix[currentI-1][currentJ-1] + matchOrmis) >= (matrix[currentI][currentJ-1] + gap):
        return "diagonal"
    elif (matrix[currentI][currentJ-1] + gap) >= (matrix[currentI-1][currentJ-1] + matchOrmis)\
        and  (matrix[currentI][currentJ-1] + gap) >= (matrix[currentI-1][currentJ] + gap):
        return "horizontal"
    elif (matrix[currentI-1][currentJ] + gap) >= (matrix[currentI-1][currentJ-1] + matchOrmis)\
        and  (matrix[currentI-1][currentJ] + gap) >= (matrix[currentI][currentJ-1] + gap):
        return "vertical"

def backTrack(matrix, seq1, seq2, currentI, currentJ, result, maxScore):
    if currentI == 0 and currentJ == 0:
        print("done")
        return
        #return result
    else:
        move = getMaxMove(matrix,currentI,currentJ,2,-1,-2,seq1,seq2)
        if move == "diagonal":
            print(seq1[currentI-1], seq2[currentJ-1], "diagonal move")
            backTrack(matrix, seq1, seq2, currentI-1, currentJ-1, result, maxScore)
        elif move == "horizontal":
            print(seq1[currentI-1], "-", "horizontal move")
            backTrack(matrix, seq1, seq2, currentI, currentJ-1, result, maxScore)
        elif move == "vertical":
            print(currentI, currentJ, "val")
            print("-", seq2[currentJ-1], "vertical move")
            backTrack(matrix, seq1, seq2, currentI-1, currentJ, result, maxScore)

# sequences definitions
seq1 = "gaattcagtta"
seq2 = "ggatcga"

'''
        gaa-tc---a
        ggaatccgga
'''
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