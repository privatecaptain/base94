import unittest

def base94_encode(number):
	result = ''
	while number > 0:
		result += chr(32 + number%94)
		number /= 94
	return result[::-1]



def base94_decode(string):
	base94_ints = [ord(i)-32 for i in string]
	base94_ints.reverse()
	result = 0
	for i in range(0,len(base94_ints)):
		result += base94_ints[i]*(94**i)
	return result

text = open('95.txt','r')
words =  []
base94_encode_dict = {}
base94_decode_dict = {}
lines = text.readlines()


for i  in lines:
	words += i.split()

for i in range(0,len(words)):
	base94_encode_dict[words[i]] = i+1
	base94_decode_dict[i+1] = words[i]

original_text = ' '
for i  in lines:
	original_text += i

length = len(original_text)
encoded_text = ''

original_text = original_text.split()
for i in original_text:
	encoded_text += base94_encode(base94_encode_dict[i])+' '
print encoded_text
print len(encoded_text),length,len(words)

