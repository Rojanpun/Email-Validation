print ('Welcome to quiz!')

playing = input('do you want to play? ')

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("what does CPU stand for? ")

if answer.lower() == "central processing unit":
    print('Correct')
    score += 1
else:
    print('Incorrect')

answer = input("What does GPU stand for? ")

if answer.lower() == "graphics processing unit":
    print('Correct')
    score += 1
else:
    print('Incorrect')

answer = input("what does RAM stand for? ")

if answer.lower() == "random access memory":
    print('Correct')
    score += 1
else:
    print('Incorrect')

answer = input("what does ROM stand for? ")

if answer.lower() == "read only memory":
    print('Correct')
    score += 1
else:
    print('Incorrect')

print("You got " + str(score) + " questions correct")
print("You got " + str((score/4)*100) + "%.")