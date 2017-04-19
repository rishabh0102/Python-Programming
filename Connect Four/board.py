class Board:
    """ a datatype representing a C4 board
        with an arbitrary number of rows and cols
    """

    def __init__(self, height, width):
        """ the constructor for objects of type Board """
        self.height = height
        self.width = width

        # self.slots[row][col]
        self.slots = [[' ' for x in range(width)] for y in range(height)]

    def __repr__(self):
        """ Returns a string representation for a Board object.
        """
        s = ''         # begin with an empty string

        # add one row of slots at a time
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        # Add code here for the hyphens at the bottom of the board
        # and the numbers underneath it.

        s += '--'*self.width    # add the bottom of the board
        s += '-\n'
        
        for col in range( self.width ):
            s += ' ' + str(col%10)

        s += '\n'
        return s
        
    def add_checker(self, checker, col):
        """ put your docstring here
        """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)

        # put the rest of the method here
        row = self.height - 1
        while self.slots[row][col] != ' ':
            row += -1
        self.slots[row][col] = checker

    def reset(self):
        """ the software version of the little
            blue slider that releases all of the checkers!
        """
        self.slots = [[' ' for x in range(self.width)] for y in range(self.height)]

    def add_checkers(self, col_nums):
        """ takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object, 
            starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in col_nums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    def can_add_to(self, col):
        """ returns True if a move to col is allowed
            in the board represented by self
            returns False otherwise
        """
        if col < 0 or col >= self.width:
            return False
        return self.slots[0][col] == ' '

    def is_full(self):
        """ returns True if the board is completely full """
        for col in range(self.width):
            if self.can_add_to(col):
                return False
        return True

    def remove_checker(self, col):
        """ removes the checker from column col """
        for row in range(self.height):
            # look for the first nonempty row
            if self.slots[row][col] != ' ':
                # put in the checker
                self.slots[row][col] = ' '
                return

    def is_checker(self, row, col, checker):
        """ checks if the spot at row, col is legal and the same checker """
        if 0 <= row < self.height:
            if 0 <= col < self.width: # legal...
                if self.slots[row][col] == checker:
                    return True
        return False

    def is_win_for(self, checker):
        """ checks if the board self is a win for ox """
        assert(checker == 'X' or checker == 'O')

        for row in range(self.height):
            for col in range(self.width):
                if self.is_checker(row, col, checker) and \
                   self.is_checker(row+1, col, checker) and \
                   self.is_checker(row+2, col, checker) and \
                   self.is_checker(row+3, col, checker):
                    return True
                if self.is_checker(row, col, checker) and \
                   self.is_checker(row, col+1, checker) and \
                   self.is_checker(row, col+2, checker) and \
                   self.is_checker(row, col+3, checker):
                    return True
                if self.is_checker(row, col, checker) and \
                   self.is_checker(row+1, col+1, checker) and \
                   self.is_checker(row+2, col+2, checker) and \
                   self.is_checker(row+3, col+3, checker):
                    return True
                if self.is_checker(row, col, checker) and \
                   self.is_checker(row+1, col-1, checker) and \
                   self.is_checker(row+2, col-2, checker) and \
                   self.is_checker(row+3, col-3, checker):
                    return True
        return False





