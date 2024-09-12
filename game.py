from board import Board
from ai import AI

class GomokuGame:
    def __init__(self):
        self.board = Board()
        #self.ai = AI()  # AI实例
        self.current_player=1
        self.x=0
        self.y=0
    def start(self):
        """开始游戏循环"""
        self.board.display_board()
        self.current_player = 1  # 1 表示黑棋，-1 表示白棋
        while True:
            self.board.display_board()
            self.player_turn()
            if self.check_end_game(self.x,self.y,self.current_player):
                break
            self.ai_turn()
            if self.check_end_game(self.x,self.y,self.current_player):
               break

    def player_turn(self):
        """处理玩家的输入和下棋"""
        

        if self.current_player == 1:
            print("黑棋 (●) 回合")
        else:
            print("白棋 (○) 回合")

        self.x, self.y = get_user_input()

        if self.board.place_stone(self.x, self.y, self.current_player):
            # 切换回合
            self.current_player = -self.current_player
        else:
            print("该位置已被占用，请重新输入。")

        
    def ai_turn(self):
        """AI下棋逻辑"""
        #move = self.ai.get_move(self.board)
        #self.board.place_stone(move[0], move[1], -1)  # AI通常是白棋

    def check_end_game(self,x,y,current_player):
        """检查游戏是否结束"""
        #检查是否有玩家获胜
        winner = self.board.check_winner()
        
        if winner:
            self.board.display_board()
            print(f"玩家 {'黑棋' if winner == 1 else '白棋'} 获胜！")
            return True
        winner2=self.board.check_slant(x,y,-current_player)
        if winner2:
            self.board.display_board()
            print(f"玩家 {'黑棋' if winner2 else '白棋'} 获胜！")
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