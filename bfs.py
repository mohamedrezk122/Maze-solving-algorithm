
def BFS(maze , start ,end):

    queue = [[start]]
    visited = []

    if start == end :
        print("same node idiot")
        return 

    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in visited:
            visited.append(node)
            neighbours = maze.G.neighbors(node)

            for neighbour in neighbours:
                solution = list(path)
                solution.append(neighbour)
                queue.append(solution)
                if neighbour == end:

                    return solution

            
    
    return "sorry no path :("      


        

