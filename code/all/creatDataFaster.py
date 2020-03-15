import pandas as pd
from time import time
import numpy as np
from datetime import datetime
t=time()
sales_people = {"陈天浩": "上海",
                "孙健": "上海",
                "王梓戎": "广东",
                "刘丹": "上海",
                "刘颖": "上海",
                "刘雪": "天津",
                "章洋": "上海",
                "殷琳": "广东",
                "李辉": "北京",
                "王玉": "吉林",
                "侯宁": "上海",
                "吴中岳": "广东",
                "张林": "广东",
                "庄雷": "上海",
                "王宇": "吉林",
                "利坤": "上海",
                "董丹丹": "广东",
                "蔡建平": "山东",
                "陈杨": "吉林",
                "蔡勇": "广东",
                "李琳": "上海",
                "魏苍生": "天津",
                "刘帆": "天津",
                "戴雪": "上海",
                "许亮": "吉林",
                "李智童": "山东",
                "钱国": "山东",
                "郭华锋": "吉林",
                "阎云": "山东",
                "江敏": "上海"}
products = {"苹果": 10,
            "梨": 8,
            "桃": 6.5,
            "葡萄": 15,
            "椰子": 20,
            "西瓜": 30,
            "百香果": 12,
            "榴莲": 50,
            "桔子": 6,
            "香蕉": 7.5}
def get_counterpart(counterpart_dict,source):
    counterpart=counterpart_dict[source]
    return counterpart
def random_dater(start_date,end_date):
    p_start_date=datetime.strptime(start_date,'%Y-%m-%d')
    p_end_date=datetime.strptime(end_date,'%Y-%m-%d')
    days_delta=p_end_date-p_start_date
    days_to_add=np.arange(0,days_delta.days)
    random_date=np.datetime64(
        start_date)+np.random.choice(days_to_add)
    return random_date
sales2=pd.DataFrame(columns=['交易日期','客户ID','售货员','分公司','产品','单价','数量','订单金额'],index=range(100000))
sales2['交易日期']=sales2['交易日期'].apply(lambda row: random_dater('2019-01-01','2019-12-31'))
sales2['客户ID']=sales2['客户ID'].apply(lambda row: "C"+str(np.random.randint(1,1000)).zfill(5))
sales2['售货员']=sales2['售货员'].apply(lambda row: np.random.choice(list(sales_people)))
sales2['分公司']=sales2.apply(lambda row: get_counterpart(sales_people,row['售货员']),axis=1)
sales2['产品']=sales2['产品'].apply(lambda row: np.random.choice(list(products)))
sales2['单价']=sales2.apply(lambda row: get_counterpart(products,row['产品']),axis=1)
sales2['数量']=sales2.apply(lambda row: np.random.randint(1,10000))
sales2['订单金额']=sales2['单价']*sales2['数量']
# sales2.to_hdf('zz.h5',key='z')
print('{0:.2f}s'.format(time()-t))
