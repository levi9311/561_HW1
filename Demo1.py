import Queue

class node:
	""" 
		Store information of node(including node_name and connect information)

	"""
	def __init__(self, name):
		""" init class with name """
		self.name = name
		self.pre_node = []
		self.neighbors = []
		self.sunday_cost = 0

	def add_neighbor(self, node_name, cost):
		""" add a connect node with cost """
		self.neighbors.append = (node_name, cost)

	def add_sundayInfo(self, cost):
		""" add sunday traffic cost information """
		self.sunday_cost = cost


class queue_item:
	""" 
		queue_items contain the information of routes

	"""

	def __init__(self, name, routes, cost = 0):
		self.name = name
		self.routes = routes
		self.cost = cost

	def add_cost(cost):
		self.cost = self.cost + cost

class priority_queue:
	"""
		the queue with priority

	"""
	def __init__(self):
		self.list = []

	def put(self, queue_item):
		if self.list.empty():
			self.list.append(queue_item)
			return
		flag = 0
		for i in range(len(self.list)):
			if queue_item.name == self.list[i].name:
				if queue_item.cost < self.list[i].cost:
					self.list[i] = queue_item
					flag = 1
				else
					flag = 1

		if flag == 0:
			self.list.append(queue_item)

		self.list.sort(key = lambda x: x.cost)

	def get(self):
		temp = self.list[0]
		del self.list[0]
		return temp



def BFS(NODE_LIST, START, GOAL):
	""" BFS strategy """
<<<<<<< HEAD
	EXPLORED_LIST = []
	node_queue = Queue.Queue()
=======
	node_queue = Queue.LifoQueue()
>>>>>>> origin/master
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
<<<<<<< HEAD
			temp_item = queue_item(i, temp.routes + '#' + temp.name, temp.cost + NODE_LIST[temp.name].neighbors[i])
=======
			temp_item = queue_item(i[0], temp.routes + '#' + temp.name)
>>>>>>> origin/master
			node_queue.put(temp_item)

	return ''

def DFS(NODE_LIST, START, GOAL):
<<<<<<< HEAD
	""" DFS strategy """
	EXPLORED_LIST = []
	node_queue = Queue.LifoQueue()
=======
	""" BFS strategy """
	node_queue = Queue.Queue()
>>>>>>> origin/master
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
			temp_item = queue_item(i[0], temp.routes + '#' + temp.name)
			node_queue.put(temp_item)

	return ''

<<<<<<< HEAD
def UCS(NODE_LIST, START, GOAL):
	""" UCS strategy """
	node_queue = priority_queue()
	new_start = queue_item(START, '')
	node_queue.put(new_start)



=======
>>>>>>> origin/master
file_reader = open('input.txt', 'r')

strategy = file_reader.readline().strip()
START = file_reader.readline().strip()
GOAL = file_reader.readline().strip()
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
