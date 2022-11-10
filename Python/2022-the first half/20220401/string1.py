# str1 = "hobby"
# b = str1.count("b")
# print(b)
# a = str1.count('a')
# print(a)

# str2 ="Python is best choice"
# print(str2.find("is"))

# """
# 2-1) find(sub, start, end) # start index 이상 end index 미만에서 sub가 있는 첫 인덱스 찾기

# 찾는 문자가 없는 경우에 -1을 출력한다.

# 문자열을 찾을 수 있는 변수는 문자열만 사용이 가능하다.  리스트, 튜플, 딕셔너리 자료형에서는 find 함수를 사용할 수 없다. 만일 사용하게 되면 AttributeError 에러가 발생한다.

 

# 2-2) index(sub, index) index 위치 이후 부터 처음 sub가 나오는 index 값

# 찾는 문자가 없는 경우에 ValueError 에러가 발생한다.

# 문자열, 리스트, 튜플 자료형에서 사용 가능하고 딕셔너리 자료형에는 사용할 수 없어 AttributeError 에러가 발생한다.

#찾는 문자가 2개이상 있을 경우
#result = list(filter(lamba i: str1[i] == "b", range(Len(str1))))
"""
filter함수 : 문자열에서 원하는 문자들을 걸러주기 위해서 사용한다.
lamba함수 : 
"""
#print("find character result = ", result)
# """

# sep = ","
# sep2 = "|"
# print(sep.join('1234'))
# print(sep2.join('123555'))

# str3 = '                hi          1234  '#hi와 1234사이의 공백은 문자열에 포함된다.
# print(str3.lstrip())
# print(str3.rstrip())
# print(str3.strip())
# str4 = '__  __     hi________________'
# print("{}1234".format(str4.strip("_")))


str5 = "Life is too short"
print(str5.replace("Life","Your leg"))
print(str5)#따라서 변수로 변경된 것을 받고 나서 출력해야한다.
str5_1 = str5.replace("Life","Your leg")
print(str5_1)
print(str5.split())
str6 ="a:b:c:d"
print(str6.split(":"))

str7 = "a,b,c,d"
print(str7.split(","))
print(type(str7.split(",")))