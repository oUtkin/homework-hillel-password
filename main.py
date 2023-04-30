# Довжина пароля більша або дорівнює 8 символам.
# У паролі є хоча б одна цифра
# У паролі є хоча б одна велика
# У паролі є хоча б одна маленька буква
# У паролі є хоча б один спеціальний символ (+, -, /, _, % і т.д. P.S. їх насправді більше)

# asking user to enter the password
password = input('Enter your password: ')
pass_score = 0
recommendation = ''
len_hint = ''
digit_hint = ''
cap_let_hint = ''
low_let_hint = ''
spec_char_hint = ''

if len(password) <= 8:
    len_hint = 'Use unless 8 symbols\n'
else:
    pass_score += 1

has_digit = False
for i in password:
    if i.isdigit():
        has_digit = True
if not has_digit:
    digit_hint = 'Use digits\n'
else:
    pass_score += 1

has_cap_let = False
for j in password:
    if j.isupper():
        has_cap_let = True
if not has_cap_let:
    cap_let_hint = 'Use capital letters\n'
else:
    pass_score += 1

has_low_let = False
for k in password:
    if k.islower():
        has_low_let = True
if not has_low_let:
    low_let_hint = 'Use lowercase letters\n'
else:
    pass_score += 1

has_spec_char = False
for x in password:
    if not x.isalnum():
        has_spec_char = True
if not has_spec_char:
    spec_char_hint = 'Use special characters\n'
else:
    pass_score += 1

recommendation = f'Recommendation:\n{len_hint}{digit_hint}{cap_let_hint}{low_let_hint}{spec_char_hint}'

print(f'Password score: {pass_score}')
if pass_score < 5:
    print(recommendation)
else:
    print('Such a good password')
