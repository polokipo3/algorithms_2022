b = [['login', 'password', 0]]


def enter(a):
    login = input('Login: ')
    password = input('Password: ')
    for i in a:                                                         # O(n)
        if i[0] == login:                                               # O(1)
            if i[1] == password:                                        # O(1)
                if i[2] == 1:                                           # O(1)
                    return print("Welcome back!")
                else:
                    print("Would you like to complete authentification?")
                    ans = input()
                    if ans.lower() == 'yes':                            # O(1)
                        i[2] = 1
                        print('Authentification completed')
                        return enter(a)
                    else:
                        return print('Answer is incorrect, please try again')
            else:
                return print('Password is wrong')
    return print(f'There is no such login as {login}')
# Сложность: О(n)
enter(b)

# Идей для второго решения нет