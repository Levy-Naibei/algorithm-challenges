""" Given the total number of rows and columns in the theater (nRows and nCols, respectively),
 and the row and column you're sitting in, return the number of people who sit strictly behind you 
 and in your column or to the left, assuming all seats are occupied"""

def seats_in_theater(nCols, nRows, col, row):
    # Calculates the number of people to the right of you in your row. 
    # col - column you are sitting in
    # nCols - col + 1: Adds 1 to include yourself in the count.
    people_in_your_row = nCols - col + 1
    
    # This part calculates the number of rows starting from the row you are sitting in 
    # and going towards the back of the theater.
    people_behind_you = nRows - row
    
    # Calculate the total number of people behind you and in your column or to the left
    total_people = people_in_your_row * people_behind_you
    
    return total_people
