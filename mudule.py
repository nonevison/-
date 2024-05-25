#단어 수
"""count = 0

def checking_josha(word):
    word_len = len(word)
    list_word = word.split()
    josha = ['는', '이', '가']
    for i in range(0, word_len - 1): #만약 글자 수가 4라면 0부터 3까지여야 글자 수와 동일해짐
        if word[-1] == josha[i]:
            return True 
        else:
            return False


for i in test.split(' '):
    if checking_josha(i) == True:
        count =+ 1

number_of_word = len(test.split()) + count
"""

test = "안녕하세요. 저는 노재상입니다." #17자, 공백 2자, 


#문장부호 판독
def judge_sign(word):
    sign_list = [',', '.','?','!',',','、', '·',':',
                 '/','\'','"','(',')','{','}','[',']',
                 '『', '』','「','」','《','》','〈','〉','―',
                 '–','~','˙','_','○','×','□','……']
    
    for i in range(0,34):#문장 부호 34개
        if(word == sign_list[i]):
            return True
        


#문장 부호 개수 세기
def count_sign(text):
    count = 0
    for i in text.split():
        if judge_sign(i[-1]):
            count += 1 

    return count



#띄어쓰기 개수 세기
def number_of_space(text):
    length = len(text)
    count = 0
    for i in range(0, length):
        if(text[i] == ' '):
            #print(text[i-1])
            count += 1
    return count



#공백 포함
def number_of_text(text):
    number_of_text = len(text) - count_sign(text)
    return number_of_text




#공백 제외 -> 글 - 문장 부호 - 띄어쓰기
def number_of_noempty(text):
    number_of_text_noempty = number_of_text(text) - number_of_space(text)

    return number_of_text_noempty




#문장 수
def number_of_sentence(text):
    count1 = 0
    for i in text.split():
        if judge_sign(i[-1]) == True:
            count1 += 1
    
    return count1




#출력

#print("""
#        공백 포함 : {0}
#       공백 제외 : {1}
#      문장 수 : {2}
#    """.format(number_of_text(test), number_of_noempty(test), number_of_sentence(test)))
