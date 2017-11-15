# coding=utf-8

from paycenter.models.schemas import Molorders


class molorderModel(object):

    def __init__(self):
        self.tab = Molorders

    def get_one_order(self, orderid):
        return self.tab.select().where(self.tab.order_id == orderid)
