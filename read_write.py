fw = open('sample.txt', 'w')
#open a file / prepare a file to be opened
# w = write text
# r = read
fw.write("hello there, this is my first file I wrote with python\n And it was great\n")
fw. wirte("i think bacon is great too!\n")
fw.close

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close


with open('sample.txt', 'r', encoding='utf8') as fr:
	for line in fr:
		print(line)

with open('sample.txt', 'w', encoding='utf8') as fw:
	line = 'Write sample!'
	fw.write(line)