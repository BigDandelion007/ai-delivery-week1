# -*- coding: utf-8 -*-
print('Hello AI Delivery!')

services = ['hadoop','spark','flink']
for service in services:
    print(f"服务名称：{service}")

status = {'hadoop':'running','spark':'stopped','flink':'running'}
for service,state in status.items():
    print(f'{service}状态{state}')