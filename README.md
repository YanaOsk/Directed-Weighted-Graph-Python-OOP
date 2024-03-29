# Directed Weighted Graph Python
![weight01](https://user-images.githubusercontent.com/69717074/147417650-99c6265c-b1db-4134-a3c7-08f6bf872e09.gif)

As in the previous assignment, we were asked to work with a directed and weighted graph. In fact, this task, is to "translate" the previous task into the Python language, but there was a lot of work on the changes that arise from the differences of languages. While working on the task we discovered a lot of things we did not know we could do in Python. Let's start by explaining.
We got two interfaces - the first creates the graph, the second an interface that works on the algorithms that run on graphs. In fact, there is really no such thing as interfaces in Python, these are actually abstract classes that we had to inherit.
We have created 2 classes that inherit from the interfaces
## DiGraph - We will detail the class and what each function does :

We created a constructor, which gets the number of vertices, the number of sides, a counter, and a dictionary of vertices that will contain in the key the ID of the vertex and in value the information about the vertex.

|Function name | Explanation |
|--------------|-------------|
| v_size | Function returns the number of vertices in the graph |
| e_size | Returns the number of sides in the graph |
| get_all_v | A function that returns to us the dictionary of vertices that contains all the information |
| all_in_edges_of_node | A function that returns a dictionary, where in this key the ID of the vertex and value is all the vertices connected to it (if there is one) |
| all_out_edges_of_node | A function like the previous one, only it returns the vertices that come out of a vertex |
| get_mc | A function by which we count every change we make in the construction of the graph, such as adding a side, deleting a side, adding a vertex, etc. |
| add_edge | A function that adds a side to a graph, since we did not have a side object but only a vertex, we had to work with both dictionaries and vertex objects that could simulate us sides. So when adding a edge we had to put the source in the inEdges dictionary and the destination in the outEdges and coordinate between them. |
| add_node | A function that adds a vertex to a graph |
| remove_node | A function that deletes the vertex from the grap . |
| remove_edge | A function that deletes the side, that is, deletes them from both dictionaries the source and the destination. And print functions. |

## GraphAlgo class that contains algorithms and the GUI:

Contains the constructor that builds the graph through the DiGraph class

|Function name | Explanation |
|--------------|-------------|
| get_ graph | A function that returns the graph |
| load_from_json | A function that loads a json file and converts it to an object through a dictionary. We referred to the condition of a T0 file, which has nothing in it except the id of the vertex, which knew how to accept such files as well and create objects from them. |
| save_to_json  | A function that saves us the graph for a new json file. In its operation each time overwrites the previous file. |
| shortest_path | A function that calculates for us the shortest route from source vertex to destination vertex. We used the dijkstra algorithm which is detailed below. |
| tsp | A function that calculates for us the shortest path to pass between all vertices, we used it in the FloydWarshall algorithm which we will explain later. |
| center | A function that calculates the most central vertex, from which the other vertices can be reached in the "cheapest" way. |
| plot_graph | A function that emits the graph in the GUI that we will detail below. |

## Algorithms we used :

### Dijkstra :

The algorith we took from some youtube videos : 

https://www.youtube.com/watch?v=pVfj6mxhdMw

https://www.youtube.com/watch?v=XB4MIexjvY0

https://www.youtube.com/watch?v=EFg3u_E6eHU

and the algorithm from the wikipedia:


Let the node at which we are starting at be called the initial node. Let the distance of node Y be the distance from the initial node to Y. Dijkstra's algorithm will initially start with infinite distances and will try to improve them step by step.

Mark all nodes unvisited. Create a set of all the unvisited nodes called the unvisited set.
Assign to every node a tentative distance value: set it to zero for our initial node and to infinity for all other nodes. The tentative distance of a node v is the length of the shortest path discovered so far between the node v and the starting node. Since initially no path is known to any other vertex than the source itself (which is a path of length zero), all other tentative distances are initially set to infinity. Set the initial node as current.
For the current node, consider all of its unvisited neighbors and calculate their tentative distances through the current node. Compare the newly calculated tentative distance to the current assigned value and assign the smaller one. For example, if the current node A is marked with a distance of 6, and the edge connecting it with a neighbor B has length 2, then the distance to B through A will be 6 + 2 = 8. If B was previously marked with a distance greater than 8 then change it to 8. Otherwise, the current value will be kept.
When we are done considering all of the unvisited neighbors of the current node, mark the current node as visited and remove it from the unvisited set. A visited node will never be checked again.
If the destination node has been marked visited (when planning a route between two specific nodes) or if the smallest tentative distance among the nodes in the unvisited set is infinity (when planning a complete traversal; occurs when there is no connection between the initial node and remaining unvisited nodes), then stop. The algorithm has finished.
Otherwise, select the unvisited node that is marked with the smallest tentative distance, set it as the new current node, and go back to step 3.

### Floyd Warshall algorithm :

https://www.youtube.com/watch?v=4OQeCuLYj-4

and the algorithm from GeeksForGeeks site:

We initialize the solution matrix same as the input graph matrix as a first step. Then we update the solution matrix by considering all vertices as an intermediate vertex. The idea is to one by one pick all vertices and updates all shortest paths which include the picked vertex as an intermediate vertex in the shortest path. When we pick vertex number k as an intermediate vertex, we already have considered vertices {0, 1, 2, .. k-1} as intermediate vertices. For every pair (i, j) of the source and destination vertices respectively, there are two possible cases. 
1) k is not an intermediate vertex in shortest path from i to j. We keep the value of dist[i][j] as it is. 
2) k is an intermediate vertex in shortest path from i to j. We update the value of dist[i][j] as dist[i][k] + dist[k][j] if dist[i][j] > dist[i][k] + dist[k][j]
The following figure shows the above optimal substructure property in the all-pairs shortest path problem.

## Node

Also we created Node class, that holds node object.
There is a constructor that gets id, pos, tag, weight, inEdges, outEdges
Since we did not have an edge object, we used vertex information with the dictionaries.
pos , tag and weight - have default values in the constructor.

# GUI 

## In the GUI we decided to use the pygame platform.

Within the plot_graph function, we have written some functions that will help us deal with graph printing to the screen.
First we encountered a problem with the T0 file that does not have the coordinates, so there was no way to place the graph,
so we randomly created the coordinates for it and inserted it into the object of the code code.
In addition to this we have created 4 functions that will help us with the resolution of the screen, since the coordinates are very close to each other.
In fact as in the previous task, we created the highest and lowest x and y, to do the zoom in the right place, i.e. between these coordinates and use the space between them.
In addition to that we had to show arrows of a graph so we created a function that would draw our arrows at the right angle with the direction of the edges,
we had to do a mathematical calculation for it to work. In addition we created a screen we filled it with vertices and ribs in their correct position.

## Graphs we get from our GUI:

_T0_

<img src="https://user-images.githubusercontent.com/69717074/147419042-becb1be7-8a51-4ccd-9fad-5bcf6944813b.png" width="450">


_A0_

<img src="https://user-images.githubusercontent.com/69717074/147419045-78be1b13-5c74-44f4-a1ac-46f93df5bfc1.png" width="450">


_A1_

<img src="https://user-images.githubusercontent.com/69717074/147419050-edde9207-a0d2-47fd-86bb-167701752dd8.png" width="450">


_A2_

<img src="https://user-images.githubusercontent.com/69717074/147419053-368dfb0c-acfd-44bc-bc3a-560c2aca3b0b.png" width="450">


_A3_

<img src="https://user-images.githubusercontent.com/69717074/147419065-f70dc709-acbf-49cc-843a-ae9cf2800556.png" width="450">


_A4_

<img src="https://user-images.githubusercontent.com/69717074/147419070-8ef054ee-502c-46c5-be4f-e493e9cc3bca.png" width="450">


_A5_

<img src="https://user-images.githubusercontent.com/69717074/147419075-8209c0e3-ca18-415c-86a2-1f8886b4337a.png" width="450">

# Tests

Also we made a test's for all classes and the functions that we made. The tests will check the correctness of the code and algorithms.

# Run our code 

You can run our code from the main by the  check() function
also you can run it from GraphAlgo class.




