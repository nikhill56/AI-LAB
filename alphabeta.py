MAX = 9999
MIN = -9999


def minimax(curDepth, nodeIndex, maxTurn, scores, alpha, beta):

    if curDepth == 3:
        return scores[nodeIndex]

    if maxTurn:

        best = MIN

        for i in range(0, 2):
            val = minimax(curDepth+1, nodeIndex*2+i,
                          False, scores, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            if(beta <= alpha):
                break
        return best
    else:

        best = MAX

        for i in range(0, 2):
            val = minimax(curDepth+1, nodeIndex*2+i, True, scores, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            if(beta <= alpha):
                break
        return best


scores = [3, 5, 2, 9, 12, 5, 23, 23]
print("Optimal Values is:", end=" ")
print(minimax(0, 0, True, scores, MIN, MAX))
