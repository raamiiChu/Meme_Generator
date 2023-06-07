![meme](https://github.com/raamiiChu/NCCU_111-2_DCT_Artificial-Intelligence-and-Digital-Content_Group8_DEMO/assets/87169493/caa3fe26-5f7a-42f8-9989-6c72a8902ccc)


# 在終端機執行指令  
```
pip install -r requirements.txt
```
##### 如果失敗的話，逐一執行以下指令
```
pip install flask
pip install line-bot-sdk
pip install gradio
pip install selenium
pip install chromedriver-binary
pip install transformers
pip install ckip-transformers
```

# 說明
將 Predis AI 串接到 Linebot 以及 Gradio  

##### 流程  
1. 對輸入文本進行預處理  
2. 假如預處理結果至少有 4 個詞彙則開始執行網路爬蟲  

##### 使用套件  
- **selenium**
  - 網址：https://predis.ai/free-ai-tools/ai-meme-generator/#  
  - 透過網路爬蟲，使用現成 AI 製作迷因  
- **ckip-transformers**
  - 用於預處理文本
  - https://github.com/ckiplab/ckip-transformers

# meme_gen_gradio.py  
- 直接執行即可，會回傳本地端網址，以及分享用網址  
- 若中止執行，則 2 份網址皆會刪除  

# meme_gen_linebot.py  
## 操作影片：https://www.youtube.com/watch?v=J3cmRowF5RU

1. 在 ngrok 依序執行以下指令，[ngrok 下載連結](https://ngrok.com/download)  
  ```
  ngrok authtoken "你的 authtoken"
  ngrok http 5000
  ```
  執行完會獲得一組網址  
  ```
  https:// ...... .ngrok-free.app
  ```

2. 修改 Channel access token, Channel secret，執行 meme_gen_linebot.py

  ```
  15 line_bot_api = LineBotApi('Channel access token')
  16 handler = WebhookHandler('Channel secret')
  ```

3. 在 ngrok 網址 尾端加上 "/webhook" ，貼在如下位置  
![Messaging API](https://github.com/raamiiChu/Meme_Generator/assets/87169493/6f69ac71-038b-4a24-8b11-51c88aa38866)
![upload url](https://github.com/raamiiChu/Meme_Generator/assets/87169493/e654d04d-7792-4633-ae84-be460cde03b1)

4. 點擊 "Verify" 出現以下畫面代表成功  
![check is success](https://github.com/raamiiChu/Meme_Generator/assets/87169493/60739db3-d2a0-496b-995b-20b03e9b1865)
