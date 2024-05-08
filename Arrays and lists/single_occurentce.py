def check_single_occurence(list):
    result=0
    for num in list:
        print(result)
        result=result^num
    return result

if "__main__":
    print(check_single_occurence([1,2,3,2,1]))