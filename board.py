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
        for i in range(self.size):#横向检测
            num = 0
            for j in range(self.size):
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
            num = 0
            for j in range(self.size):
                if j==0 and self.board[j][i]!=0:
                    num +=1
                elif self.board[j][i]==self.board[j-1][i]!=0:
                    num+=1
                elif self.board[j][i]!=self.board[j][i-1]:
                    if self.board[j][i]!=0:
                        num=1
                    else:
                        num = 0
                if num >=5:
                    return self.board[j][i]
        return 0
    def check_slant(self,x,y,current_player):#处理斜向
        """检查是否有玩家胜利,返回赢家颜色(1 或 -1),没有则返回0"""
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