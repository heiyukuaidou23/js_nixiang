from datetime import datetime

# 获取当前时间
current_time = datetime.now()

# 将当前时间转换为精确到毫秒的时间戳
timestamp = current_time.timestamp() * 1000

print(int(timestamp))