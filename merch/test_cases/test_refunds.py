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
        order = self.order.full_paid('simple')
        paid = self.order.wait_status(order, "paid")
        assert paid is True
        refund = self.order.refund_order(order, 10).json()
        refunded = self.order.wait_status(order, "refunded")
        assert refunded is True
        assert refund['refunded_amount'] == 10.0

    def test_partly_refund(self):
        order = self.order.full_paid('simple')
        paid = self.order.wait_status(order, "paid")
        assert paid is True
        refund = self.order.refund_order(order).json()
        refunded = self.order.wait_status(order, "refunded")
        assert refunded is True
        assert refund['refunded_amount'] == 1.0

    def test_some_refunds(self):
        order = self.order.full_paid('simple')
        paid = self.order.wait_status(order, "paid")
        assert paid is True
        refund = self.order.refund_order(order, 3).json()
        refunded = self.order.wait_status(order, "refunded")
        assert refunded is True
        assert refund['refunded_amount'] == 3.0
        refund = self.order.refund_order(order, 5).json()
        refunded = self.order.wait_status(order, "refunded")
        assert refunded is True
        assert refund['refunded_amount'] == 8.0

    def test_error_status(self):
        error = 'Invalid order status'
        register = self.order.create_order(10, self.gateway).json()
        id = register['id']
        assert register['status'] == 'registered'
        refund = self.order.refund_order(id)
        assert refund.status_code == 400
        assert error in refund.text




