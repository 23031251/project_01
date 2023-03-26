shop_list = ['Potato', 'Pea', 'Rice', 'Bread']
c = 'Fish'
shop_list_fruits = ['Apple', 'Orange', 'Strawberry']
# action a
a = shop_list.index('Pea')
b = shop_list.index('Rice')
shop_list.insert(b, c)
print('action a result: ', shop_list)
#  action b
shop_list.extend(shop_list_fruits)
print('action b result: ', shop_list)
# action c
shop_list.remove('Potato')
print('action c result: ', shop_list)
# action d
d = shop_list.index('Bread')
e = shop_list.index('Orange')
print('Bread position: ', d+1)
print('Orange position: ', e+1)
# print(shop_list)