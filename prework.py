def hello_name(user_name):
    print ("Hello" + user_name.title() + "!")
#hello_name('Steve')

def greeting(user_name):
    print('Hello {}'.format(user_name.title()))
    print(f'Hello again {user_name.title()}')

#greeting('Steve')

def odd_numbers():
    for i in range(0,100):
        if i % 2 != 0:
            print (i)

#odd_numbers()

def odd_numbers2():
    for i in range(1,101,2):
        print(i)

#odd_numbers2()

#question 3
def max_num_in_list(a_list):
    return max(a_list)

the_list = [10000, 5, 78, 309, 121]
#print(max_num_in_list(the_list))

#question4
#def is_leap_year(a_year):
#    if a_year % 4 == 0:
#        return True
#    elif a_year % 100 == 0:
#        return False
#    elif a_year % 400 == 0:
#        return True
#    else
#        return False

#question5
a_list = [1,2,3,4,5]

def is_consecutive(a_list):
    i = 0
    status = True
    while i < len(a_list) - 1:
       if a_list[i] + 1 == a_list[i + 1]:
           i += 1
       else:
            status = False
            break
    print(status)

print(is_consecutive(a_list))
