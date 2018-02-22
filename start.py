from main import game
import sys
import random
import turtle
import json

cell_size = game.cell_size

def main():
    print("\nWelcome to Game of Life\n\nPress l to load from config \nPress space to start the game\nPress s to pause the game \nPress q to quit the game ")
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
        temp_state = set()
        with open('config.json') as json_data:
            json_parse = json.load(json_data)

        json_data = json_parse["live_cells"]

        for i in range(len(json_data)):
            temp_val = tuple(map(int,json_data[i][1:-1].split(',')))
            temp_state.add(temp_val)

        for i in temp_state:
            if newBoard.is_valid(i[0], i[1]):
                newBoard.toggle_cell(i[0], i[1])
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
        newBoard.clear_board()
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
    
    turtle.onkey(step_continuous, 'space')
    turtle.onkey(clear_board, 'c')
    turtle.onkey(sys.exit, 'q')
    turtle.onkey(load_config, 'l')
    turtle.onkey(step_once, 's')

    turtle.listen()
    turtle.mainloop()

if __name__ == '__main__':
    main()