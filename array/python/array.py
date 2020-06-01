import logging


class Array(object):
	
	DEFAULT_CAPACITY = 16
	SIZING_VELOCITY = 2
	EMPTY_VALUE = None

	def __init__(self, arg):
		super(Array, self).__init__()
		self.capacity = self.DEFAULT_CAPACITY
		self.array = [self.EMPTY_VALUE for i in range self.capacity]
		self.count = 0		

	def isEmpty(self):
		return self.count == 0

	def __resize(self, newCapacity):		
		if self.capacity == newCapacity:
			return

		tempArray = [self.EMPTY_VALUE for i in range newCapacity]
		for i in range(newCapacity):
			tempArray[i] = self.array[i]

		self.capacity = newCapacity
		self.array = tempArray

	def __upSize(self):
		self.resize(self.capacity*self.SIZING_VELOCITY)

	def __downSize(self):
		self.resize(max(self.DEFAULT_CAPACITY, self.capacity/self.SIZING_VELOCITY))

	def __updateSize(self):
		if self.count <= self.capacity/(2*self.SIZING_VELOCITY):
			self.__downSize()
			return

		if self.count >= (self.capacity-1):
			self.__updateSize()
			return

	def get(self, index):
		if index < 0 or index >= self.count:
			return None
		return self.array[index]	

	def insert(self, item, index):		
		if index < 0 or index > self.count:
			return logging.error('Invalid index.')

		for i in reversed(range(index+1, self.count+1)):
			self.array[i] = self.array[i-1]
		self.array[index] = item

		self.count += 1
		self.__updateSize()

	def append(self, item):	
		self.insert(item, self.count)

	def prepend(self, item):		
		self.insert(item, 0)

	def pop(self):	
		if self.isEmpty():
			return None

		self.count -= 1
		lastItem = self.array[self.count]
		self.__updateSize()
		return lastItem

	def delete(self, index):
		if index < 0 or index >= self.count:
			return logging.error('Invalid index.')

		for i in range(index, self.count):
			self.array[i] = self.array[i+1]

		self.count -= 1
		self.__updateSize()

	def find(self, item):
		for i in range(self.count):
			if self.array[i] == item:
				return i
		return None

	def remove(self, item):
		index = self.find(item)
		if index != None:
			self.delete(index)

	def removeAll(self, item):
		tempArray = Array()

		for i in range(self.count):
			if self.array[i] != item:
				tempArray.append(item)

		self.capacity = tempArray.capacity
		self.array = tempArray.array
		self.count = tempArray.count









		