# coding=utf-8

from paycenter.models.schemas import Appleorders


class applereceiptModel(object):

    def __init__(self):
        self.tab = Appleorders

    def get_one_receipt(receipt):
        return self.tab.select().where(self.tab.receipt == receipt)

    def get_one_receipt_by_orderid(orderid):
        return self.tab.select().where(self.tab.order_id == orderid)
