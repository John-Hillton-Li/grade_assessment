import correcet
import os
import sys
path = os.path.abspath(os.path.dirname(sys.argv[0]))

std_answers = correcet.STD_ANS()

messages = []
with open(path+r'\objective_score.txt', 'r') as f:
    for line in f:
        messages.append(line[:-1])

for message in messages:
    pass

