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
        pass
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

        # 检查是否有玩家获胜（此处未实现，可加入胜负判断）
        # winner = board.check_winner()
        # if winner:
        #     print(f"玩家 {'黑棋' if winner == 1 else '白棋'} 获胜！")
        #     break

if __name__ == "__main__":
    game_loop()