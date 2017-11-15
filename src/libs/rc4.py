#/usr/bin/python
#coding=utf-8

class RC4:

	def __init__(self,public_key = None):
		self.public_key = public_key or 'none_public_key'

	def encode(self,strings):
		self.docrypt(strings)
		return self.result

	def decode(self,strings):
		self.docrypt(strings)
		return self.result

	def initKey(self, aKey):
		b_key = bytearray(aKey)
		state = list(xrange(256))
		index1 = index2 = 0
		if b_key == None or len(b_key) == 0:
			return None
		i = 0
		while i < 256:
			index2 = ((b_key[index1] & 0xff) + (state[i] & 0xff) + index2) & 0xff
			tmp = state[i]
			state[i] = state[index2]
			state[index2] = tmp
			index1 = (index1 + 1) % len(b_key)
			i += 1
		return state

	def docrypt(self,strings):
		x = y = i = 0
		self.result = ''
		self.keybox = self.initKey(self.public_key)
		key = self.keybox
		strlenth = len(strings)
		while i < strlenth:
			x = (x + 1) & 0xff
			y = ((key[x] & 0xff) + y) & 0xff
			key[x],key[y] = key[y],key[x]
			xorIndex = ((key[x] & 0xff) + (key[y] & 0xff)) & 0xff
			item = ord(strings[i]) ^ key[xorIndex]
			self.result += chr(item)
			i += 1