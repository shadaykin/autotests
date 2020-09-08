import random
import time
import merch.variables as var
from merch.functions.order import Orders
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestRefunds:

    order = Orders()
    gateway = var.gateway
    env = var.enviroment

    def test_refund_simple(self):
        """Возврат простого заказа"""
        order = self.order.full_paid('simple')
        paid = self.order.wait_status(order, "paid")
        assert paid is True
        refund = self.order.refund_order(order, 10).json()
        refunded = self.order.wait_status(order, "refunded")
        assert refunded is True
        assert refund['amount'] == '10.00'


    def test_refund_pre_auth(self):
        """Возврат двухстадийного заказа"""
        order = self.order.full_paid("pre_auth_payment")
        paid = self.order.wait_status(order, "paid")
        assert paid is True
        refund = self.order.refund_order(order, 10).json()
        refunded = self.order.wait_status(order, "refunded")
        assert refunded is True
        assert refund['amount'] == "10.00"

    def test_refund_save(self):
        """Возврат заказа с сохраненным способом оплаты"""
        order = self.order.full_paid("save_payment_method")
        paid = self.order.wait_status(order[0], "paid")
        assert paid is True
        refund = self.order.refund_order(order[0], 10).json()
        refunded = self.order.wait_status(order[0], "refunded")
        assert refunded is True
        assert refund['amount'] == "10.00"

    def test_refund_binding(self):
        """Возврат рекуррентного заказа"""
        order = self.order.full_paid('save_payment_method')
        paid = self.order.wait_status(order[0], "paid")
        assert paid is True
        binding = self.order.full_paid("binding", order[1])
        paid = self.order.wait_status(binding, "paid")
        assert paid is True
        refund = self.order.refund_order(binding, 10).json()
        refunded = self.order.wait_status(binding, "refunded")
        assert refunded is True
        assert refund['amount'] == "10.00"

    def test_partly_refund(self):
        """Частичный возврат простого заказа"""
        order = self.order.full_paid('simple')
        paid = self.order.wait_status(order, "paid")
        assert paid is True
        refund = self.order.refund_order(order).json()
        refunded = self.order.wait_status(order, "refunded")
        assert refunded is True
        assert refund['amount'] == "1.00"

    def test_some_refunds(self):
        """Несколько возвратов для одного заказа"""
        order = self.order.full_paid('simple')
        paid = self.order.wait_status(order, "paid")
        assert paid is True
        refund = self.order.refund_order(order, 3).json()
        refunded = self.order.wait_status(order, "refunded")
        assert refunded is True
        assert refund['amount'] == "3.00"
        refund = self.order.refund_order(order, 5).json()
        refunded = self.order.wait_status(order, "refunded")
        assert refunded is True
        assert refund['amount'] == "5.00"
        status = self.order.status_order_in_merch(order)
        assert status.json()['refunded_amount'] == 8.0

    def test_error_status(self):
        """Возврат заказа при некорректном статусе != paid/refunded"""
        error = 'Invalid order status'
        register = self.order.create_order(10, self.gateway).json()
        id = register['id']
        assert register['status'] == 'registered'
        refund = self.order.refund_order(id)
        assert refund.status_code == 400
        assert error in refund.text

    def test_refund_with_other_token(self):
        """Возврат заказа, принадлежащего другому клиенту"""
        id = self.order.full_paid('simple')
        self.order.wait_status(id, 'paid')
        data = {"amount": "1.00"}
        header = {'Authorization': 'Token ' + var.tokens['other'+self.env.split('test')[1]]}
        refund = requests.post(var.enviroments[self.env]+(var.processing_endpoints['refund']) % id, headers=header, data=data)
        assert refund.status_code == 404






