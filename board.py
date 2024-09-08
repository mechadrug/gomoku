class Board:
    def __init__(self, size=15):
        self.size = size  # 棋盘尺寸
        self.board = [[0] * size for _ in range(size)]  # 0代表空，1代表黑棋，-1代表白棋

    def display_board(self):
        """在命令行中绘制棋盘"""
        print("   " + " ".join([f"{i:2}" for i in range(self.size)]))  # 绘制列号
        for i, row in enumerate(self.board):
            row_display = []
            for cell in row:
                if cell == 0:
                    row_display.append(' .')  # 空位用 '.' 表示
                elif cell == 1:
                    row_display.append(' ●')  # 黑子用 '●' 表示
                elif cell == -1:
                    row_display.append(' ○')  # 白子用 '○' 表示
            print(f"{i:2} " + " ".join(row_display))  # 绘制行号和每行的内容

    def place_stone(self, x, y, color):
        """在指定位置放置棋子"""
        if self.is_valid_move(x, y):
            self.board[x][y] = color
            return True
        return False
    
    def is_valid_move(self, x, y):
        """检查棋子位置是否合法"""
        return 0 <= x < self.size and 0 <= y < self.size and self.board[x][y] == 0

    def check_winner(self):
        """检查是否有玩家胜利,返回赢家颜色(1 或 -1),没有则返回0"""
        for i,row in enumerate(self.board):#横向检测
            num = 0
            for j,col in enumerate(self.board[i]):
                if j==0 and self.board[i][j]!=0:
                    num+=1
                elif self.board[i][j]==self.board[i][j-1]!=0:
                    num+=1
                elif self.board[i][j]!=self.board[i][j-1]:
                    if self.board[i][j]!=0:
                        num=1
                    else:
                        num =0
                if num >=5:
                    return self.board[i][j]
        for i in range(self.size):#竖向检测
            for j in range(self.size):
                if j==0 and self.board[j][i]!=0:
                    num +=1
                elif self.board[j][i]==self.board[j-1][i]!=0:
                    num+=1
                elif self.board[j][i]==self.board[i][j-1]:
                    if self.board[j][i]!=0:
                        num=1
                    else:
                        num = 0
                if num >=5:
                    return self.board[j][i]
        return 0
    def check_slant(self,x,y,current_player):#处理斜向
        def get_point(r,c,dr,dc):
            count=0
            while 0<=r<=self.size and 0<=c<=self.size and self.board[r][c]==current_player:
                r+=dr
                c+=dc
                count+=1
            
            return count
        count1=get_point(x,y,1,1)+get_point(x,y,-1,-1)-1
        print(count1)
        if count1>=5:
            return True
        count2=get_point(x,y,1,-1)+get_point(x,y,-1,1)-1
        print(count2)
        if count2>=5:
            return True
        return False
def get_user_input():
    """获取用户输入的坐标"""
    while True:
        try:
            x, y = map(int, input("请输入你的落子位置，格式为 'x y': ").split())
            return x, y
        except ValueError:
            print("输入无效，请输入两个整数，例如 '7 7'。")   
def game_loop():
    board = Board()
    current_player = 1  # 1 表示黑棋，-1 表示白棋

    while True:
        board.display_board()

        if current_player == 1:
            print("黑棋 (●) 回合")
        else:
            print("白棋 (○) 回合")

        x, y = get_user_input()

        if board.place_stone(x, y, current_player):
            # 切换回合
            current_player = -current_player
        else:
            print("该位置已被占用，请重新输入。")

        #检查是否有玩家获胜（此处未实现，可加入胜负判断）
        winner = board.check_winner()
        
        if winner:
            print(f"玩家 {'黑棋' if winner == 1 else '白棋'} 获胜！")
            break
        winner2=board.check_slant(x,y,-current_player)
        if winner2:
            print(f"玩家 {'黑棋' if winner2 else '白棋'} 获胜！")
            break

if __name__ == "__main__":
    game_loop()