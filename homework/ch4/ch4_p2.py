HEIGHT_AND_WIDTH = 6

for i in range(1, HEIGHT_AND_WIDTH+1):
    for j in range(HEIGHT_AND_WIDTH):
        if i + j > 6:
            fig = 'x '
        else:
            fig = 'o '
        print(fig, end=" ")
    print()