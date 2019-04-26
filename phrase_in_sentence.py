"""
Given a list of sentences and a list of phrases. The task is to find which sentence(s) contain all the words in a phrase and for every phrase print the sentences number that contains the given phrase.

Constraint: A word cannot be a part of more than 10 sentences.

Examples:



Input: 
Sentences:
1. Strings are an array of characters.
2. Sentences are an array of words.
Phrases:
1. an array of
2. sentences are strings
Output:
Phrase1 is present in sentences: 1,2
Phrase2 is present in sentences: None
"""



class PhraseIdentifier():
	def __init__(self, sentence_list, phrase_list):
		self.sl = sentence_list
		self.pl = phrase_list

	def phrase_in_sentence(self):
		phrase_count = 0
		for p in self.pl:
			phrase_count += 1
			phrase_words = p.split()
			sentence_count = 1
			for s in self.sl:
				cond = False
				for word in phrase_words:
					if word in s:
						cond = True
					else:
						cond = False
						break;
				if cond:
					print "Phrase %s is present in sentence: %s" %(phrase_count, sentence_count)
					sentence_count += 1


if __name__ == '__main__':
	sentence_list = ["Strings are an array of characters.", "sentences are an array of words."]
	phrase_list = ["an array of", "sentences are strings"]
	obj = PhraseIdentifier(sentence_list, phrase_list)
	obj.phrase_in_sentence()
