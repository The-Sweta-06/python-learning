words = ["Donkey", "bad", "ganda"]

with open("file.nxt", "r") as f:
    content = f.read()
 
for word in words:
    contentNew = content.replace(word, "#" * len(word))
    
with open("file.nxt", "w") as f:
    f.write(contentNew)