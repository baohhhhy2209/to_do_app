
listItems = list()
class ListItem:

	isComplete = False 
	title = ''
	def __init__(self, title): 
		listItem.append(self)
		self.title = title 

	def set_as_complete(self): 
		self.isComplete = True 

	def get_listITem(self): 
		return self
	def update(self, index, title):
		listItem[index].title = title 
	def delete(self, index): 
		del listItem[index]
listItem = ListItem("wash the dishes")
listItem.set_as_complete()
print(listItem.get_listITem())
