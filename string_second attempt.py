#thank you for your feedback, this code actually ran!

sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog!" #sentence saved as string. 
print(sentence)

new_sentence = sentence.replace('!', ' ') #replace the sentence above with a space instead of !
print(new_sentence) 

repeat_sentence = new_sentence + new_sentence

uppercase_sentence = repeat_sentence.upper() #prints the sentence out in uppercase.
print(uppercase_sentence)

reverse_sentence = uppercase_sentence[::-1] #prints sentence out in reverse

print(reverse_sentence)  