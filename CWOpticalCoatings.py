n=int(input())

all_samples=[]
for sample in range(n):
    sample=input().split()
    all_samples.append(sample)

for sample in all_samples:
    wavelength=float(sample[0])
    filmN=float(sample[1])
    glassN=float(sample[2])
    #nf>ng --> first wave out-of-phase, second wave in-phase --> out-of-phase --> 2t=m*lambda/n
    if filmN>glassN:
        first_three=[]
        for m in range(1,4):
            thickness=(m*wavelength)/(2*filmN)
            first_three.append(thickness)
        print(format(first_three[0],"0.3f"), format(first_three[1],"0.3f"), format(first_three[2],"0.3f"))

    #nf<ng --> first wave out-of-phase, second wave out-of phase --> in-phase --> 2t=(m+1/2)*lambda/n
    elif filmN<glassN:
        first_three=[]
        for m in range(3):
            thickness=((m+0.5)*wavelength)/(2*filmN)
            first_three.append(thickness)
        print(format(first_three[0],"0.3f"), format(first_three[1],"0.3f"), format(first_three[2],"0.3f"))

    #nf=ng --> film doesn't work
    elif filmN==glassN:
        print("Ineffective Film")