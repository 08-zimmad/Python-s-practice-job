# using methods
def using_methods(list):

    print(min(list))
    print(max(list))



# without method
def without_methods(list):
    min=list[0]
    max=list[0]
    for num in list:
        if num>max:
            max=num
        else:
            min=num

    return [min,max]

if "__main__":
    list=[1,2,3,4,5]
    using_methods(list)
    print(without_methods(list))

