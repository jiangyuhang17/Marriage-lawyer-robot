import jieba

jieba.load_userdict('user_dict.txt')  # 添加自定义词典
stopwords = []  # 设置停用词集合
for word in open('stop_words.txt', 'r'):
	stopwords.append(word.strip())

def fenci(article):
	words = jieba.cut(article, cut_all = False)  # 分词

	ord_word = [] # 重新定义一个list来存储分词结果
	for word in words:
		if word.encode('utf-8') not in stopwords and len(word)!=1:  # 去除停用词
			ord_word.append(word)

	return ord_word

def print_fenci(words):
	# 按照词频打印出所有关键词
	for word in words:
		# 只有当关键词长度不为1时，才记为有效词
		if len(word) != 1:
				print word,