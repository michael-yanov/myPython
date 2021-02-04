number = int(input('Enter a number: '))
reversed_number = 0
tmp_original = number

while tmp_original > 0:
    print(reversed_number * 10, ' reversed_number * 10')
    print(tmp_original % 10, ' tmp_original % 10')
    reversed_number = (reversed_number * 10) + tmp_original % 10
    tmp_original = tmp_original // 10
if number == reversed_number:
    print('palindrome')
else:
    print('no palindrome')