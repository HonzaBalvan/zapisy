jeden_input = input()
cely_input = ""

while jeden_input != "Amen.":
    cely_input.append(jeden_input)
    jeden_input = input()

cely_input.translate(None, ',')
sentence = cely_input.split()

words = sentence.split()
average = sum(len(word) for word in words) / len(words)
print(average)
