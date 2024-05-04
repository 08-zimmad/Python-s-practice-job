# ctypes
import ctypes
def ref_count(address):
 return ctypes.c_int.from_address(address).value
counter=2
address=id(counter)
print(counter)
print("Ref: ",ref_count(address))
remem=counter
print(ref_count(1))
# ctypes.c_long.from_address(counter_id).value



# def get_string_from_addr(addr):
#  return ctypes.c_char_p.from_address(addr).value.decode('utf-8')

# string="my"
# address=id(string)
# print(address)
# print("ref: ", get_string_from_addr(address))
# print(get_string_from_addr("my name is zimmad"))