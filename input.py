'''
name = input('Enter Your Name:');
age = input('Enter Your age:');
print('my name is '+name);
print("i am ",age," years old");
'''

# age=int(input('Enter Your age :'));
# print("my age is now ",age)
# name=input("Enter your Name:");
# print(name +" is my name");

# a=24;
# b=7
# print(a+b);
# print(a-b);
# print(a*b);
# print(a/b);
# print(a//b);
# print(a%b);
# if a>20:
#     print("number is big")
# elif a>10:
#     print("number is middle")
# else:
#     print('number is samll')

#ternary operator
    
# num1 = 20;
# num2 = 30;
# num3 = 50;
# # print(num1 if num1>num2 else num2);
# if num1 > num2 and num1 > num3:
#     print(num1);
# elif num2 > num1 and num2 > num3:
#     print(num2);
# else:
#     print(num3);


# ch = 'M'
# if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
#     print('vowel');
# else:
#     print('Consonent');

# mark = 56;
# if mark >=80 and mark <=100:
#     print("A+");
# elif mark >=70 and mark<80:
#     print("A");
# elif mark >=60 and mark<70:
#     print("A-");
# elif mark >=50 and mark<60:
#     print("B");
# elif mark >=40 and mark<50:
#     print("C");
# elif mark >=33 and mark<40:
#     print("D");
# else:
#     print("F");

# fruits = ['apple','ball','orange','mango'];
# for i in fruits:
#     print(i);

# a=0;
# while a<=20:
#     print(a);
#     a= a + 1;

# num = int(input('Enter the Number:'));
# sum = 0;

# j=1;
# while j<= num:
#     sum = sum + j;
#     j = j + 1;
# print(sum);

# m=1
# while m <= 20:
    
#     m = m + 1;
#     print(m)

#     if(m == 10):
#         continue
#     print("Hello")

number = [3,1,6,4,9,7];
# number.sort();
# print(number);
# number.reverse();
# print(number);
# number.append(15)
# print(number);
# print(number.index(6))
print(number.pop())
print(number.pop())

number.insert(2,8)
print(number);
number.remove(8);
print(number);