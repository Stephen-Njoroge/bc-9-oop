class NotesApplication(object):
	'''
	a class classed NotesApplication. Remember to inherit from the object class.
	'''
	def __init__(self, author):
		self.author = author
		self.notes = []
	def create(self, note_content):
		self.notes.append(note_content)
		return self.notes
	def list(self):
		'''
		This function lists out each of the notes in the notes list in the following format. 
		The note_id parameter below represents the respective index of each of the items in the list, 
		the NOTE_CONTENT represent the note content and the author represents the note author.
		'''
		for item in self.notes:
			print "Note Id: " + str(self.notes.index(item)) + ": " + item +  " By "  + self.author

	def get(self, note_id):
		'''
		This function takes a note_id which refers to the index of the note in the notes 
		list and returns the content of that note as a string.

		'''
		string = self.notes[note_id]
	def search(self, search_text):
		'''
		This function take a search string, search_text and 
		returns all the notes with that text within it in the following format.

		'''
		while notes:
			if search_text in self.notes:
				return "Showing results for search" + search_text + notes.index(search_text) + "by" + search_text.author
	def delete(self, note_id):
		'''
		This function deletes the note at the index note_id of the notes list.

		'''
		del self.notes[note_id]
	def replace(self, note_id, new_content):
		self.notes[note_id] = new_content

juma = NotesApplication("Dr Juma")
print juma.create("Kifo Kisimani")
juma.list()
juma.replace(0,"Mtu wa Watu")
juma.list()



