
# asking user to enter the password
password = input('Enter your password: ')

# will show us how strong is the password
pass_score = 0

# shows user how to make the password stronger
recommendation = ''

# list of specific hints how to make the password stronger
len_hint = ''
digit_hint = ''
cap_let_hint = ''
low_let_hint = ''
spec_char_hint = ''

# checking the length of password
if len(password) <= 8:
    len_hint = 'Use unless 8 symbols\n'
else:
    pass_score += 1

# variables to check every character in the password
has_digit = False
has_cap_let = False
has_low_let = False
has_spec_char = False

for i in password:
    # checking does password have any digit
    if i.isdigit():
        has_digit = True
    # checking does password have any capital letter
    elif i.isupper():
        has_cap_let = True
    # checking does password have any lowercase letter
    elif i.islower():
        has_low_let = True
    # checking does password have any special character
    # using not because .isalnum() returns True
    # if string doesn't contain any special character
    elif not i.isalnum():
        has_spec_char = True

if not has_digit:
    # adding hint if password doesn't contain any digit
    digit_hint = 'Use digits\n'
else:
    # adding point to the password score if it contains any digit
    pass_score += 1

if not has_cap_let:
    # adding hint if password doesn't contain any capital letter
    cap_let_hint = 'Use capital letters\n'
else:
    # adding point to the password score if it contains any capital letter
    pass_score += 1

if not has_low_let:
    # adding hint if password doesn't contain any lowercase letter
    low_let_hint = 'Use lowercase letters\n'
else:
    # adding point to the password score if it contains any lowercase letter
    pass_score += 1

if not has_spec_char:
    # adding hint if password doesn't contain any special character
    spec_char_hint = 'Use special characters\n'
else:
    # adding point to the password score if it contains any special character
    pass_score += 1

# showing user how strong is his/her/their password is in scale from 1 to 5
print(f'Password score: {pass_score}')

# collect together all hints in 1 recommendation string
recommendation = f'Recommendation:\n{len_hint}{digit_hint}' \
                 f'{cap_let_hint}{low_let_hint}{spec_char_hint}'

# showing recommendation if password not strong enough
if pass_score < 5:
    print(recommendation)
else:
    print('Such a good password')
