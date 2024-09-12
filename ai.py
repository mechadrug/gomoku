from board import Board

class AI:
    def __init__(self):
        pass
    def evaluate(self,board,player):#评估函数
        pass
    def alpha_beta(self,depth,alpha,beta,is_AI,board,x,y,current_winner):#实现对于局面的测算
        if depth==0 or board.check_winner() or board.check_slant(x,y,current_winner):
            return self.evaluate()
        
        if is_AI:#这是ai，要尽量追求价值最大化，
            max_value=-float('inf')
            for i in range(board.size):
                for j in range(board.size):
                    if board[i][j]==0:
                        board[i][j]=-1
                        value=self.alpha_beta(depth-1,alpha,beta,-is_AI,board,i,j,-current_winner)
                        max_value=max(max_value,value)
                        alpha=max(alpha,value)
                        board[i][j]=0
                        if beta<=alpha:
                            break
            return max_value
        else:
            min_value=float('inf')
            for i in range(board.size):
                for j in range(board.size):
                    if board[i][j]==0:
                        board[i][j]=1
                        value=self.alpha_beta(depth-1,alpha,beta,-is_AI,board,i,j,-current_winner)
                        min_value=min(min_value,value)
                        beta=min(alpha,value)
                        board[i][j]=0
                        if beta<=alpha:
                            break
            return min_value