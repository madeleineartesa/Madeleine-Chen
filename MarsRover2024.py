##list of levels of difficulties copied from examples in problem description
difficulties =  [27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

diffs={} 
for i in range(len(difficulties)-1): ##for loop going through each 
    difference=difficulties[i+1]-difficulties[i] ##calcs difference btwn two consecutive numbers
    start=difficulties[i]+1 ##indicates the day a difference started
    pair=(difference,start) ##makes tuple of the difference btwn numbers and the starting day (this is the format the problem asks for)
    diffs.update([pair]) ##inserts tuple into dictionary

if max(diffs)<=0: ##if there are no positive differences, this will print (0,1) in accordance with the problem guidelines
    print((0,1))

else: ##if there are positive differences
    pair2=(max(diffs),diffs[max(diffs)]) ##finds the maximum-value key in the dictionary and the corresponding value
    print(pair2) ##prints the tuple with the max difference