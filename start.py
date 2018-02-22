from main import game
import sys
import random
import turtle
import json

cell_size = game.cell_size

def main():
    screen = turtle.Screen()
    xlen, ylen = screen.screensize()
    turtle.title("Game of Life")
    turtle.setworldcoordinates(0, 0, xlen, ylen)
    turtle.hideturtle()
    turtle.speed('fastest')
    turtle.tracer(0, 0)
    turtle.penup()

    continuous = False
    newBoard = game.newGame(xlen // cell_size, ylen // cell_size)

    # Load config from JSON
    def load_config():
        temp = set()
        with open('config.json') as json_data:
            json_parse = json.load(json_data)

        json_data = json_parse["live_cells"]
        for i in range(len(json_data)):
            cell = tuple(map(int,json_data[i][1:-1].split(',')))

            if newBoard.is_valid(cell[0], cell[1]):
                newBoard.toggle_cell(cell[0], cell[1])
                newBoard.display_board()

    # Set up mouse bindings
    def toggle(x, y):
        cell_x = x // game.cell_size
        cell_y = y // game.cell_size
        if newBoard.is_valid(cell_x, cell_y):
            newBoard.toggle_cell(cell_x, cell_y)
            newBoard.display_board()

    turtle.onscreenclick(turtle.listen)
    turtle.onscreenclick(toggle)
    newBoard.display_board()

    def clear_board():
        newBoard.clear()
        newBoard.display_board()

    def step_once():
        nonlocal continuous
        continuous = False
        perform_step()

    def step_continuous():
        nonlocal continuous
        continuous = True
        perform_step()

    def perform_step():
        newBoard.step()
        newBoard.display_board()

        if continuous:
            turtle.ontimer(perform_step, 25)

    # Setting up keybindings
    turtle.onkey(step_once, 's')
    turtle.onkey(step_continuous, 'c')
    turtle.onkey(clear_board, 'e')
    turtle.onkey(sys.exit, 'q')
    turtle.onkey(load_config, 'l')

    turtle.listen()
    turtle.mainloop()

if __name__ == '__main__':
    main()