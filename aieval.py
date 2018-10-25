class AIEval:
    def __init__(self, eval, state):
        if state == 1:
            self.pawnEvalWhite = eval[0]
            self.pawnEvalBlack = self.reverseList(self.pawnEvalWhite)

            self.bishopEvalWhite = eval[1]
            self.bishopEvalBlack = self.reverseList(self.bishopEvalWhite)

            self.rookEvalWhite = eval[2]
            self.rookEvalBlack = self.reverseList(self.rookEvalWhite)

            self.knightEval = eval[3]

            self.evalQueen = eval[4]

            self.kingEvalWhite = eval[5]
            self.kingEvalBlack = self.reverseList(self.kingEvalWhite)

        elif state == 2:
            self.pawnEvalBlack = eval[0]
            self.pawnEvalWhite = self.reverseList(self.pawnEvalBlack)

            self.bishopEvalBlack = eval[1]
            self.bishopEvalWhite = self.reverseList(self.bishopEvalBlack)

            self.rookEvalBlack = eval[2]
            self.rookEvalWhite = self.reverseList(self.rookEvalBlack)

            self.knightEval = eval[3]

            self.evalQueen = eval[4]

            self.kingEvalBlack = eval[5]
            self.kingEvalWhite = self.reverseList(self.kingEvalBlack)

    def reverseList(self, _list):
        return _list[::-1]