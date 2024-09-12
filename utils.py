def convert_line_to_string(line,player):
    """动态转换棋盘上的坐标变为字符串,使得当前玩家的值永远是1"""

    return ''.join(['1'if x==player else '2' if x== -player else '0' for x in line])


def get_lines(board,direction):
    """获取行 列 对角线的信息"""
    
    size=len(board)
    lines=[]
    if direction=='row':#返回行
        for row in board:
            lines.append(row)

    elif direction == 'col':#返回列
        for col in range(size):
            column=[board[row][col]for row in range(size)]
            lines.append(column)

    elif direction == 'diag1':#对角线从右上到左下
        for diag_offset in range(4,15):
            diag1=[board[diag_offset-i][i] for i in range(diag_offset+1)]
            lines.append(diag1)
        for diag_offset in range(4,14):
            diag1=[board[14-i][14-diag_offset+i] for i in range(diag_offset+1)]
            lines.append(diag1)
    
    elif direction =='diag2':#对角线从左上到右下
        for diag_offset in range(4,15):
            diag2=[board[i][14-diag_offset+i] for i in range(diag_offset+1)]
            lines.append(diag2)
        for diag_offset in range(4,14):
            diag2=[board[14-diag_offset+i][i] for i in range(diag_offset+1)]
            lines.append(diag2)
    return lines




