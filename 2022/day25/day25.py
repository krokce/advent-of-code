with open('day25.txt', 'r') as file:
    lines = [l.strip("\n") for l in file.readlines()]

S2D = {"0":0, "1":1, "2":2, "-":-1, "=":-2}
D2S = {0:"0", 1:"1", 2:"2", -1:"-", -2:"="}

def snafu2dec(n):
    return sum([S2D[n[len(n)-i-1]] * 5**i for i in range(len(n))])

def dec2snafu(n):
    snafu_value = 0
    snafu_digits = []
    
    digit = 0
    while abs(snafu_value - n) > 5:
        tuning_direction = -1 if snafu_value > n else 1

        for multiplier in range(3):
            if digit > len(snafu_digits)-1:
                snafu_digits.append(0)
            
            snafu_digits[digit] = tuning_direction * multiplier
            snafu_value = sum([5**x * y for x,y in enumerate(snafu_digits)])

            if snafu_value > n and tuning_direction > 0:
                tuning_direction = -1
                digit = 0
                break

            if snafu_value < n and tuning_direction < 0:
                tuning_direction = 1 
                digit = 0
                break

        digit += 1

    while snafu_value != n:
        delta = int((n-snafu_value)/abs(snafu_value - n))
        digit = 0
        while True:
            snafu_digits[digit] += delta
            if snafu_digits[digit] < -2:
                snafu_digits[digit] = 2
                digit += 1
            elif snafu_digits[digit] > 2:
                snafu_digits[digit] = -2
                digit += 1
            else:
                snafu_value = sum([5**x * y for x,y in enumerate(snafu_digits)])
                break

    return "".join(reversed([D2S[snafu_digit] for snafu_digit in snafu_digits]))

#1
s = sum([snafu2dec(snafu) for snafu in lines])
print(dec2snafu(s))