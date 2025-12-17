print('''
                  __..-----')
        ,.--._ .-'_..--...-'
       '-"'. _/_ /  ..--''""'-.
       _.--""...:._:(_ ..:"::. 
    .-' ..::--""_(##)#)"':. \ \)    \ _|_ /
   /_:-:'/  :__(##)##)    ): )   '-./'   '\.-'
   "  / |  :' :/""\///)  /:.'    --(       )--
     / :( :( :(   (#//)  "       .-'\.___./'-.
    / :/|\ :\_:\   \#//\            /  |  
    |:/ | ""--':\   (#//)              '
    \/  \ :|  \ :\  (#//)
         \:\   '.':. \#//
          ':|    "--'(#///)
                     (#///)
                     (#///)         ___/""\     
                      \#///\           oo##
                      (##///)         `-6 #
                      (##///)          ,'`.
                      (##///)         // `.
                      (##///)        ||o   
                       \##///\        \-+--//
                       (###///)       :_|_(/
                       (sjw////)__...--:: :...__
                       (#/::""        :: :     ""--.._
                  __..-""           __;: :            "-._
          __..--""                  `---/ ;                '._
 ___..--""                             `-'                    "-..___
   (_ ""---....___                                     __...--"" _)
     """--...  ___"""""-----......._______......----"""     --"""
                   """"       ---.....   ___....----
''')
print("""
🏝️  Welcome to Treasure Island!
Legends say a priceless treasure lies hidden deep within this island.
Your mission is simple… survive long enough to find it.
""")

direction = input("You stand at a crossroads. Do you go Left or Right? ").strip().lower()

if direction == "left":
    print("\nYou walk cautiously and arrive at a silent river glistening under moonlight.")
    action = input("Do you Swim across or Wait for something to happen? ").strip().lower()

    if action == "wait":
        print("\nA mysterious boat appears and takes you safely across.")
        print("On the other side stands an ancient temple with three glowing doors.")
        door = input("Which door do you choose? Red, Blue, or Yellow? ").strip().lower()

        if door == "yellow":
            print("\n✨ The door opens to a room filled with gold and jewels.")
            print("🎉 Congratulations! You found the treasure and WON the game!")
        elif door == "red":
            print("\n🔥 Flames burst from the room!")
            print("Game Over.")
        elif door == "blue":
            print("\n🐍 A nest of beasts awakens and attacks!")
            print("Game Over.")
        else:
            print("\n❓ Confused, you hesitate too long.")
            print("Wrong choice. Game Over.")

    elif action == "swim":
        print("\n🌊 You jump into the river… but something drags you under.")
        print("Game Over.")

    else:
        print("\n❌ You freeze in fear and make no decision.")
        print("Wrong choice. Game Over.")

elif direction == "right":
    print("\n🕳️ You fall into a hidden trap covered by leaves.")
    print("Game Over.")

else:
    print("\n❌ Unable to decide, you wander until night falls.")
    print("Wrong choice. Game Over.")
