import prompt


def games(player_name, q_list, r_list):
    for i in range(3):
        print(f'Question: {q_list[i]}')
        user_answer = prompt.string('Your answer: ')
        result = str(r_list[i])
        if user_answer == result:
            print('Correct!')
        else:
            print(f"'{user_answer}' "
                  f"is wrong answer ;(. Correct answer was '{result}'.")
            print(f"Let's try again, {player_name}!")
            break
    else:
        print(f'Congratulations, {player_name}!')
