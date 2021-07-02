#assignment 1
givenval = [3,4,5,6,1,2,45,32,56,56,89,90,12,54,45,9,67,68,31,32]
 #selection sort
for x in range(len(givenval)):
    for y in range(x,len(givenval)-1):
        if x>y:
            temp=givenval[x]
            givenval[x]=givenval[y]
            givenval[y]=temp
#values sorted

#calculating mean
mean_val = 0.0
for x in range(len(givenval)):
    mean_val += givenval[x]

mean_val = mean_val/len(givenval)

print("mean is", mean_val)
medianval =0.0
if len(givenval)%2==0:
    medianval = (givenval[len(givenval)/2]+givenval[len(givenval)/2 - 1])/2
else:
    medianval=givenval[len(givenval)/2]

print("median is", medianval)


# calculating mode
mode=givenval[0]
count = 1
count_prev = 1
for x in range(len(givenval)):
    for y in range(len(givenval)):
        count=count+1

    if count>count_prev:
        count_prev=count 
        mode=givenval[x]

    count=1

if count_prev>1:
    print("mode is", mode)
else:
    print("print no reoccuring numbers")

      