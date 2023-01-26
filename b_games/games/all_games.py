import prompt
from b_games.cli import welcome_user


def games(rules_str, qlist_func, alist_func):
    print('Welcome to the Brain Games!')
    player_name = welcome_user()
    print(rules_str)
    q_list = qlist_func()
    r_list = alist_func(q_list)
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
