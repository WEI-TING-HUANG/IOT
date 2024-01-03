# IOT作業
# 緣由：
由於同事送我的平平安安（富士山蘋果）於睡覺前放於餐廳，隔天早上起床後，我的蘋果被不知明物體咬了一口，所以設計了一個裝置，當有不明物體靠近時，可以監控及做到驅趕的效果。

# 構想：
透過紅外線感測器，當發現物體靠近時則發line notify，訊息中包含網址，可透過網址連至樹莓派上所架設的Web Server，可透過Web Server執行監控及發出響音驅趕不明物體。

# 服務架構圖：

<img width="416" alt="image" src="https://github.com/WEI-TING-HUANG/IOT/assets/155205404/4da21e3a-2927-4ea3-a45d-a4b387dcaed5">

# 需要的裝置：
1.	樹莓派
2.	紅外線感測器
3.	鏡頭
4.	蜂鳴器

# 建置步驟：
1.	取得line notify的token，並架設紅外線感測器，程式可參考PIR_SIMPLE.py
2.	Web Server是透過Flask架設，Web Server及監控程式可參考app.py及camera.py及templates底下的index.html

# 照片
外表<br/>
<img width="416" alt="image" src="https://github.com/WEI-TING-HUANG/IOT/assets/155205404/d55427dc-d306-45da-b22f-f78c7870f514">
<br/>
內部長像<br/>
<img width="416" alt="image" src="https://github.com/WEI-TING-HUANG/IOT/assets/155205404/0b5cce1a-34eb-461c-9e34-949ff04c9e30">

# 影片
https://youtu.be/ic1j1oKyvjQ
