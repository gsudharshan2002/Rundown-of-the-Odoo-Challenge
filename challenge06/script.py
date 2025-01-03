
idx = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
tmp = [0, 6, 38, 2, 36, 14, 8, 3, 2, 15, 1, 5, 7, 36, 41, 14, 9, 12, 3, 14]
pwd = []
for i in tmp:
    pwd.append(idx[i])
print(''.join(pwd))
