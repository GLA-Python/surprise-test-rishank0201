def function_expanding(lst):
    diff=0
    c=0
    for i in range(len(lst)-1):
        if lst[i+1]>=lst[i]:
            if (lst[i+1]-lst[i])>diff:
                diff=lst[i+1]-lst[i]
                c+=1
        else:
            if (lst[i]-lst[i+1])>diff:
                diff=lst[i]-lst[i+1]
                c+=1
    if c==(len(lst)-1):
        return("True")
    else:
        return("False")

#  MAIN
lst=eval(input())
out=function_expanding(lst)
print(out)