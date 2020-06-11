"""
Design Tic-Tac-Toe
-------------------
Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves is allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Example:
Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

TicTacToe toe = new TicTacToe(3);

toe.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

toe.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

toe.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

toe.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

toe.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

toe.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|

Follow up:
Could you do better than O(n2) per move() operation?
"""
from collections import defaultdict


class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n

        """
        self.board = [[None] * n] * n
        
        With this approach, each row will be referencing the same obj.
        This if I set row[0][0] = 12, then row[1][0] will also become 12.
        
        >>> a = [ [0]*3 ] * 3
        >>> a
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        >>> a[0][0] = 12
        >>> a
        [[12, 0, 0], [12, 0, 0], [12, 0, 0]]

        """
        self.board = self.get_board(n)
        self.n = n
        self.winner = 0

    def get_board(self, n):
        board = defaultdict(lambda: [])
        for i in range(n):
            row = [0] * n
            board[i].extend(row)

        return board

    def is_winner_move(self, row, col, player):
        # horizonatal
        for j in range(self.n):
            if self.board[row][j] != player:
                break
        else:
            return True

        # vertical
        for i in range(self.n):
            if self.board[i][col] != player:
                break
        else:
            return True

        # diagonal
        if not ((row == col) or (row + col) == self.n - 1):
            return False

        # (0, 0), (1, 1) ... (n-1, n-1)
        # (0, n-1), (1, n-2) ... (n-1, 0)
        for i in range(self.n):
            if self.board[i][i] != player:
                break
        else:
            return True

        for i in range(self.n):
            if self.board[i][self.n - i - 1] != player:
                break
        else:
            return True

        return False

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        if self.winner:
            return self.winner

        self.board[row][col] = player
        is_win = self.is_winner_move(row, col, player)
        if is_win:
            self.winner = player

        return player if is_win else 0


# Test case 1
t = TicTacToe(n=3)
assert 0 == t.move(row=0, col=0, player=1)
assert 0 == t.move(0, 2, 2)
assert 0 == t.move(2, 2, 1)
assert 0 == t.move(1, 1, 2)
assert 0 == t.move(2, 0, 1)
assert 0 == t.move(1, 0, 2)
assert 1 == t.move(2, 1, 1)
assert 1 == t.move(1, 2, 1)

# Test case 2
"""
1 0 2
2 2 0
1 1 1
"""
t = TicTacToe(n=3)
assert 0 == t.move(row=0, col=0, player=1)
assert 0 == t.move(0, 2, 2)
assert 0 == t.move(2, 2, 1)
assert 0 == t.move(1, 1, 2)
assert 0 == t.move(2, 0, 1)
assert 0 == t.move(1, 0, 2)
assert 1 == t.move(2, 1, 1)
assert 1 == t.move(1, 2, 1)
