# #리스트 내포

# #for 문, if 문 들을 지정하여 리스트를 간편하게 만드는 것

# #[표현식 for 변수 in 순회가능한 데이터]

# nums = [i for i in range(5)]
# print(nums)

# double_nums = [i*2 for i in nums]

# print(double_nums)

# #[표현식 for 변수 in 순회가능한 데이터 if 조건식] #즉, 리스트 내포는 result.append(i)를 하는 것과 같은 뜻이다.
# numz = [i for i in range(10) if i % 2 ==0]

# double_numz = [i*2 for i in numz if i % 3 == 0]

# strings = ['cat', 'dog', 'pig']

# string_filter = [i for i in strings if i.find('g') == 2]
# print(string_filter)

# number_head = ["01711111111","01011111111","01211111111","01111111111","01711113333"]
# number_head_filter = [i for i in number_head if i[2] == "7"]
# print(number_head_filter)

word_list = ['apple', 'watch', 'apolo', 'star', 'abocado']
result = [word for word in word_list if word[2] == 'a' or word[3] == 'a']

# def check_a(x):
#     for word in x:
#         if word[2] == 'a' or word[3] == 'a':
#             return word
#         else:
#             return '' 
        
def check_a(x):
        return x[2] == 'apple' or x[3] == 'a'
        #return len(x)<=4

#print(check_a(word_list))
        
#print(filter(check_a,list(map(lambda i : word_list[i],len(word_list)))))
print(list(filter(check_a,word_list)))#filter(bool 값, 리스트)
#filter는 결국 word_list가 반복되는 부분이고 check_a는 checking 하는 것이므로 check하는 부분에서는 반복이 들어가선 안된다.


# items = ['오메가3',None,'비타민c500',None,'홍삼절편']

# result = []

# for item in items:
#     if item != None:
#         result.append(item)
#     else:
#         result.append("")
# print(result)

# result1 = [item for item in items if item != None] #if만 썼을 경우
# result2 = [item if item != None else '' for item in items] #if와 else 둘다 썼을 경우

# print(result1);print(result2)
    
