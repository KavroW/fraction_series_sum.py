x = 1
acc = 0
for x in range(1,98,2):
    acc += (x/(x+2))
print(f'{acc:.3f}')