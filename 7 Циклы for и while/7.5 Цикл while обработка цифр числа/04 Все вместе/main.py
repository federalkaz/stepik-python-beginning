num = int(input())
sum = 0
amount_digit = 0
proizved = 1
srednee_arif = 0
sum_first_last = 0
aux2 = num

while num > 0:
    aux = num % 10
    num = num // 10
    sum += aux
    amount_digit += 1
    if aux > 0:
        proizved *= aux
    if num < 100:
        last_digit = aux

first_digit = aux2 // (10 ** (amount_digit - 1))
last_digit = aux2 % 10
srednee_arif = sum / amount_digit
sum_first_last = first_digit + last_digit

print(sum)
print(amount_digit)
print(proizved)
print(srednee_arif)
print(first_digit)
print(sum_first_last)
