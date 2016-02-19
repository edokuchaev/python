total = 0
question ='For...'
option = '1 starts a cycle, 2 iterates'
right = 2
print(question,' ',option)
user = input()
print('You answered...',user)
if int(user) == right:
    total = total +1
    print('Yes, right!')
else:
    print('No, wrong')
print('Score = ',total)
#
question ='Float takes more memory in'
option = '1 Python2.7, 2 Python3'
right = 2
print(question,' ',option)
user = input()
print('You answered...',user)
if int(user) == right:
    total = total +1
    print('Yes, right!')
else:
    print('No, wrong')
print('Score = ',total)
#
question ="print(u'Moscva')"
option = '1 prints in unicode, 2 prints underlined'
right = 1
print(question,' ',option)
user = input()
print('You answered...',user)
if int(user) == right:
    total = total +1
    print('Yes, right!')
else:
    print('No, wrong')
print('Score = ',total)
#
question ="print(u'Unicode \strange to wotk with')"
option = '1 will print with tab, 2 from the new line'
right = 2
print(question,' ',option)
user = input()
print('You answered...',user)
if int(user) == right:
    total = total +1
    print('Yes, right!')
else:
    print('No, wrong')
print('Score = ',total)
#
question ="print('moscow'[3:6])"
option = '1 will print mos, 2 will print cow'
right = 2
print(question,' ',option)
user = input()
print('You answered...',user)
if int(user) == right:
    total = total +1
    print('Yes, right!')
else:
    print('No, wrong')
print('Score = ',total)
#
question ="print('number',7) and print('number %d' % (7))"
option = '1 will have same result, 2 not the same result'
right = 1
print(question,' ',option)
user = input()
print('You answered...',user)
if int(user) == right:
    total = total +1
    print('Yes, right!')
else:
    print('No, wrong')
print('Score = ',total)
