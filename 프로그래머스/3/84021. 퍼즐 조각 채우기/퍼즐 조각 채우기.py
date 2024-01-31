def solution(game_board, table):
    
    def dfs_for_shape_board(visited_board,row, col, lst, cord):
        visited_board[row][col] = True
        for i in moves:
            n_row, n_col = row + i[0], col + i[1]
            c_row, c_col = cord[0] + i[0], cord[1] + i[1]
            if 0<=n_row<rows and 0<=n_col<cols and not visited_board[n_row][n_col] and game_board[n_row][n_col] ==0:
                #print(i)
                lst.append((c_row, c_col))
                dfs_for_shape_board(visited_board, n_row, n_col, lst, (c_row, c_col))

    def dfs_for_shape_table(visited_table, row, col, row_lst, col_lst):
        visited_table[row][col] = True
        for i in moves:
            n_row, n_col = row + i[0], col + i[1]
            if 0<=n_row<rows and 0<=n_col<cols and not visited_table[n_row][n_col] and table[n_row][n_col] ==1:
                #print(i)
                row_lst.append(n_row)
                col_lst.append(n_col)
                dfs_for_shape_table(visited_table, n_row, n_col, row_lst, col_lst)

    def dfs_for_shape_piece(visited_piece,row, col, lst, cord):
        visited_piece[row][col] = True
        for i in moves:
            n_row, n_col = row + i[0], col + i[1]
            c_row, c_col = cord[0] + i[0], cord[1] + i[1]
            if 0<=n_row<rows_pc and 0<=n_col<cols_pc and not visited_piece[n_row][n_col] and sub[n_row][n_col] ==1:
                #print(i)
                lst.append((c_row, c_col))
                dfs_for_shape_piece(visited_piece, n_row, n_col,lst, (c_row, c_col))

        
    moves = [(0,1),(0,-1),(1,0),(-1,0)]  # right, left, down, up
    
    answer = 0
    rows = len(game_board)
    cols = len(game_board[0])
    shape_dict= []
    visited_board = [[False for _ in range(cols)] for _ in range(rows)]
    for row in range(rows):
        for col in range(cols):
            if not visited_board[row][col] and game_board[row][col] == 0:
                lst1 = []
                cord = (0,0)
                dfs_for_shape_board(visited_board,row,col,lst1, cord)
                shape_dict.append(lst1)
    piece_dict = []
    visited_table = [[False for _ in range(cols)] for _ in range(rows)]
    for row in range(rows):
        for col in range(cols):
            if not visited_table[row][col] and table[row][col] == 1:
                row_lst,col_lst = [],[]
                row_lst.append(row)
                col_lst.append(col)
                dfs_for_shape_table(visited_table,row, col, row_lst,col_lst)
                min_row, max_row, min_col, max_col = min(row_lst), max(row_lst), min(col_lst), max(col_lst)
                piece = [i[min_col: max_col+1] for i in table[min_row: max_row +1]]
                piece_move_lst = []

                rotated_90 = list(zip(*piece[::-1]))
                rotated_180 = list(zip(*rotated_90[::-1]))
                rotated_270 = list(zip(*rotated_180[::-1]))

                for sub in [piece, rotated_90, rotated_180, rotated_270]:
                    rows_pc = len(sub)
                    cols_pc = len(sub[0])
                    vis_pc = [[False for _ in range(cols_pc)] for _ in range(rows_pc)]
                    for row_ in range(rows_pc):
                        for col_ in range(cols_pc):
                            if not vis_pc[row_][col_] and sub[row_][col_] ==1:
                                tmp_lst = []
                                cord = (0,0)
                                dfs_for_shape_piece(vis_pc, row_, col_, tmp_lst,cord)
                                piece_move_lst.append(tmp_lst)


                #piece_dict[str(ct2)] = piece_move_lst
                piece_dict.append(piece_move_lst)
    for ch in piece_dict:
        for ch_ in ch:
            if ch_ in shape_dict:
                shape_dict.remove(ch_)
                answer+=len(ch_)+1
                break
    return answer