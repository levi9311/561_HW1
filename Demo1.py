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
		self.neighbors.append((node_name, cost))

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
		self.qlist = []

	def put(self, queue_item):
		''' put node in queue ordered by path cost '''
		print 'before: ' + str(self.qlist)
		if not self.qlist:
			self.qlist.append(queue_item)
			return
		flag = 0
		for i in range(len(self.qlist)):
			if queue_item.name == self.qlist[i].name:
				if queue_item.cost < self.qlist[i].cost:
					self.qlist[i] = queue_item
					flag = 1
				else: 
					flag = 1

		if flag == 0:
			self.qlist.append(queue_item)

		# sort by path cost
		self.qlist.sort(key = lambda x: x.cost)
		print 'after:'
		for i in self.qlist:
			print i.name + ' ' + str(i.cost)

	def get(self):
		temp = self.qlist[0]
		del self.qlist[0]
		return temp

	def empty(self):
		flag = False
		if len(self.qlist) == 0:
			flag = True 
		return flag


def BFS(NODE_LIST, START, GOAL):
	""" BFS strategy """
	EXPLORED_LIST = []
	node_queue = Queue.Queue()
	new_start = queue_item(START, '')
	node_queue.put(new_start)
	while not node_queue.empty():
		temp = node_queue.get()
		if temp.name in EXPLORED_LIST:
			continue
		EXPLORED_LIST.append(temp.name)
		if temp.name == GOAL:
			return (temp.routes + '#' + temp.name, temp.cost)
		for i in NODE_LIST[temp.name].neighbors:
			temp_item = queue_item(i[0], temp.routes + '#' + temp.name, temp.cost + 1)
			node_queue.put(temp_item)

	return ''

def DFS(NODE_LIST, START, GOAL):
	""" DFS strategy """
	EXPLORED_LIST = []
	node_queue = Queue.LifoQueue()
	new_start = queue_item(START, '')
	node_queue.put(new_start)
	while not node_queue.empty():
		temp = node_queue.get()
		if temp.name in EXPLORED_LIST:
			continue
		EXPLORED_LIST.append(temp.name)
		if temp.name == GOAL:
			return (temp.routes + '#' + temp.name, temp.cost)
		NODE_LIST[temp.name].neighbors.reverse()
		for i in NODE_LIST[temp.name].neighbors:
			print str(i) + ' ' + str(temp.name)
			temp_item = queue_item(i[0], temp.routes + '#' + temp.name, temp.cost + 1)
			node_queue.put(temp_item)

	return ''

def UCS(NODE_LIST, START, GOAL):
	""" UCS strategy """
	EXPLORED_LIST = []
	node_queue = priority_queue()
	new_start = queue_item(START, '')
	node_queue.put(new_start)
	while not node_queue.empty():
		temp = node_queue.get()
		if temp.name in EXPLORED_LIST:
			continue
		EXPLORED_LIST.append(temp.name)
		if temp.name == GOAL:
			return (temp.routes + '#' + temp.name, temp.cost)
		for i in NODE_LIST[temp.name].neighbors:
			temp_item = queue_item(i[0], temp.routes + '#' + temp.name, temp.cost + i[1])
			node_queue.put(temp_item)

	return ''

def A_STAR(NODE_LIST, START, GOAL):
	""" A* strategy """
	EXPLORED_LIST = []
	node_queue = priority_queue()
	new_start = queue_item(START, '', NODE_LIST[START].sunday_cost)
	node_queue.put(new_start)
	while not node_queue.empty():
		temp = node_queue.get()
		if temp.name in EXPLORED_LIST:
			continue
		EXPLORED_LIST.append(temp.name)
		if temp.name == GOAL:
			return (temp.routes + '#' + temp.name, temp.cost)
		print 'neighbors: '+ str(NODE_LIST[temp.name].neighbors)
		for i in NODE_LIST[temp.name].neighbors:
			print 'put' + str(i)
			cost_g = temp.cost - NODE_LIST[temp.name].sunday_cost + i[1]
			cost_h =  NODE_LIST[i[0]].sunday_cost
			temp_item = queue_item(i[0], temp.routes + '#' + temp.name, cost_g + cost_h)
			node_queue.put(temp_item)	

	return ''

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

route_tuple = None

if strategy == 'BFS':
	route_tuple = BFS(NODE_LIST, START, GOAL)
	print route_tuple

if strategy == 'DFS':
	route_tuple = DFS(NODE_LIST, START, GOAL)
	print route_tuple

if strategy == 'UCS':
	route_tuple = UCS(NODE_LIST, START, GOAL)
	print route_tuple
	
if strategy == 'A*':
	route_tuple = A_STAR(NODE_LIST, START, GOAL)
	print route_tuple

