import queue

class node:
	""" 
		Store information of node(including node_name and connect information)

	"""

	def __init__(self, name):
		""" init class with name """
		self.name = name
		self.pre_node = []
		self.neighbors = {}
		self.sunday_cost = 0

	def add_neighbor(self, node_name, cost):
		""" add a connect node with cost """
		self.neighbors[node_name] = cost

	def add_sundayInfo(self, cost):
		""" add sunday traffic cost information """
		self.sunday_cost = cost

file_reader = open('input.txt', 'r')

strategy = file_reader.readline()
START = file_reader.readline()
GOAL = file_reader.readline()
count = int(file_reader.readline())

NODE_LIST = {}

# generate the graph
for i in range(count):
	live_route = file_reader.readline().split()
	STATE1 = live_route[0]
	STATE2 = live_route[1]
	COST = int(live_route[2])
	if STATE1 not in NODE_LIST:
		new_node = node(STATE1)
		NODE_LIST[STATE1] = new_node	
		print NODE_LIST
	if STATE2 not in NODE_LIST:
		new_node = node(STATE1)
		NODE_LIST[STATE1] = new_node
		print NODE_LIST
	NODE_LIST[STATE1].add_neighbor(STATE2, COST)

count_sun = int(file_reader.readline())

# import the sunday traffic information
for i in range(count_sun):
	sunday_route = file_reader.readline().split()
	STATE = sunday_route[0]
	COST = sunday_route[1]
	NODE_LIST[STATE].add_sundayInfo(COST)


def BFS(NODE_LIST, START, GOAL):
	""" BFS strategy """
	node_queue = Queue.Queue()
	node_queue.put(START)
	while not node_queue.empty():
		temp = node_queue.get()
		if temp == GOAL:
			break;


a = node('road')
b = [a]
if a in b:
	a.add_neighbor('A', 34)
	a.add_neighbor('B', 34)
