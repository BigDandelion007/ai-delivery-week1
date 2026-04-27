# -*- coding: utf-8 -*-
import os 

LOG_FILE = 'ai-delivery-week1/test.log'
error_count = warn_count = info_count = 0

with open(LOG_FILE,'r',encoding='utf-8') as f:
    for line in f:
        if "ERROR" in line:
            error_count += 1
        elif "WARN" in line:
            warn_count += 1
        elif "INFO" in line:
            info_count += 1

print(f"日志统计结果：")
print(f"INFO:{info_count}条")
print(f"WARN:{warn_count}条")
print(f"ERROR:{error_count}条")

if not os.path.exists('output'):
    os.makedirs('output')

with open('output/log_report.txt','w',encoding='utf-8') as f:
    f.write(f"日志统计结果：\n")
    f.write(f"INFO: {info_count} 条\n")
    f.write(f"WARN: {warn_count} 条\n")
    f.write(f"ERROR: {error_count} 条\n")

print('统计结果已保存到 output/log_report.txt')