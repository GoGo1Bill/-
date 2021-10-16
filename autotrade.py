import datetime
import time
import pyupbit
import requests

def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxb-2609205237909-2635866947824-BrPYWlwX1w8CRAV1DSXlS8oC"

df = pyupbit.get_ohlcv("KRW-DOGE", interval="minute5", count=1)
target = df.iloc[0]['open'] - df.iloc[0]['close']

    
def get_start_time(KRWDOGE):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv("KRW-DOGE", interval="day", count=1)
    start_time = df.index[0]
    return start_time

df = pyupbit.get_ohlcv("KRW-DOGE", interval="minute5", count=1)
current = df.iloc[0]['close']

while True:
     try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-DOGE")
        end_time = start_time + datetime.timedelta(days=1)

        if start_time < now < end_time:
            if target > 2 or target <-2:
                 post_message(myToken,"#test", "price : " +str(current))
                 print(current)

     except Exception as e:
        print(e)
        post_message(myToken,"#test", e)
        time.sleep(7200)