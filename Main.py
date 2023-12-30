import API
import sys
import map

def log(string):
    sys.stderr.write("{}\n".format(string))
    sys.stderr.flush()

def turnBack():
    API.turnRight()
    API.turnRight()

def goTo(coord):
    #coordinates = [x for x in coord]
    x = coord[0]
    y = coord[1]
    currentPos = API.pos.copy()
    #currentPos = currentPos.copy()
    current_orient = API.orientation[API.pointer]
    difference = [currentPos[0]-x,currentPos[1]-y]
    if current_orient == 0 :     #tODO:Use shift function logic and improve  
        if difference == [0,1]:
            API.turnLeft()
        elif difference == [0,-1]:
            API.turnRight()
            #pass
        elif difference == [1,0]:
            #API.moveForward()
            pass
        elif difference == [-1,0]:
            turnBack()
    elif current_orient == 1:
        if difference == [1,0]:
            API.turnLeft()
        elif difference == [0,-1]:
            #API.moveForward()
            pass
        elif difference == [-1,0]:
            API.turnRight()
        elif difference == [0,1]:
            turnBack()    
    elif current_orient == 2:             #Check logic
        if difference == [0,1]:
            API.turnRight()
        elif difference == [0,-1]:
            API.turnLeft()
        elif difference == [-1,0]:
            #API.moveForward()
            pass
        elif difference == [1,0]:
            turnBack()
    elif current_orient == 3:
        if difference == [-1,0]:
            API.turnLeft()
        elif difference == [0,1]:
            #API.moveForward()
            pass
        elif difference == [1,0]:
            API.turnRight()                 #FInd alternate logic
        elif difference == [0,-1]:
            turnBack()    
    API.moveForward()

def shift(array,shift_num):  #Rotate/shidt array elements by shift_num
     length = len(array)
     for i, ele in enumerate(array[:]):
        array[(i + shift_num) % length] = ele
     return array
         

def wallset(coordinates):
    walls = [0,0,0,0]           #Walls from POV of Mouse
    #mouse_frame = [0,1,2,3]     Directions from frame of reference of mouse
    if API.wallFront():
        walls[0] = 1
    if API.wallRight():
        walls[1] = 1
    '''if API.wallBack():
        walls[2] = 1'''
    if API.wallLeft():
        walls[3] = 1
    shifted_array = shift(walls,API.pointer)
    map.wall_map[coordinates[0]][coordinates[1]] = shifted_array.copy() 
    adjust_walls(coordinates)  
    log(f"walls at {coordinates}:{map.wall_map[coordinates[0]][coordinates[1]]}")        

def adjust_walls(coordinates):
       x,y = coordinates[0],coordinates[1]
       walls = map.wall_map[x][y].copy()
       if walls[0]:
           if x-1>-1:
             map.wall_map[x-1][y][2] = 1
       if walls[1]:
           if y+1>16:
             map.wall_map[x][y+1][3] = 1
       if walls[2]:
           if x+1>16:
             map.wall_map[x-1][y][0] = 1
       if walls[3]:
           if y-1>-1:
             map.wall_map[x][y-1][1] = 1
           
def open_neighbours(coordinates):
    neighbours_list = []
    dirs = [[-1,0],[0,1],[1,0],[0,-1]]
    walls = map.wall_map[coordinates[0]][coordinates[1]].copy()
    print(walls)
    for i in range (4):
        neighbour = [0,0]
        if walls[i] == 0 :
            neighbour[0] = coordinates[0] + dirs[i][0]
            neighbour[1] = coordinates[1] + dirs[i][1]
            print(neighbour)
            if (-1 < neighbour[0] <16 and -1 < neighbour[1] <16):
              neighbours_list.append(neighbour)
    #log(neighbours_list)          
    return neighbours_list          
       

def modified_floodfill(coordinates):
    stack =[]
    flood_map = map.map_flood.copy() 
    stack.append(coordinates)
    while(len(stack)!=0):
        coord = stack.pop()
        open_cells = open_neighbours(coord)
        #print(open_cells)
        min_val_list = [flood_map[x][y] for x,y in open_cells]
        min_val = min(min_val_list)
        #log(min_val)
        if(flood_map[coord[0]][coord[1]] != 1 + min_val ):
            flood_map[coord[0]][coord[1]] = 1 + min_val
            log(f"{coord}:{flood_map[coord[0]][coord[1]]}")
            for open_neighbour in open_cells:
                stack.append(open_neighbour)

    map.map_flood = flood_map.copy()
    for i in range(16):
        for j in range(16):
             API.setText(i,j,map.map_flood[i][j])
    #log(map.map_flood)


def next_cell(coordinates):
    open_cells = open_neighbours(coordinates)
    flood_map = map.map_flood.copy()
    cell_vals = [flood_map[x][y] for x,y in open_cells]
    least_cell_pointer = 0
    min_cell_val = min(cell_vals)
    for x in range(len(cell_vals)):
        if cell_vals[x] == min_cell_val:
            least_cell_pointer = x
            log(f"Min cells:{open_cells[x]}")
    log(f"Next cell:{open_cells[least_cell_pointer]}")        
    return open_cells[least_cell_pointer]        
            
    

def main():
    log("Running...")
    API.setColor(0, 0, "G")
    API.setText(0, 0, "abc")
    program_status = True
    #API.moveForward()
    a = 0    
    while program_status:
       a+=1
       log(f"Loop counter:{a}")
       log(f"Current Pos:{API.pos}")
       r = API.pos.copy()
       map.path[r[0]][r[1]] = "p"
       wallset(API.pos)
           
       modified_floodfill(API.pos)
       
       l = next_cell(API.pos)
       goTo(l)
       log("\n")
      

       if(API.pos==[7,7] or API.pos==[7,8] or API.pos==[8,7] or API.pos==[8,8]):
            program_status = False
    log(map.map_flood)        
    for i in range(16):
        for j in range(16):
             API.setText(j,15-i,map.path[i][j])
             l = map.wall_map[i][j]
             if l[0] == 1:
                 API.setWall(j,15-i,'n')
             if l[1] == 1:
                 API.setWall(j,15-i,'e')
             if l[2] == 1:
                 API.setWall(j,15-i,'s')
             if l[3] == 1:
                 API.setWall(j,15-i,'w')
         
     

if __name__ == "__main__":
    main()

'''
def shift(lst, shft=0):
    ln = len(lst)
    for i, ele in enumerate(lst[:]):
        lst[(i + shft) % ln] = ele
    return lst
'''