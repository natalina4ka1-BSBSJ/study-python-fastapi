bot_name="Botty1"
user_name="person1"
#data entry (person asks; we answer)
print(f"my name catbott {bot_name} what is your name?")

user_name=input("write your name:")
#logic(cat_strategy;if we're lazy, we sleep; if not we work)
print(f" Nice to meet you,{user_name}.What schall we do")
 
action=input("wrete 'play' or 'sleep':").lower()
if action == 'play':
     print("ok, Let's go")
#The game itself can be added here in the future

elif action == 'sleep':
     print("sweet dreams")

else:
     print("I didn't understand you, but I'II just lie next to you like a cat.")