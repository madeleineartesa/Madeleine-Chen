n=int(input())

all_samples=[]
for sample in range(n):
    sample_list=input().split()
    all_samples.append(sample_list)


for sample in all_samples:
    ##find speed
    speed=sample[0]
    length=sample[1]
    freq=sample[2]
    if speed=="x":
        speed=int(int(length)*int(freq))
    elif length=="x":
        length=int(int(speed)/int(freq))
    elif freq=="x":
        freq=int(int(speed)/int(length))
    print(speed, length, freq)