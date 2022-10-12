correct_answer = 14
answer_count = 0
answer_limit = 3


while answer_count < answer_limit:
    answer = int(input("Answer: "))
    answer_count += 1
    if answer == 14:
        print("Congratulations, you won!")
        break
else:
    print("Sorry, you failed! Try again next time")