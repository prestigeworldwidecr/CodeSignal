'''

Great progress on your learning journey! Now it's time to apply what you've learned about traversing through adjacent cells in a grid. In this task, you'll work with a metaphorical mountain, where each cell value represents the elevation at that point. Your goal is to continue the hike from a specified starting point, always moving to the adjacent cell with a higher elevation. Please fill in the missing code to complete the trek.

'''

import sys

def trek_path(elevation_map, start_x, start_y) :
# {
    possible_moves = [None]
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # East, South, West, North
    path = [elevation_map[start_x][start_y]]
    # flag = True

    # Pre-completed: Find all possible moves from the current position, moving only to higher and not yet visited elevations.
    while(True) :
    # {
        current_height = path[-1]

        # print(current_height)

        # Pre-completed: Find all possible moves from the current position, moving only to higher and not yet visited elevations.
        possible_moves = [(start_x + dx, start_y + dy) for dx, dy in directions
                            if (0 <= start_x + dx < len(elevation_map) and
                                0 <= start_y + dy < len(elevation_map[0]) and
                                elevation_map[start_x + dx][start_y + dy] > current_height)
                        ]

        if (not possible_moves) :
        # {
            break
        # }

        else :
        # {
            None
        # }

        # TODO: Implement logic to select the next position based on the highest elevation in the possible moves.

        # Hint: Use a key function with the max() function to find the move leading to the highest elevation.  
        # print(max(possible_moves, key=lambda pos: elevation_map[pos[0]][pos[1]]))
        # path.append()
        # start_x = possible_moves[len(possible_moves) - 1][0]
        # start_y = possible_moves[len(possible_moves) - 1][1]
        start_x = possible_moves[max(possible_moves, key=lambda pos: elevation_map[pos[0]][pos[1]])][0]
        start_y = possible_moves[max(possible_moves, key=lambda pos: elevation_map[pos[0]][pos[1]])][1]
        path.append(elevation_map[start_x][start_y])
        
    # }

    return path

# }

mountain = [
                [1, 2, 3],
                [2, 3, 4],
                [3, 5, 6]
            ]

print(trek_path(mountain, 1, 1))

'''

***** BONEYARD *****

possible_moves = [
                            (start_x + dx, start_y + dy) for dx, dy in directions
                            if (0 <= start_x + dx < len(elevation_map) and
                                0 <= start_y + dy < len(elevation_map[0]) and
                                elevation_map[start_x + dx][start_y + dy] > current_height)
                        ]


    
    print(possible_moves)

    while (False) :
    # {
        current_height = path[-1]
        
        # TODO: Implement logic to select the next position based on the highest elevation in the possible moves.
        # Hint: Use a key function with the max() function to find the move leading to the highest elevation.
        if (possible_moves) :
        # {
            None
        # }

        else :
        # {
            None # break
        # }

    # }       
    

            # print("hi!")
            
        # current_height = path[-1]
        # possible_moves
        
    # print(path[-1])

    # print(len(possible_moves))
    # path = [elevation_map[start_x][start_y]]
    

        # print((start_x + dx, start_y + dy))

                # print(max(possible_moves))
                # path.append(max_elevation)
                # start_x = start_x + dx
                # start_y = start_y + dy
                # print('!', len(possible_moves), max_elevation)
                # print(elevation_map[start_x + dx][start_y + dy])    
        # print('!', len(possible_moves), max_elevation)                     

# max_elevation = -sys.maxsize        



# path.append(max_elevation)
    # path.pop() 
    # return path
                                
for dx, dy in directions :
        # {            
        # }


        if (possible_moves[0] is None) :
        # {
            possible_moves.pop()
        # }

        else :
        # {
            None
        # }
        possible_moves.pop()

        possible_moves.append((start_x + dx, start_y + dy))
            key = lambda possible_moves: elevation_map[[start_x + dx][start_y + dy]]
            print(key)

        # start_x = start_x + dx
        # start_y = start_y + dy            

# max_elevation = elevation_map[start_x + dx][start_y + dy]
                # max_elevation = max(possible_moves)        

possible_moves = [
                            (start_x + dx, start_y + dy) for dx, dy in directions
                            if (0 <= start_x + dx < len(elevation_map) and
                                0 <= start_y + dy < len(elevation_map[0]) and
                                elevation_map[start_x + dx][start_y + dy] > current_height)
                        ]
                        
for dx, dy in directions :
        # {
            possible_moves = [None]
            # print(elevation_map[start_x + dx][start_y + dy], current_height)

            if (0 <= start_x + dx < len(elevation_map) and 0 <= start_y + dy < len(elevation_map[0]) and elevation_map[start_x + dx][start_y + dy] > current_height) :
            # {
                possible_moves.append((start_x + dx, start_y + dy))
            # }

            else :
            # {
                # possible_moves.pop()
                None
            # }

        # }

if (possible_moves) :
        # {            
            None
        # }

        else :
        # {
            flag = False
        # }        

'''
