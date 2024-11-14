sentence = input()
words = sentence.split()
dict = {w: len(w) for w in words}
print(dict)
