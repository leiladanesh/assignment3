import random
words=['glass','scissor','tissue','paper','book','clock']
word= random.choice(words)
char_list = []
for i in range(len(word)):
    char_list.append('-')


june = 6
while june>0:
    print(' '.join(char_list)) 
    if(' '.join(char_list)) == word:
        print('you are won!')  
        break
    
    input_char=input('enter character for game:=').lower()

    if input_char in word:
        for i in range(len(word)):
            if word[i]== input_char:
                char_list[i]=input_char
        

    else:
        june=june-1
        print('try agane!!\n your june is:',june) 

    if word == input_char:
        print('\n you win!')
        break
    elif june<1:
        print('\n game over!') 
        break              