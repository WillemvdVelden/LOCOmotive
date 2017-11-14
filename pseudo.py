procedure DFS(graph, station):
    label station as discovered
    for all edges from station to station2 in G.adjacentEdges(station) do
        if edge is not labeled as discovered then
            recursively call DFS(graph, station2)