import copy
from typing import List


def print_boards(boards: List[List[List[str]]]):
    size = len(boards[0])
    line = "-" * 4 * size
    for board in boards:
        print_board(board)
        print(line)


def print_board(board: List[List[str]]):
    size = len(board)
    line = "-" * 4 * size
    for row in board:
        print(line)
        row_to_print = "|"
        for col in row:
            row_to_print += " "
            for char in col:
                row_to_print += char if char != "." else " "
                row_to_print += " |"
        print(row_to_print)
    print(line)


def convert_row(row: List[str]) -> str:
    line = ""
    for char in row:
        line += char
    return line


def convert_board(board: List[List[str]]) -> List[str]:
    output_board = []
    for row in board:
        output_board.append(convert_row(row))
    return output_board


def convert_boards(boards: List[List[List[str]]]) -> List[List[str]]:
    output_boards = []
    for board in boards:
        output_boards.append(convert_board(board))
    return output_boards


def init_board(n: int) -> List[List[str]]:
    board: List[List[str]] = []
    for i in range(n):
        row: List[str] = []
        for j in range(n):
            row.append(".")
        board.append(row)
    return board


def is_valid(board: List[List[str]], cell: List[int]) -> bool:
    size = len(board)
    row = cell[0]
    col = cell[1]

    for i in range(size):
        if board[row][i] == "Q" or board[i][col] == "Q":
            return False
        for j in range(size):
            dy = col - j
            dx = row - i
            if dx == dy or dx == -dy:
                if board[i][j] == "Q":
                    return False

    return True


def solve(boards: List[List[List[str]]], board: List[List[str]], start_col=0, start_row=0, depth=0):
    if board is None:
        print("No Solution")
        return None

    n = len(board)
    for i in range(start_row, n):
        for j in range(start_col, n):
            if is_valid(board, [i, j]):
                board[i][j] = "Q"
                sol = solve(boards, board, 0, i + 1, depth + 1)
                if sol is not None:
                    if depth == n - 1:
                        board[i][j] = "."
                        continue
                    return sol
                board[i][j] = "."
        return None
    boards.append(copy.deepcopy(board))
    return board


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        boards: List[List[List[str]]] = []
        board: List[List[str]] = init_board(n)

        solve(boards, board)
        print(len(boards))
        # print_boards(boards)
        return convert_boards(boards)


if __name__ == '__main__':
    sol = Solution()
    print(sol.solveNQueens(4))
