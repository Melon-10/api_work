import hashlib
import time

from faker import Faker
di=[]
# 1、姓名
fk = Faker(locale="zh-CN")
name = fk.name()
dit={"姓名":name}
di.append(dit)
# print(di)

# 2、身份证
card = fk.ssn()
# print(card)
dit={"身份证号":card}
di.append(dit)
print(di)
print(di[0]["姓名"])
