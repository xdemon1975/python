text = """testing
writing text
in the files
한글도 입력
"""

files = open("t.txt", 'w')
print(files)

files.write(text)
files.close()
