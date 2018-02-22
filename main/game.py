import turtle
cell_size = 10

class newGame:

    def __init__(self, xlen, ylen):
        self.xlen = xlen
        self.ylen = ylen
        #State is set() type variable
        self.state = set()      

    def is_valid(self, x, y):
        "Returns true if the x,y coordinates are valid"
        return (0 <= x < self.xlen) and (0 <= y < self.ylen)

    def makeit_live(self, x, y):
        if not self.is_valid(x, y):
            raise ValueError("Not a valid cell")

        key = (x,y)
        self.state.add(key)

    def toggle_cell(self, x, y):
        "Make's live cell dead or dead cell alive"
        if not self.is_valid(x,y):
            raise ValueError("Not a valid cell")
        
        key = (x,y)
        if key in self.state:
            self.state.remove(key)
        else:
            self.state.add(key)

    def clear_board(self):
        self.state.clear()

    def step(self):
        "Compute one generation"
        temp_state = set()

        for i in range(self.xlen):
            x_range = range( max(0, i-1), min(self.xlen, i+2) )
            for j in range(self.ylen):
                s = 0
                live = ((i,j) in self.state)
                for ycord in range( max(0, j-1), min(self.ylen, j+2) ):
                    for xcord in x_range:
                        if (xcord, ycord) in self.state:
                            s += 1

                s -= live             
               
                if s == 3:
                    #If there are three live neighbours
                    temp_state.add((i,j))
                elif s == 2 and live: 
                    #If there are two live neighbours and the cell is alive
                    temp_state.add((i,j))
                elif live:
                    #If there are no neighbours for a live cell
                    pass

        self.state = temp_state

    def draw_cell(self, x, y):
        "Draw the cell (x,y) on the screen."
        turtle.penup()
        key = (x, y)
        if key in self.state:
            turtle.setpos(x*cell_size, y*cell_size)
            turtle.color('black')
            turtle.pendown()
            turtle.setheading(0)
            turtle.begin_fill()
            for i in range(4):
                turtle.forward(cell_size-1)
                turtle.left(90)
            turtle.end_fill()

    def display_board(self):
        "Display the whole board"
        turtle.clear()
        for i in range(self.xlen):
            for j in range(self.ylen):
                self.draw_cell(i, j)
        turtle.update()





    




        
        


    

