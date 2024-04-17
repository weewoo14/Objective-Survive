from settings import *
level_outline = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                 [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                 [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                 [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                 [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                 [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
level1_map = [[] for idx in range(len(level_outline))]
for row in range(len(level_outline)):
    for col in range(len(level_outline[row])):
        if level_outline[row][col] == 1:
            level1_map[row].append((WHITE,(100*(col),100*(row),95,95)))
        elif level_outline[row][col] == 2:
            level1_map[row].append((GRAY,(100*(col),100*(row),95,95)))
        else:
            level1_map[row].append((BLACK,(100*(col),100*(row),95,95)))