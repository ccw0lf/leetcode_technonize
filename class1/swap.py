a =[1,2,3,4,5]

start =0
end= len(a)-1

while start<=end:

    temp = a[start]
    a[start]= a[end]
    a[end]=temp

    start+=1
    end-=1



    print(a)



            








