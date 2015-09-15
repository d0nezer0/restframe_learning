# -*- coding: utf-8 -*-
# 设置api的分级权限和用户权限的配置文件.

API_LEVEL = (
    (1, (u'api/update_product/', u'api/update_company/')),
    (2, (u'api/update_user/', u'api/pay/')),
    (3, (u'api/update_self_info',)),
    (4, (u'api/get_product',)),
)

CLIENT_LEVEL = (
    (1, (u'google', u'facebook', u'microsoft')),
    (2, (u'ali', u'baidu', u'tencent')),
    (3, (u'360', u'jd', u'huawei')),
    (4, (u'xicai', u'zhongniu', u'zhongjin')),
)

PRIVILEGE_DICT = {u'xicai': (u'api/update_user/', u'api/pay/'),
                  u'wanglibao': (u'api/update_product/', u'api/update_company/', u'api/pay/'),
                  u'360': (u'sss'),
                  }
