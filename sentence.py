


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

	# overloaded operators
	def __getitem__(self, i):
		wordList = self.getWords()
		return wordList[i]

	def __len__(self):
		return getNumWords()

	def __contains__(self, word):
		wordList = self.getWords()
		for w in wordList:
			if w == word:
				return True
		return False

	def __add__(self, newWords):
		self.words = self.words + self.newWords




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

