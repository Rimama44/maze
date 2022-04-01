from collections import deque
import sys
import colorama
from colorama import Fore, Back, Style

row = [-1, 0, 0, 1]
col = [0, -1, 1, 0]

def getStartIndex(maze):
    for j,i in enumerate(maze):
         if i.count("1") > 0:
               return (j, i.index('1'))

def getEndIndex(maze):
    for j,i in enumerate(maze):
         if i.count("2") > 0:
               return (j, i.index('2'))

def draw_maze(maze, start):
    maze[start[0]][start[1]] = "1"
    for row in maze:
        for item in row:
            if item == "*":
                print(Fore.WHITE, item, end='')
            elif item == " ":
                print(Fore.RESET, item, end='')
            elif item == "+":
                print(Fore.GREEN, item, end='')
            elif item == "2" or item == "1":
                print(Fore.RED, item, end='')
        print()

def correct_position(maze, pos_r, pos_c):
    if pos_r < 0 or pos_c < 0:
        return False
    if pos_r >= len(maze) or pos_c >= len(maze[0]):
        return False
    if maze[pos_r][pos_c] in ' 2':
        return True
    return False

def solver(maze, start):
    position = deque()
    position.append(start)
    while len(position) > 0:
        pos_r, pos_c = position.pop()
        if maze[pos_r][pos_c] == '2':
            return print("Path to goal found !")
        if maze[pos_r][pos_c] == '+' :
            continue
        else: maze[pos_r][pos_c] = '+'

        if correct_position(maze, pos_r - 1, pos_c):
            position.append((pos_r - 1, pos_c))
        if correct_position(maze, pos_r + 1, pos_c):
            position.append((pos_r + 1, pos_c))
        if correct_position(maze, pos_r, pos_c - 1):
            position.append((pos_r, pos_c - 1))
        if correct_position(maze, pos_r, pos_c + 1):
            position.append((pos_r, pos_c + 1))
    
    return print("No path found...")

# MAIN ALGORITHM

mazemap = [line.strip() for line in open("maps/rect_04.map", 'r')]
maze = [list(i) for i in mazemap]

start = getStartIndex(maze)
end = getEndIndex(maze)
draw_maze(maze, start)
solver(maze, start)
draw_maze(maze, start)