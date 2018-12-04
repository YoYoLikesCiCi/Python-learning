# -*- coding: UTF-8 -*-
#工作日的力量，一周5个工作日，进步1%，2个休息日，退步1%
#daydayup q3.py
dayfactory = 0.01
dayup = 1.0
for i in range(365):
    if i % 7 in [6,0]:
        dayup = dayup*(1-dayfactory)
    else:
        dayup = dayup*(1+dayfactory)
print("工作日的力量：{:.2f}".format(dayup))
