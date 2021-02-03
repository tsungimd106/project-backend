#coding:utf-8
def cut_sentences(content):
	# 结束符號，包含中文和英文的
	end_flag = ['?', '!', '.', '？', '！', '。', '…'," "]
	
	content_len = len(content)
	sentences = []
	tmp_char = ''
	for idx, char in enumerate(content):
		# 拼接字符
		tmp_char += char

		# 判斷是否已經到了最後一位
		if (idx + 1) == content_len:
			sentences.append(tmp_char)
			break
			
		# 判斷此字符是否為結束符號
		if char in end_flag:
			# 再判斷下一個字符是否為結束符號，如果不是結束符號，則切分句子
			next_idx = idx + 1
			if not content[next_idx] in end_flag:
				sentences.append(tmp_char)
				tmp_char = ''
				
	return sentences

content = '大園、觀音、新屋、楊梅是桃園「最有發展潛力區」，我們有國際空港、最大工業區、北台最大農業區及亞洲最大火車機廠等。未來，請讓專業、有經驗、會做事的吳志揚來服務，加速在地經濟發展，讓鄉親過好日子！一、反對農田水利會長官派，加強監督管理即可。二、爭取依生產成本波動調升公糧稻穀保證收購價格，並堅守海關進囗稅則保障本土農漁產品。三、監督政府落實桃園航空城計畫，爭取合理補償及徵收條件，加速開發。四、爭取地方創生經費，設置客家文化發展基金，再造「海客文化」。五、爭取大潭電廠增加回饋項目並落實在居民身上，給予自用住宅用電補助。六、爭取竹圍、永安漁港安全與建設升級。七、爭取埔心、楊梅、富岡、新富鐵路捷運化，並增加火車停靠班次；另爭取楊梅富岡機廠落實成立鐵道文化園區，研擬設立國家鐵道博物館。八、爭取台4、15、31、61、66快速道路路平專案，並加強高架橋下空間活化運用。九、爭取中央協助輔導設立「休閒農業園區」，並推動農業精緻、休閒、有機、智慧化。十、爭取增加沿海醫療資源:大型醫院、勞工健檢中心、職災門診等。十一、捍衛環境保護，監督政府管制並減少各種環境汙染。'
sentences = cut_sentences(content)
print('\n\n'.join(sentences))
