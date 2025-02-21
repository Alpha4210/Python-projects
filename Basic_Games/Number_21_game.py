from random import randint

playing = True

max_num = 21
while playing:
    ask = input("You want to play first or second: ")
    if ask=='first':
        while True:
            no_of_nos = int(input("Enter how many numbers you want to enter: "))
            if no_of_nos>3:
                print("You can't enter more than 3 numbers at once")    
        for i in range(no_of_nos):
            print(f"Enter {no_of_nos} numbers:")
            user_num = input("")
            list_user_num = user_num.split()
            c_no_of_nos = randint(1,3)
            list_c_nos = []
            if int(list_user_num[-1]) == 21:
                if int(list_user_num[-1])==21:
                    print("Computer won")
                else:
                    print("Player won")
                break
            else:
                for i in range(int(list_user_num[-1]),int(list_user_num[-1])+c_no_of_nos):
                    list_c_nos.append(i)
                for i in list_c_nos:
                    print(i+1,end='\n')
                
                    
                