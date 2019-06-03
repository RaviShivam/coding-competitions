w, b = map(float, input().split(' '))
print(type(w), type(b))
if w + 0.5 > b or w%5!=0:
    print('{:.2f}'.format(b))
else:
    print('{:.2f}'.format(b-w-0.5))