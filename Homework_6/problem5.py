# Делаем обёртку для рекурсии в виде другой функции

def func(n):
    def rec(number):
        pass
    return rec(n)

# Так мы получаем измерения только для func и без каждого прохода rec