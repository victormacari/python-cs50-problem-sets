from string import digits, ascii_letters, punctuation

for i in digits + ascii_letters + punctuation:
    for j in digits + ascii_letters + punctuation:
        for k in digits + ascii_letters + punctuation:
            for l in digits + ascii_letters + punctuation:
                print(i, j, k, l)