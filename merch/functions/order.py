import random
import time
import merch.variables as var
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class Orders:

    env = var.enviroments[var.enviroment]
    header = {'Authorization': 'Token ' + var.tokens[var.enviroment]}

    card_yakassa = var.cards_yakassa
    card_gpb = var.cards_gpb

    def create_order(self, amount, gateway, *args, **kwargs):
        """Создание заказа
        В зависимости от кейса заказ может быть:
        - одностадийный простой - args = null,
        - двухстадийный - pre_auth_payment in args,
        - сохраненный способ оплаты - save_payment_method and pass_id in args,
        - оплата по связке - binding_id (and pass_id) in args,
        - рекуррентный + двухстадийный - pre_auth_payment and (save_payment_method and pass_id
         or binding_id) in args"""

        client_order_id = 'autotest_order_' + str(random.randint(0, 10000))
        if len(args) == 0:
            data = {
                "return_url": var.order_options['return_url'],
                "payment_gateway": gateway,
                "client_order_id": client_order_id,
                "amount": amount,
                "fail_url": var.order_options['fail_url']}
        elif 'pre_auth_payment' in args and len(args) == 1:
            data = {
                "return_url": var.order_options['return_url'],
                "payment_gateway": gateway,
                "client_order_id": client_order_id,
                "amount": amount,
                "fail_url": var.order_options['fail_url'],
                "pre_auth_payment": True}
        elif 'save_payment_method' in args and len(args) == 1:
            data = {
                "return_url": var.order_options['return_url'],
                "payment_gateway": gateway,
                "client_order_id": client_order_id,
                "amount": amount,
                "fail_url": var.order_options['fail_url'],
                "save_payment_method": True,
                "customer_id": "111" + str(random.randint(1000,2000)),
                "pass_id": "111" + str(random.randint(1000,2000))}
        elif 'pre_auth_payment' in args and 'save_payment_method' in args:
            data = {
                "return_url": var.order_options['return_url'],
                "payment_gateway": gateway,
                "client_order_id": client_order_id,
                "amount": amount,
                "fail_url": var.order_options['fail_url'],
                "save_payment_method": True,
                "customer_id": "111" + str(random.randint(1000, 2000)),
                "pass_id": "111" + str(random.randint(1000, 2000)),
                "pre_auth_payment": True}
        elif 'binding' in args and len(args) == 2:
            data = {
                "return_url": var.order_options['return_url'],
                "payment_gateway": gateway,
                "client_order_id": client_order_id,
                "amount": amount,
                "fail_url": var.order_options['fail_url'],
                "binding_id": args[1]}
        create = requests.post(self.env+var.processing_endpoints['order'], headers=self.header, data=data)
        return create

    def status_order_in_merch(self, orderid):
        """Проверка статуса заказа в Merch"""
        status = requests.get(self.env + var.processing_endpoints['order']+orderid+'/', headers=self.header)
        return status

    def deposit_order(self, orderid, *args):
        """Списание средств при двухстадийном платеже,
        если указан 2-ий параметр (сумма), то будет списываться указанная сумма"""
        if len(args) == 1:
            data = {"amount": args[0]}
            deposit = requests.post(self.env + str(var.processing_endpoints['deposit']) % orderid, headers=self.header, data=data)
        else:
            deposit = requests.post(self.env + str(var.processing_endpoints['deposit']) % orderid, headers=self.header)
        return deposit

    def cancel_order(self, orderid, *args):
        """Отмена списания средств при двухстадийном платеже"""
        if len(args) == 1:
            data = {"amount": args[0]}
            cancel = requests.post(self.env + str(var.processing_endpoints['cancel']) % orderid, headers=self.header, data=data)
        else:
            cancel = requests.post(self.env + str(var.processing_endpoints['cancel']) % orderid, headers=self.header)
        return cancel

    def refund_order(self, orderid, *args):
        """Возврат оплаты"""
        if len(args) == 0:
            data = {"amount": "1"}
        else:
            data = {"amount": args[0]}
        refund = requests.post(self.env + str(var.processing_endpoints['refund']) % orderid, headers=self.header, data=data)
        return refund

    def activate_binding(self, binding_id):
        """Активация связки"""
        activate = requests.post(self.env + var.processing_endpoints['bindings']
                                 + binding_id + '/activate/', headers=self.header)
        return activate

    def deactivate_binding(self, binding_id):
        """Деактивация связки"""
        deactivate = requests.post(self.env + var.processing_endpoints['bindings'] + binding_id + '/deactivate/', headers=self.header)
        return deactivate

    def get_bindings(self, pass_id):
        """Получение списка связок пользователя"""
        get_binding = requests.get(self.env + var.processing_endpoints['bindings'] + pass_id, headers=self.header)
        return get_binding

    def enter_data_card(self, gateway, url, case):
        """Ввод данных карты на форме оплаты, в зависимости от шлюза.
        Существуют кейсы для параметра case:
        - success_num - успешная оплата
        - block_to_limit - неуспешная оплата по причине блокировки средств или их недостаток
        - card_expired - карта просрочена ТОЛЬКО для Я.Кассы
        - error_3DS - ошибка при прохождении 3d-secure"""
        browser = webdriver.Chrome()
        browser.get(url)
        a = 0
        result = False
        if gateway == 'gpb':
            card_num = browser.find_element_by_id('pan')
            month = browser.find_element_by_id('month')
            year = browser.find_element_by_id('year')
            cvc = browser.find_element_by_id('cvc')
            confirm = browser.find_element_by_id('btnConfirm')
            try:
                email = browser.find_element_by_id('email')
                email.send_keys(var.email)
            except:
                pass
            card_num.send_keys(self.card_gpb[case])
            month.send_keys(self.card_gpb['expiration_month'])
            year.send_keys(self.card_gpb['expiration_year'])
            cvc.send_keys(self.card_gpb['cvc'])
            confirm.click()
            while not result and a < 10:
                try:
                    assert '/auth/start.do' in browser.current_url
                    result = True
                except:
                    time.sleep(1)
                    a += 1
            assert result is True
            time.sleep(3)
            password = browser.find_element_by_name('password')
            password.send_keys(self.card_gpb['password'])
            password.submit()
        if gateway == 'yakassa':
            card_num = browser.find_element_by_id('cardNumber')
            month = browser.find_element_by_name('skr_month')
            year = browser.find_element_by_name('skr_year')
            cvc = browser.find_element_by_name('skr_cardCvc')
            try:
                email = browser.find_element_by_name('cps_email')
                email.send_keys(var.email)
            except:
                pass
            card_num.send_keys(self.card_yakassa[case])
            month.send_keys(self.card_yakassa['expiration_month'])
            year.send_keys(self.card_yakassa['expiration_year'])
            cvc.send_keys(self.card_yakassa['cvc'])
            cvc.submit()
            cvc.send_keys(Keys.RETURN)
            while not result and a < 10:
                try:
                    assert 'success' in browser.current_url
                    result = True
                except:
                    time.sleep(1)
                    a += 1
            assert result is True
        time.sleep(1)
        return browser

    def full_paid(self, case, *args):
        """Полная оплата заказа для определенного кейса
        pre_auth_payment - двухстадийный заказ,
        save_payment_method - с сохраненным способом оплаты,
        simple - простой заказ,
        binding + binding_id - оплата по связке"""
        if case == 'pre_auth_payment':
            order = self.create_order(10, var.gateway, "pre_auth_payment")
            url = order.json()['form_url']
            enter = self.enter_data_card(var.gateway, url, "success_num")
            enter.close()
            id = order.json()['id']
            info = self.status_order_in_merch(id)
            status = info.json()['status']
            print(status)
            time.sleep(2)
            if len(args) == 1:
                self.deposit_order(id, args[0])
            else:
                self.deposit_order(id)
            info = self.status_order_in_merch(id)
            status = info.json()['status']
            print(status)
            print(id)
            return id
        if case == "save_payment_method":
            order = self.create_order(10, var.gateway, "save_payment_method")
            url = order.json()['form_url']
            enter = self.enter_data_card(var.gateway, url, "success_num")
            enter.close()
            id = order.json()['id']
            time.sleep(2)
            info = self.status_order_in_merch(id)
            status = info.json()['status']
            binding = info.json()['binding_id']
            print(binding)
            print(status)
            print(id)
            return id, binding
        if case == 'simple':
            order = self.create_order(10, var.gateway)
            url = order.json()['form_url']
            enter = self.enter_data_card(var.gateway, url, "success_num")
            enter.close()
            id = order.json()['id']
            time.sleep(2)
            info = self.status_order_in_merch(id)
            status = info.json()['status']
            print(status)
            print(id)
            return id
        if case == 'binding' and len(args) == 1:
            order = self.create_order(10, var.gateway, "binding", args[0])
            id = order.json()['id']
            time.sleep(3)
            status = self.status_order_in_merch(id)
            print(id)
            print(status.json()['status'])
            return id

    def wait_status(self, id, status):
        """функция, ожидающая перехода заказа в переданный статус"""
        a = False
        b = 0
        while not a and b < 30:
            fact = self.status_order_in_merch(id)
            if fact.json()['status'] == status:
                a = True
            else:
                time.sleep(1)
                b +=1
        assert a is True
        return a



