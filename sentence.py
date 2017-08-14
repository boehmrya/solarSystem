


class Sentence:
	def __init__(self, iWords):
		self.words = iWords

	# accessor methods
	def getSentence(self):
		return self.words

	def getWords(self):
		return (self.words).split()

	def getLength(self):
		return len(self.words)

	def getNumWords(self):
		return len(self.getWords())

	# mutator methods
	def makeUpperCase(self):
		self.words = self.words.upper()

	def addPuncMark(self, puncMark):
		self.words = (self.words + puncMark)



class newSentence:
	def __init__(self, iWords):
		self.words = iWords.split()

	def getSentence(self):
		return ' '.join(self.words)

	def getWords(self):
		return self.words

	def getLength(self):
		return len(self.getSentence())

	def getNumWords(self):
		return len(self.words)

