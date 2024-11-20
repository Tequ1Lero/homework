immutable_var = ('string_1', 'string_2', 3, 4, 5.1, 6.2, True)
print(immutable_var)
# immutable_var[0] = 'string_3.11'
# кортежи не поддерживают обращение к элементу, поэтому изменить его в текущем виде нельзя нельзя.
# при выполнении команды получим код TypeError: 'tuple' object does not support item assignment
# Изменение допустимо только в том случае, если кортеж содержит в себе измиеняемый объект, например список

mutable_var = ['string_1', 'string_2', 3, 4, 5.1, 6.2, True]
mutable_var[0] = 'string_3.11'
print(mutable_var)