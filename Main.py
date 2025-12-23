import string #to use punctuation list 
text=input("Enter your sentence or paragraph:")
clean_text="" #remove punctuation 
for char in text:
    if char not in string.punctuation:#(if character is not a punctuation mark)skip punctuation marks and use others like letters,spaces etc.
        clean_text+=char#add new characters to clean_text.e.g:yasir,khan=>yasirkhan
words=clean_text.split()#split into words Yasirkhan=>yasir khan
total_words=len(words)
#counting total characters excluding spaces
total_characters=0
for w in words:
    total_characters+=len(w)
#counting unique words
unique_words=[]
for w in words:
    w_lower=w.lower() #make lowercase for accurate counting 
    if w_lower not in unique_words:#check if the word is not already in the unique list.
        unique_words.append(w_lower)#add new unique word to the list
unique_words_count=len(unique_words)
print("Results:")
print("total words:",total_words)
print("Total characters(excluding spaces):",total_characters)
print("Unique Words:",unique_words_count)
print("Cleaned Text:",clean_text)