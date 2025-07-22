def solution(board):
    from copy import deepcopy

    rows, cols = len(board), len(board[0])
    board = [list(row) for row in board]

    # Step 1: Simulate gravity (falling down)
    for col in range(cols):
        stack = []
        for row in reversed(range(rows)):
            if board[row][col] == '#':
                stack.append('#')
            elif board[row][col] == '*':
                r = row + 1
                for s in stack:
                    if r < rows:
                        board[r][col] = s
                        r += 1
                for k in range(row + 1, r):
                    if board[k][col] != '*':
                        board[k][col] = '#'
                for r2 in range(r, rows):
                    if board[r2][col] != '*':
                        board[r2][col] = '_'
                stack = []
        # Fill remaining stack at bottom
        r = rows - len(stack)
        for i in range(rows):
            if i < r:
                if board[i][col] != '*':
                    board[i][col] = '_'
            else:
                if board[i][col] != '*':
                    board[i][col] = stack[i - r]

    # Step 2: Mark explosions
    to_explode = [[False]*cols for _ in range(rows)]
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),  (0, 0),  (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == '*':
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < rows and 0 <= nj < cols and board[ni][nj] == '#':
                        to_explode[ni][nj] = True

    # Step 3: Apply explosions
    for i in range(rows):
        for j in range(cols):
            if to_explode[i][j]:
                board[i][j] = '_'

    return [''.join(row) for row in board]
