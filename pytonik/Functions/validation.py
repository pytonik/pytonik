import re, os

class validation:

	def __getattr__(self, item):
		return item


	def __init__(self):
		return None
	
	def length(self, varstring, min, max=''):

		len_count = len(varstring)
		if min != "" and max != "":
			if len_count >= int(min) and  len_count <= int(max):
				return True
			else:
				return False
		if min != "":
			if len_count >= int(min):
				return True
			else:
				return False

	def count(self, varstring):

		return len(varstring)

	def email(self, varstring):

		regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
		if re.search(regex, varstring):
			return True
		else:
			return False 
			
	def url(self, varstring):

		regex = re.compile(
			r'^(?:http|ftp)s?://'  # http:// or https://
			r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
			r'localhost|'  # localhost...
			r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
			r'(?::\d+)?'  # optional port
			r'(?:/?|[/?]\S+)$', re.IGNORECASE)

		if regex.match(varstring):
			return True
		else:
			return False
		
	def ip(self, varstring):
     
		regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''
		if re.match(regex, varstring):
			return True
		else:
			return False
		
  
	def single(self, varstring):
     
		regex = re.compile(r'^[a-zA-Z]+[a-zA-Z]+$', re.IGNORECASE)
		if regex.search(varstring):
			return True
		else:
			return False

	def phone(self, varstring):
     
		regex = re.compile(r'([+]?\d{1,4}[.\-\s]?)?(\d{3}[.-]?){2}\d{4}$')
		if regex.match(varstring):

			return True
		else:
			return False
 
	def number(self, varstring):
     
		regex = re.compile(r'(\d+)')
		if regex.match(varstring):
			return True
		else:
			return False

	def fullname(self, varstring):
     
		regex = re.compile(r'(^[a-zA-Z\- ]+)$', re.IGNORECASE)
		if regex.search(varstring):
			return True
		else:
			return False


	def trim(self, varstring):

		regex = re.sub('<[^<]+?>', '', varstring)

		return regex

	def extension(self, varstring, exe_list):
		string_text = os.path.splitext(varstring)[1][1:]
		if string_text in exe_list: 
			return True
		else:
			return False
