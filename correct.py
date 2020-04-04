import os
import sys


def STD_ANS():
    std_answer = ["A", "B", "C", "D", "A", "B", "A", "B", "C", "D", "A", "B", "A"]  # what can only modified
    return std_answer


path = os.path.abspath(os.path.dirname(sys.argv[0]))

std_answers = STD_ANS()
objective_score = 0

answers = input("Please enter the answers: ")
# you should enter answers like "A B C D A B C D A B C D A" (NO ")
this_answers = answers.split()
if len(this_answers) < 13:
    print("less than 13")
elif len(this_answers) > 13:
    print("more than 13")

index = 0
for answer in std_answers:
    if answer == this_answers[index]:
        objective_score += 1
    index += 1

print(this_answers, objective_score * 3)

message = str(answers) + " " + str(objective_score * 3) + "\n"

# what you can modified is only address in '' (DON'T MODIFIED 'r')
with open(path+r'\objective_score.txt', 'a') as f:
    f.write(message)
