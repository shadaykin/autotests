from functions.order import Orders
import variables as var
import random


#Оплата простого заказа
print("Simple:")
simple = Orders().full_paid("simple")
'''
#Оплата двухстадийного заказа
print("Pre_auth:")
pre_auth = Orders().full_paid("pre_auth_payment")

#Оплата с сохраненным способом
print("Save:")
save = Orders().full_paid("save_payment_method")
print(save)

#Оплата по binding_id из предыдущего шага
print("Binding:")
binding = Orders().full_paid("binding", save[1])
print(binding)
#Возврат средств
print("Refund:")
refund = Orders().refund_order(simple)
'''









