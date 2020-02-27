msg = "hello world"


print("hello world")

#list

pets = ["dog","cat","fish"]

thepet = pets[1]

print(thepet)

#length & types

size= len(pets)

msg= "there are " + str(size) + " pets"

print(msg)

#loops

for animal in pets:
    print("I wish I had a "+ animal)
    
#user input
ans= input("What kind of pet do you have?")

print("you have a " + ans)

#booleans

known = ans in pets

print("it is " + str(known) + " that i have seen a " + ans)

#branching

if known:
    msg= "my friend has a " + ans 
else:
    msg="I don't know anyone with a " + ans
print(msg)
  
#dictionary

feels= {"cat":"selfish", "dog":"loyal", "fish":"wet"} 

if known:
    pre= "e" if ans == "fish" else ""
    msg= ans + pre + "s are very " + feels.get(ans)
    
else:
    msg="I don't know anyone with a " + ans
print(msg)   
