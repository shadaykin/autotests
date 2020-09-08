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
        '''списание денег с простого заказа со статусом registered'''
        create = self.order.create_order(10, var.gateway)
        id = create.json()['id']
        deposit = self.order.deposit_order(id)
        assert deposit.status_code == 400
        assert error in deposit.text

    def test_deposit_simple_paid(self):
        '''списание денег с простого заказа со статусом paid'''
        error = 'Invalid order status'
        id = self.order.full_paid('simple')
        deposit = self.order.deposit_order(id)
        assert deposit.status_code == 400
        assert error in deposit.text

    def test_deposit_simple_refunded(self):
        '''списание денег с простого заказа со статусом refunded'''
        error = 'Invalid order status'
        id = self.order.full_paid('simple')
        refund = self.order.refund_order(id)
        assert refund.status_code == 200
        time.sleep(2)
        deposit = self.order.deposit_order(id)
        assert deposit.status_code == 400
        assert error in deposit.text

    def test_deposit_preauth_registered(self):
        error = 'Invalid order status'
        '''списание денег с двухстадийного заказа со статусом registered'''
        create = self.order.create_order(10, var.gateway, "pre_auth_payment")
        id = create.json()['id']
        deposit = self.order.deposit_order(id)
        assert deposit.status_code == 400
        assert error in deposit.text

    def test_deposit_preauth_held(self):
        '''списание денег с двухстадийного заказа со статусом held'''
        create = self.order.create_order(10, self.gateway, 'pre_auth_payment')
        id = create.json()['id']
        url = create.json()['form_url']
        browser = self.order.enter_data_card(self.gateway, url, "success_num")
        browser.close()
        wait = self.order.wait_status(id, 'held')

        deposit = self.order.deposit_order(id)
        assert deposit.status_code == 200
        paid = self.order.wait_status(id,'paid')

    def test_deposit_preauth_refunded(self):
        '''списание денег с двухстадийного заказа со статусом refunded'''
        error = 'Invalid order status'
        id = self.order.full_paid('pre_auth_payment')
        self.order.wait_status(id, 'paid')
        refund = self.order.refund_order(id)
        assert refund.status_code == 200
        time.sleep(2)
        deposit = self.order.deposit_order(id)
        assert deposit.status_code == 400
        assert error in deposit.text

    def test_deposit_preauth_paid(self):
        '''списание денег с двухстадийного заказа со статусом paid'''
        error = 'Invalid order status'
        id = self.order.full_paid('pre_auth_payment')
        paid = self.order.wait_status(id,'paid')
        deposit = self.order.deposit_order(id)
        assert deposit.status_code == 400
        assert error in deposit.text

