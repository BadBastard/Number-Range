#operation number range

InputUs = float(input('Input number that are not between 3-10(smaller or bigger): '))
#checking smaller number than 3

x = InputUs < 3

#checking bigger number than 10

y = InputUs > 10

#Result

correct = x or y
print('your number is',InputUs,'and the resut are: ',correct)

#----13++++20----

InputUs = float(input('Input number that are between 13-20: '))

#checking smaller number than 3

x = InputUs >13

#checking bigger number than 10

y = InputUs < 20

#Result

correct = x and y
print('Your number is',InputUs,'and This is: ',correct)

#----19++++++++

InputUs = float(input('Input number 19+: '))

#checking

x = InputUs > 19

#checking

y = InputUs < 19

#Result

correct = x and y
print('Your number is',InputUs,'and This is: ',correct)