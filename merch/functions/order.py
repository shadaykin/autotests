import requests
import variables as var
import random


class Orders:

    env = var.enviroments[var.enviroment]
    header = {'Authorization': 'Token ' + var.token}

    def create_order(self, amount, gateway, *args):
        """Создание заказа
        В зависимости от кейса заказ может быть:
        - одностадийный простой - args = null,
        - двухстадийный - pre_auth_payment in args,
        - рекуррентный - save_payment_method in args,
        - рекуррентный + двухстадийный - pre_auth_payment and save_payment_method in args"""

        client_order_id = 'autotest_order_' + str(random.randint(0, 10000))
        if len(args) == 0:
            data = {
                "success_url": var.order_options['success_url'],
                "payment_gateway": gateway,
                "client_order_id": client_order_id,
                "amount": amount,
                "fail_url": var.order_options['fail_url']}
        elif 'pre_auth_payment' in args and 'save_payment_method' not in args:
            data = {
                "success_url": var.order_options['success_url'],
                "payment_gateway": gateway,
                "client_order_id": client_order_id,
                "amount": amount,
                "fail_url": var.order_options['fail_url'],
                "pre_auth_payment": True}
        elif 'pre_auth_payment' not in args and 'save_payment_method' in args:
            data = {
                "success_url": var.order_options['success_url'],
                "payment_gateway": gateway,
                "client_order_id": client_order_id,
                "amount": amount,
                "fail_url": var.order_options['fail_url'],
                "save_payment_method": True,
                "pass_id": "pass_id" + str(random.randint(1000,2000))}
        elif 'pre_auth_payment' in args and 'save_payment_method' in args:
            data = {
                "success_url": var.order_options['success_url'],
                "payment_gateway": gateway,
                "client_order_id": client_order_id,
                "amount": amount,
                "fail_url": var.order_options['fail_url'],
                "save_payment_method": True,
                "pass_id": "pass_id" + str(random.randint(1000, 2000)),
                "pre_auth_payment": True}

        create = requests.post(self.env+var.processing['order'], headers=self.header, data=data)
        return create

    def status_order_in_merch(self, orderid):
        status = requests.get(self.env + var.processing['order']+orderid, headers=self.header)
        return status


#test_create = Orders().create_order('5', 'gpb')
test_status = Orders().status_order_in_merch('7955cae7-2f1e-4a9c-b7da-a37fbaa5ad2f')

print(test_status.status_code)
print(test_status.json())