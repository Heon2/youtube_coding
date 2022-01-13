input = input()  # 0~9 =>아스키 코드 값 :48~57
alphabet = []
number = []

for i in input:
    if(47 < ord(i) < 58):  # 문자열이 숫자일 경우
        number.append(int(i))
    else:  # 문자열일 알파벳일 경우
        alphabet.append(i)
sum = sum(number)
if(sum != 0):
    alphabet.append(str(sum))
result = ('').join(alphabet)
print(result)
