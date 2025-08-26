
import operator

def count(article):
	words = article.split()
	word_count = len(words)
	dict_word = {}
	for word in words:
		if word in dict_word:
			dict_word[word] += 1
		else:
			dict_word[word] = 1

	sorted_dict_word = sorted(dict_word.items(), key=operator.itemgetter(1), reverse=True)
	return sorted_dict_word,word_count
