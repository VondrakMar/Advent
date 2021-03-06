f = open("data.t", "r")
rowsN = 127
columnN = 7


# for the first iteration set Srow and Scol to zeros
def whichseat(seq,Srow, Scol, row, col):

    R = [Srow,row]
    C = [Scol,col]
    if seq[0] == "F":
        R[1] -= int((row - Srow+1)/2)
    if seq[0] == "B":
        R[0] += int((row - Srow)/2) + 1
    if seq[0] == "R":
        C[0] += int((col - Scol)/2) + 1
    if seq[0] == "L":
        C[1] -= int((col - Scol)/2) + 1
    if len(seq) > 1:
        return whichseat(seq[1:], R[0], C[0], R[1], C[1])
    else:
        return R[0]*8 + C[0]
# first part answer
max = 0
for line in f:
    hold = whichseat(line, 0, 0, rowsN, columnN)
    if max < hold:
        max = hold
print(max)

