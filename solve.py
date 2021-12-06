from bfs import BFS
from PIL import Image
from maze import Maze
from track import Scene

image = Image.open("./images_in/tiny.png")
maze = Maze(image)

print(maze.count)

start = maze.node.index(maze.start)
end =  maze.node.index(maze.end)

def path():
    nodes = BFS(maze,start,end)
    solution = []
    new= []

    for sol in nodes:

        solution.append((maze.G.nodes[sol]['pos'][1] , maze.G.nodes[sol]['pos'][0]))


    x_old = solution[0][1]
    y_old = solution[0][0]
    for y,x in solution:

       if x == x_old:

           if y_old>y:
               for i in range(y_old , y-1 , -1):
                   new.append((i,x))if (i,x) not in new else None
           else:
               for i in range(y_old , y+1):
                   new.append((i,x))if (i,x) not in new else None
           y_old = y


       elif y == y_old:

           if x_old > x:
               for j in range(x_old , x-1 ,-1):
                   new.append((y,j)) if (y,j) not in new else None
           else:
               for j in range(x_old , x+1):
                   new.append((y,j)) if (y,j) not in new else None
           x_old = x

    return new
Scene(maze , path())
