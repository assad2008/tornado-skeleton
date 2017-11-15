# coding=utf-8

import time

from paycenter.models.schemas import Orders
from paycenter.common.readamount import paseramount


class orderModel(object):

    def __init__(self):
        self.tab = Orders

    def get_one_order(self, orderid):
        try:
            return self.tab.get(self.tab.orderid == orderid)
        except:
            return None

    def get_one_order_by_cporderid(self, cporderid):
        try:
            return self.tab.select().where(self.tab.cporderid == cporderid).get()
        except:
            return None

    def create_order(self, orderid, kwagrs):
        ordercreate = self.tab.create(
            orderid=orderid,
            cporderid=kwagrs.get("cporderid"),
            ordertype=0,
            orderchannel=kwagrs.get("orderchannel"),
            uid=kwagrs.get("uid"),
            account_id=kwagrs.get("account_id"),
            productid=kwagrs.get("productid"),
            companyid=kwagrs.get("companyid"),
            channelid=kwagrs.get("channelid"),
            appid=kwagrs.get("appid"),
            amount=kwagrs.get("amount"),
            amountunit=kwagrs.get("amountunit"),
            cpprice=kwagrs.get("cpprice"),
            currency=kwagrs.get("currency"),
            currencycode=kwagrs.get("currencycode"),
            merpriv=kwagrs.get("merpriv"),
            realamout="",
            denomination=kwagrs.get("denomination"),
            gameversionname=kwagrs.get("denomination"),
            gameroleid=kwagrs.get("gameroleid"),
            gameserverid=kwagrs.get("gameserverid"),
            platformid=kwagrs.get("platformid"),
            osversion=kwagrs.get("platformid"),
            countrycode=kwagrs.get("countrycode"),
            language=kwagrs.get("language"),
            ip_addr=kwagrs.get("ip_addr"),
            orderstatus=1,
            create_at=int(time.time())
        )
        return ordercreate.orderid

    def update_order_amount(self, orderid):
        order = self.tab.get(self.tab.orderid == orderid)
        amount = order.originalamount
        amounts, unit = paseramount(amount)
        orderupdate = self.tab.update(
            amount=amount,
            amoutunit=unit
        ).where(self.tab.orderid == orderid)
        orderupdate.execute()
