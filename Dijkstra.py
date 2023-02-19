from queue import PriorityQueue

from Graph import *


import heapq

def dijkstra(vertices, start):
    distances = {(v.index): float('inf') for v in vertices}
    distances[start.index] = 0
    pq = [(0, start.index)]

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        for vertex in vertices:
            if vertex.index == current_vertex:
                current = vertex
                break

        for neighbor_index, weight in current.neighbours:
            distance = current_distance + weight

            for vertex in vertices:
                if vertex.index == neighbor_index:
                    neighbor = vertex
                    break

            if distance < distances[neighbor.index]:
                distances[neighbor.index] = distance
                neighbor.parent = current
                heapq.heappush(pq, (distance, neighbor.index))

    return distances

def getShorthestPath(G, end, dist):
    if dist == float("inf"):
        return []
    path =[]
    end = G.vertex[end].parent
    for i in range(dist-1):
        path.append(end.index)
        end = end.parent
    return path



