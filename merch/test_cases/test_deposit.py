import random
import time
import merch.variables as var
from merch.functions.order import Orders
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestCase:

    order = Orders()
    gateway = var.gateway
    env = var.enviroment

    def test_deposit_simple_registered(self):
        error = 'Invalid order status'
        """списание денег с простого заказа со статусом registered"""
        create = self.order.create_order(10, var.gateway)
        id = create.json()['id']
        deposit = self.order.deposit_order(id)
        assert deposit.status_code == 400
        assert error in deposit.text

    def test_deposit_simple_paid(self):
        """списание денег с простого заказа со статусом paid"""
        error = 'Invalid order status'
        id = self.order.full_paid('simple')
        deposit = self.order.deposit_order(id)
        assert deposit.status_code == 400
        assert error in deposit.text

    def test_deposit_simple_refunded(self):
        """списание денег с простого заказа со статусом refunded"""
        error = 'Invalid order status'
        id = self.order.full_paid('simple')
        refund = self.order.refund_order(id)
        assert refund.status_code == 201
        time.sleep(2)
        deposit = self.order.deposit_order(id)
        assert deposit.status_code == 400
        assert error in deposit.text

    def test_deposit_preauth_registered(self):
        error = 'Invalid order status'
        """списание денег с двухстадийного заказа со статусом registered"""
        create = self.order.create_order(10, var.gateway, "pre_auth_payment")
        id = create.json()['id']
        deposit = self.order.deposit_order(id)
        assert deposit.status_code == 400
        assert error in deposit.text

    def test_deposit_preauth_held(self):
        """списание денег с двухстадийного заказа со статусом held"""
        create = self.order.create_order(10, self.gateway, 'pre_auth_payment')
        id = create.json()['id']
        url = create.json()['form_url']
        browser = self.order.enter_data_card(self.gateway, url, "success_num")
        browser.close()
        wait = self.order.wait_status(id, 'held')
        deposit = self.order.deposit_order(id)
        assert deposit.status_code == 204
        paid = self.order.wait_status(id,'paid')

    def test_deposit_preauth_refunded(self):
        """списание денег с двухстадийного заказа со статусом refunded"""
        error = 'Invalid order status'
        id = self.order.full_paid('pre_auth_payment')
        self.order.wait_status(id, 'paid')
        refund = self.order.refund_order(id)
        assert refund.status_code == 201
        time.sleep(2)
        deposit = self.order.deposit_order(id)
        assert deposit.status_code == 400
        assert error in deposit.text

    def test_deposit_preauth_paid(self):
        """списание денег с двухстадийного заказа со статусом paid"""
        error = 'Invalid order status'
        id = self.order.full_paid('pre_auth_payment')
        paid = self.order.wait_status(id,'paid')
        deposit = self.order.deposit_order(id)
        assert deposit.status_code == 400
        assert error in deposit.text

    def test_deposit_partly(self):
        """Частичное списание денег с двухстадийного заказа со статусом held"""
        create = self.order.create_order(10, self.gateway, 'pre_auth_payment')
        id = create.json()['id']
        url = create.json()['form_url']
        browser = self.order.enter_data_card(self.gateway, url, "success_num")
        browser.close()
        self.order.wait_status(id, 'held')
        deposit = self.order.deposit_order(id, "6")
        assert deposit.status_code == 204
        self.order.wait_status(id,'paid')
        amount = self.order.status_order_in_merch(id)
        assert amount.json()['amount'] == "6.00"

    def test_deposit_with_other_token(self):
        """Списание суммы заказа, принадлежащего другому клиенту"""
        create = self.order.create_order(10, self.gateway, 'pre_auth_payment')
        id = create.json()['id']
        url = create.json()['form_url']
        browser = self.order.enter_data_card(self.gateway, url, "success_num")
        browser.close()
        self.order.wait_status(id, 'held')
        header = {'Authorization': 'Token ' + var.tokens['other'+self.env.split('test')[1]]}
        deposit = requests.post(var.enviroments[self.env]+(var.processing_endpoints['deposit']) % id, headers=header)
        assert deposit.status_code == 404

