def cheker(var_1):
    if type(var_1) != str:
        raise TypeError (f"Вибачте але ми не можеме працювати {type(var_1)},"f"Ми працюємо з типом str")
    else:
        return var_1

first_var = 'hello'
cheker(first_var)