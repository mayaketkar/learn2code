from sys import argv 

script, user_name = argv
prompt = '> '

print(f"{user_name}, I'm the {script} script.")
print(f"I'd like to ask you some questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"Wath types of coputer do you have? ")
coputer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.     
You live in {lives}. Not sure that is.      
And you have a {coputer} coputer. Nice.    
""" )