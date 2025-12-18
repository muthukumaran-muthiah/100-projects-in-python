import random

rock = r'''                                             
                                  88         
                                  88         
                                  88         
8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8   
88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"    
88         8b       d8 8b         8888[      
88         "8a,   ,a8" "8a,   ,aa 88`"Yba,   
88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a  
                                             
                                             '''
paper = r'''8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba,  
88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8  
88       d8 ,adPPPPP88 88       d8 8PP""""""" 88          
88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88          
88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88          
88                     88                                 
88                     88                                 '''

scissor = r'''                                                                              
                     88                                                       
                     ""                                                       
                                                                              
,adPPYba,  ,adPPYba, 88 ,adPPYba, ,adPPYba,  ,adPPYba,  8b,dPPYba, ,adPPYba,  
I8[    "" a8"     "" 88 I8[    "" I8[    "" a8"     "8a 88P'   "Y8 I8[    ""  
 `"Y8ba,  8b         88  `"Y8ba,   `"Y8ba,  8b       d8 88          `"Y8ba,   
aa    ]8I "8a,   ,aa 88 aa    ]8I aa    ]8I "8a,   ,a8" 88         aa    ]8I  
`"YbbdP"'  `"Ybbd8"' 88 `"YbbdP"' `"YbbdP"'  `"YbbdP"'  88         `"YbbdP"'  
                                                                              
                                                                              '''
rsp = [1,2,3]
rsp_symbols = [rock, scissor, paper]
print("Choices; 1 - Rock; 2 - Scissor; 3 - Paper")
user_choice = int(input("Enter your choice: "))
if 1 > user_choice > 3:
    print("Invalid choice!")
else:
    system_chose = random.choice(rsp)
    print("Your choice is: ", rsp_symbols[user_choice-1])
    print("System choice is: ", rsp_symbols[system_chose-1])

    if system_chose == 1 and user_choice == 2:
        print("You lose!")
    elif system_chose == 2 and user_choice == 3:
        print("You lose!")
    elif system_chose == 3 and user_choice == 1:
        print("You lose!")
    elif system_chose == user_choice:
        print("Draw!!!!!")
    else:
        print("You won!!!")