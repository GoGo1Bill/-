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
 
myToken = "xoxb-2609205237909-2597943438071-dQu7rGXpIJNVCYJIPfaPoyLp"

def get_start_time(KRWAXS):
    df0 = pyupbit.get_ohlcv("KRW-AXS", interval="day", count=1)
    start_time = df0.index[0]
    return start_time

while True:
     try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-AXS")
        end_time = start_time + datetime.timedelta(days=1)

        df1 = pyupbit.get_ohlcv("KRW-AXS", interval="minute15", count=3)
        target = df1.iloc[-2]['close'] - df1.iloc[0]['open']
        volume = df1.iloc[2]['volume']
        
        df2 = pyupbit.get_ohlcv("KRW-AXS", interval="minute1", count=1)
        current = df2.iloc[0]['close']

        if start_time < now < end_time:
            if target >= 1800 or target <= -1800 and volume > 20000  :

                 post_message(myToken,"#test", "AXS : " + str(current))
                 print(current)
                 time.sleep(30)
        
            else :
                 keep = 1800 < target < -1800
                 print(keep)
                 print(target)
                 print(current)
                 print(volume)
                 time.sleep(30)
                 
                          
     except Exception as e:
        print(e)
        time.sleep(30)