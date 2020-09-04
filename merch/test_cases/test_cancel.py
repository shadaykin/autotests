import random
import time
import merch.variables as var
from merch.functions.order import Orders
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestCancel:

    order = Orders()
    gateway = var.gateway
    env = var.enviroment

    def test_cancel_simple_registered(self):
        error = 'Invalid order status'
        '''отмена списания денег с простого заказа со статусом registered'''
        create = self.order.create_order(10, var.gateway)
        id = create.json()['id']
        cancel = self.order.cancel_order(id)
        assert cancel.status_code == 400
        assert error in cancel.text

    def test_cancel_simple_paid(self):
        '''отмена списания денег с простого заказа со статусом paid'''
        error = 'Invalid order status'
        id = self.order.full_paid('simple')
        cancel = self.order.cancel_order(id)
        assert cancel.status_code == 400
        assert error in cancel.text

    def test_cancel_simple_refunded(self):
        '''отмена списания денег с простого заказа со статусом refunded'''
        error = 'Invalid order status'
        id = self.order.full_paid('simple')
        refund = self.order.refund_order(id)
        assert refund.status_code == 200
        time.sleep(2)
        cancel = self.order.cancel_order(id)
        assert cancel.status_code == 400
        assert error in cancel.text

    def test_cancel_preauth_registered(self):
        error = 'Invalid order status'
        '''отмена списания денег с двухстадийного заказа со статусом registered'''
        create = self.order.create_order(10, var.gateway, "pre_auth_payment")
        id = create.json()['id']
        cancel = self.order.cancel_order(id)
        assert cancel.status_code == 400
        assert error in cancel.text

    def test_cancel_preauth_held(self):
        '''отмена списания денег с двухстадийного заказа со статусом held'''
        create = self.order.create_order(10, self.gateway, "pre_auth_payment")
        id = create.json()['id']
        url = create.json()['form_url']
        self.order.enter_data_card(self.gateway, url, "success_num")
        time.sleep(3)
        cancel = Orders().cancel_order(id)
        assert cancel.status_code == 200


    def test_cancel_preauth_refunded(self):
        '''отмена списания денег с двухстадийного заказа со статусом refunded'''
        error = 'Invalid order status'
        id = self.order.full_paid('pre_auth_payment')
        time.sleep(2)
        refund = self.order.refund_order(id)
        assert refund.status_code == 200
        time.sleep(2)
        cancel = self.order.cancel_order(id)
        assert cancel.status_code == 400
        assert error in cancel.text

    def test_cancel_preauth_paid(self):
        '''отмена списания денег с двухстадийного заказа со статусом paid'''
        error = 'Invalid order status'
        id = self.order.full_paid('pre_auth_payment')
        time.sleep(2)
        cancel = self.order.cancel_order(id)
        assert cancel.status_code == 400

