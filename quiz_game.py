print('Welcome to MY quiz!')
playing = input('Do you want to play? ')
print(playing)
if playing.lower() != 'yes':
    quit()
print("okay, Let's play :)")
score = 0
answer = input("what does a CPU stand for? ")
if answer.lower() == "central processing unit":
    print('correct answer')
    score+=1
else:
    print('incorrect answer') 
answer = input("what does a GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('correct answer')
    score+=1
else:
    print('incorrect answer')
answer = input("what does a RAM stand for? ")
if answer.lower() == "random access memory":
    print('correct answer')
    score+=1
else:
    print('incorrect answer')   
print("you got " + str(score)+ " questions correct!") 
print("you got " + str((score/4)*100)+"%")      