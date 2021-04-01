import numpy as np
from random import randint
import time
import os

class Board:
    board = []
    boardAux = []

    def create_board(self, row, column):
        matrix = np.zeros((row, column), dtype=int)
        matrix[2, 5] = 1
        matrix[3, 6] = 1
        matrix[3, 6] = 1
        matrix[4, 6] = 1
        matrix[4, 5] = 1
        matrix[4, 4] = 1
        return matrix

    def check_neighbours(self, row_check, column_check):
        neighbours = self.count_neighbours(row_check, column_check)
        if  self.boardAux[row_check][column_check] == 0:
            if neighbours == 3:
                self.boardAux[row_check][column_check] = 1

        if self.boardAux[row_check][column_check] == 1:
            if neighbours > 3 or neighbours < 2:
                self.boardAux[row_check][column_check] = 0
            if neighbours == 2 or neighbours == 3:
                self.boardAux[row_check][column_check] = 1

    def count_neighbours(self, row_check, column_check):
        neighbours = 0
        x = row_check
        y = column_check
        x2 = row_check
        y2 = column_check

        if row_check+1 == 10:
            x=-1
        if row_check-1 == -1:
            x2=10
        if column_check+1 == 10:
            y=-1
        if column_check-1 == -1:
            y2=10

        if self.board[x2-1][y] != 0:
            neighbours = neighbours+1
        if self.board[x][y2-1] != 0:
            neighbours = neighbours+1
        if self.board[x2-1][y2-1] != 0:
            neighbours = neighbours+1
        if self.board[x+1][y] != 0:
            neighbours = neighbours+1
        if self.board[x][y+1] != 0:
            neighbours = neighbours+1
        if self.board[x+1][y+1] != 0:
            neighbours = neighbours+1
        if self.board[x+1][y2-1] != 0:
            neighbours = neighbours+1
        if self.board[x2-1][y+1] != 0:
            neighbours = neighbours+1
        return neighbours

    def count_status(self):
        status_dead = 0
        status_alive = 0
        for x in range(len(self.boardAux)):
            for y in range(len(self.boardAux)):
                if self.boardAux[x][y] == 1:
                    status_alive=status_alive+1
                if self.boardAux[x][y] == 0:
                    status_dead=status_dead+1
        return status_dead, status_alive

    def check_status(self, status_dead):
        rows = len(self.boardAux)
        columns = len(self.boardAux[0])
        q_total = rows*columns
        print("Cells: {}".format(q_total))
        if q_total == status_dead:
            print("All cells are dead. Program is going to done.")
            time.sleep(1)
            sys.exit()
        else:
            pass

    def main(self):
        print("\n"*5)
        row = int(input("Insert q rows: "))
        col = int(input("Insert q cols: "))
        self.board = self.create_board(row, col)
        self.boardAux = self.create_board(row, col)
        for x in range(row):
            for y in range(col):
                self.boardAux[x][y] = self.board[x][y]
        #
        print("First model:\n{}".format(self.board))
        print('\n')
        time.sleep(2)
        i=0
        try:
            while True:
                i=i+1
                for x in range(row):
                    for y in range(col):
                        self.check_neighbours(x, y)
                for x in range(row):
                    for y in range(col):
                        self.board[x][y] = self.boardAux[x][y]
                status = self.count_status()
                self.check_status(status[0])
                print("Generation {}:\n{}\nCells dead: {}\nCells alive: {}".format(i, self.boardAux, status[0], status[1]))
                print('\n')
                time.sleep(1)
        except (KeyboardInterrupt):
            print("\n- Evolutions done with keyboard - \n Results:\n {} generations\n {} cells alive\n {} cells dead\n----------------".format(i, status[1], status[0]))

board = Board()
board.main()
