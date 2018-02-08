import jieba

jieba.load_userdict('user_dict.txt')  # 添加自定义词典
stopwords = []  # 设置停用词集合
for word in open('stop_words.txt', 'r'):
	stopwords.append(word.strip())

def fenci(article):
	words = jieba.cut(article, cut_all = False)  # 分词

	word_freq = {}  # 记录每个词出现的频率
	for word in words:
		if word.encode('utf-8') not in stopwords:  # 去除停用词
			if word in word_freq:
				word_freq[word] += 1
			else:
				word_freq[word] = 1
			
	freq_word = []  # 按照词频排序从大到小进行排序
	for word, freq in word_freq.items():
		freq_word.append((word, freq))
	freq_word.sort(key = lambda x: x[1], reverse = True)

	return freq_word

def print_fenci(freq_word, max_number):
	# 按照词频打印出所有关键词
	for word, freq in freq_word:
		try:
			a = float(word) # 过滤掉数字
		except:
			# 只有当关键词长度不为1时，才记为有效词
			if len(word) != 1:
				print word, freq,
				max_number -= 1
			if max_number <= 0:
				break