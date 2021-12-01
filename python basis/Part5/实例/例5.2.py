paper = open('first', 'w+')
print(paper.read())

paper.write('Welcome to Python File World!\r\n')
paper.write('Python is very powerful!\r\n')

paper.write('Python is also interesting!\r\n')
print(paper.read())
paper.seek(0)
print(paper.read())
paper.close()
