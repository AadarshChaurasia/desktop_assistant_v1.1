try:
	import pywhatkit as kit
except:
	pass


# done
def show_info_about(query,lines=5):
	if 'show info about' in query:
		query = query[16:]
	if 'tell me about' in query:
		query = query[14:]
	if 'tell me in detail about' in query:
		query = query[24:]
		lines = 10
	if 'ke bare mai batao' in query:
		query = query[:-18]
	info = kit.info(query,lines)
	return info

# done
def search_on_google(data):
	words = data.split(' ')
	extra_words = ['search', 'in', 'on', 'for', 'about', 'related', 'to', 'krna', 'kro',
	'google', 'ke', 'bare', 'mai', 'main', 'per', 'pr']
	if 'in google' in data or 'on google' in data or 'google pr'in data or 'google mai' in data:
		for item in extra_words:
			try:
				# print(item)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
				words.remove(item)
			except:
				continue
	kit.search(words)
	return f'searching on google about {words}'


