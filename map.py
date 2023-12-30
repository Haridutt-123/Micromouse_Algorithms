#map = [['x' for i in range(16)] for i in range(16)] #For Graphs,trees
map_current = [[0 for _ in range(16)] for _ in range(16)]
map_visit_stat = [[False for _ in range(16)] for _ in range(16)]  #To mark cells that are visited
map_flood = [[14,13,12,11,10,9,8,7,7,8,9,10,11,12,13,14],
            [13,12,11,10,9,8,7,6,6,7,8,9,10,11,12,13],
            [12,11,10,9,8,7,6,5,5,6,7,8,9,10,11,12],
            [11,10,9,8,7,6,5,4,4,5,6,7,8,9,10,11],
            [10,9,8,7,6,5,4,3,3,4,5,6,7,8,9,10],
            [9,8,7,6,5,4,3,2,2,3,4,5,6,7,8,9],
            [8,7,6,5,4,3,2,1,1,2,3,4,5,6,7,8],
            [7,6,5,4,3,2,1,0,0,1,2,3,4,5,6,7],
            [7,6,5,4,3,2,1,0,0,1,2,3,4,5,6,7],
            [8,7,6,5,4,3,2,1,1,2,3,4,5,6,7,8],
            [9,8,7,6,5,4,3,2,2,3,4,5,6,7,8,9],
            [10,9,8,7,6,5,4,3,3,4,5,6,7,8,9,10],
            [11,10,9,8,7,6,5,4,4,5,6,7,8,9,10,11],
            [12,11,10,9,8,7,6,5,5,6,7,8,9,10,11,12],
            [13,12,11,10,9,8,7,6,6,7,8,9,10,11,12,13],
            [14,13,12,11,10,9,8,7,7,8,9,10,11,12,13,14]]
path = [["x" for _ in range(16)] for _ in range(16)]
wall_map = [ [[0,0,0,0] for _ in range (16)] for _ in range (16)]    #[UP wall,RIGHT wall,DOWN,LEFT] [NORTH,EAST,SOUTH,WEST]
n = len(map_flood)
m = len(map_flood[0])
#print(map_current)
queue = []
flood_src = [[7,7],[7,8],[8,7],[8,8]]
directions = [[-1,0],[0,1],[1,0],[0,-1]]
   
    
#floodfill()
#print("___________")
#print(map_current)                
  



'''Mistakes made:
l1 = l2 when l1,l2 are lists doesnt work, becomes a reference to l2.Changes made to l1 will reflect in l2 '''
