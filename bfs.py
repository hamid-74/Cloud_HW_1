from random import *
import sys
import time

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

queue_length = 0


def bfs( visited, graph, node):
  visited.append(node)
  queue.append(node)
  queue_length = 0
  while queue:
    s = queue.pop(0) 
    queue_length = queue_length + 1
    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
  return queue_length


def random_graph_generator(n):
  random_graph = {}
  names = []

  for i in range(n):
    names.append('n' + str(i))


  for i in range(n):
    temp_list = []
    for j in range (n):
      if random() > 0.5:
        temp_list.append(names[j])
    random_graph[names[i]] = temp_list 
  return random_graph



graph = random_graph_generator(2**(int(sys.argv[1])))
 
# Driver Code
start_time = time.time()
queue_length = bfs(visited, graph, 'n0')
runtime =  (time.time() - start_time)
print("runtime --- %s seconds ---" % runtime)
print ("TEPS:" + str(queue_length/runtime) + "\n")

