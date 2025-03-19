# word_counter.py
text = input("Enter a sentence or paragraph: ")
words = text.split() 
print(f"Words: {len(words)}, Characters: {len(text)}")
