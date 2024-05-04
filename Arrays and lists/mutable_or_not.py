# dynamic / mutabel or immutabe
# low = [1, 2, 3]
# high = [4, 5]
# med=[6,8,9]
# rankings = (low, high)
# print(rankings)
# print('init address',id(rankings))
# print(type(rankings).__name__)
# rankings = (med,low, high)
# print(rankings)
import ctypes

ranks = "my name is zimmad arshad"
rates = "my name is zimmad arshad"
print(id(ranks))
print(id(rates))
result = ranks is rates
print(result)
