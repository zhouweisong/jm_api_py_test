"""
-------------------------------------------------
   File Name：     get_p
   Description :
   Author :       zws
   date：          2018/3/23
-------------------------------------------------
   Change Activity:
                   2018/3/23:
-------------------------------------------------
"""
__author__ = 'zws'

import requests
import re

class GetTicket():

    def get_ticket(self,userid):

        cookie = {"p":"HL01tv1Zau9nvduQbQYIy-nKmbHbs30O2KQpnkP9xc4suAklZVtGXPgeb0KYR6Vo"}
        url = "https://admin.jiemo.com/loginAs"
        body_data = {'user':'%s'%userid}
        r = requests.post(url=url,data=body_data,cookies=cookie,verify=False)
        print(r.text)
        ticket = re.findall(r'"ticket":"(.*?)"',r.text)[0]
        return ticket





