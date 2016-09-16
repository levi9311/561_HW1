import Queue

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


class queue_item:
	""" 
		queue_items contain the information of routes

	"""

	def __init__(self, name, routes):
		self.name = name
		self.routes = routes
		self.cost = 0

	def add_cost(cost):
		self.cost = self.cost + cost



def BFS(NODE_LIST, START, GOAL):
	""" BFS strategy """
	node_queue = Queue.Queue()
	new_start = queue_item(START, '')
	node_queue.put(new_start)
	while not node_queue.empty():
		temp = node_queue.get()
		if temp.name in EXPLORED_LIST:
			continue
		EXPLORED_LIST.append(temp.name)
		if temp.name == GOAL:
			return temp.routes + '#' + GOAL
		for i in NODE_LIST[temp.name].neighbors:
			temp_item = queue_item(i, temp.routes + '#' + temp.name)
			node_queue.put(temp_item)

	return ''

def DFS(NODE_LIST, START, GOAL):
	""" DFS strategy """
	node_queue = Queue.LifoQueue()
	new_start = queue_item(START, '')
	node_queue.put(new_start)
	while not node_queue.empty():
		temp = node_queue.get()
		if temp.name in EXPLORED_LIST:
			continue
		EXPLORED_LIST.append(temp.name)
		if temp.name == GOAL:
			return temp.routes + '#' + GOAL
		for i in NODE_LIST[temp.name].neighbors:
			temp_item = queue_item(i, temp.routes + '#' + temp.name)
			node_queue.put(temp_item)

	return ''

def 

file_reader = open('input.txt', 'r')

strategy = file_reader.readline().strip()
START = file_reader.readline().strip()
GOAL = file_reader.readline().strip()
count = int(file_reader.readline())

NODE_LIST = {}
EXPLORED_LIST = []

# generate the graph
for i in range(count):
	live_route = file_reader.readline().split()
	STATE1 = live_route[0]
	STATE2 = live_route[1]
	COST = int(live_route[2])
	if STATE1 not in NODE_LIST:
		new_node = node(STATE1)
		NODE_LIST[STATE1] = new_node	
	if STATE2 not in NODE_LIST:
		new_node = node(STATE2)
		NODE_LIST[STATE2] = new_node
	NODE_LIST[STATE1].add_neighbor(STATE2, COST)

count_sun = int(file_reader.readline())

# import the sunday traffic information
for i in range(count_sun):
	sunday_route = file_reader.readline().split()
	STATE = sunday_route[0]
	COST = int(sunday_route[1])
	NODE_LIST[STATE].add_sundayInfo(COST)

if strategy == 'BFS':
	print BFS(NODE_LIST, START, GOAL)

if strategy == 'DFS':
	print DFS(NODE_LIST, START, GOAL)




a = node('road')
b = [a]
if a in b:
	a.add_neighbor('A', 34)
	a.add_neighbor('B', 34)
