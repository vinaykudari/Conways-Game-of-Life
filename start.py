from main import game
import sys
import random
import turtle

cell_size = game.cell_size

def main():
    screen = turtle.Screen()
    xlen, ylen = screen.screensize()
    turtle.setworldcoordinates(0, 0, xlen, ylen)
    turtle.hideturtle()
    turtle.speed('fastest')
    turtle.tracer(0, 0)
    turtle.penup()

    newBoard = game.newGame(xlen // cell_size, ylen // cell_size)

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

    # Set up key bindings
    def erase():
        newBoard.clear()
        newBoard.display_board()
    turtle.onkey(erase, 'e')

    turtle.onkey(sys.exit, 'q')

    # Set up keys for performing generation steps, either one-at-a-time or not.
    continuous = False
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
        # In continuous mode, we set a timer to display another generation
        # after 25 millisenconds.
        if continuous:
            turtle.ontimer(perform_step, 25)

    turtle.onkey(step_once, 's')
    turtle.onkey(step_continuous, 'c')

    # Enter the Tk main loop
    turtle.listen()
    turtle.mainloop()


if __name__ == '__main__':
    main()