#dic = {key : value}
dic = {'name' : 'pey', 'phone' : 109993323, 'birthday' : 1118}
#dic은 key건 value건 숫자, 문자형 전부 가능하지만 phone의 value 같은 경우
#앞의 0이 짤리기 때문에 문자형으로 처리하는게 좋다. 
#생일도 마찬가지로 1998.01.01 같이 다른 형태로도 저장될 수 있기 때문에 문자형으로 저장하는게 좋다.
dic = {'name' : 'pey', 'phone' : '0109993323', 'birthday' : '1118'}

#print(type(dic[1]))

a = {1: 'a'}
#dic_name[key] = value

a[2] = 'b'
a['name'] = 'pey'
a[3] = [1,2,3]
print(a)

# del a[1]
# print(a)
# print(a[2])
# print(list(dic.keys()))
# print(type(dic.keys()))
# print(dic.keys())
# print(dic.values())
# print(type(dic.values()))
# for k in dic.keys():
#     print(k)

# for k in dic.values():
#     print(k)

print(dic.items())
dict = list(dic.items())
print(dict[2])
print(dic['phone'])
print(dic.get('name'))

#print(dic['phone1'])
if(dic.get('name')):
    for k in dic.keys():
        print(k)
else:
    print(dic.get('phone1','no phone'))
    
print('name' in dic)
print('email' in dic)

