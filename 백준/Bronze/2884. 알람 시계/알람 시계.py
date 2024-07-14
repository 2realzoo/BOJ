import sys
import datetime
input = sys.stdin.readline
[hour, min] = map(int, input().rstrip('\n').split())
target_time = datetime.datetime(2000,6,19,hour=hour, minute=min) - datetime.timedelta(minutes=45)
print(str(target_time.hour)+' '+str(target_time.minute))