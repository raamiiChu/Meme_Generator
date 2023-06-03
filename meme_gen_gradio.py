# 函式註解
from typing import *

import gradio as gr

# 從 ./crawler.py 載入
from crawler import MemeGeneratorPredisAI, text_preprocessing

# 輸入字串，回傳字串或圖片
def meme_generator(input_text: str) -> str:
    # 對輸入文本進行預處理，回傳 List[str]
    text = text_preprocessing([input_text])
    URL = "https://predis.ai/free-ai-tools/ai-meme-generator/#"

    # 至少 4 個詞彙才會執行
    if len(text) >= 4:
        # 詞彙之間以空格做間隔
        text = " ".join(text)

        # 開始網路爬蟲
        Generator = MemeGeneratorPredisAI(URL)
        Generator.open_webdriver()
        meme_url = Generator.genrate_meme(text)
        Generator.close()

        # 有小機率會產圖失敗
        if meme_url == "https://brain.predis.ai/templates_images/644252de15522fe7315e3009_1.jpeg":
            return "./error_pictures/error_fail_gen.png"
        else:
            return meme_url
    else:
        return "./error_pictures/error_4_words.png"

# 設定 css 屬性
# svelte-2xzfnp -> 輸入欄位
# svelte-1h4gtph -> "製作迷因" 按鈕
# svelte-opdjbj -> "Examples" 字體
# gallery -> "Examples" 下方的範例情境文本
css = """
.svelte-2xzfnp {
    font-size: 1rem !important;
}
.svelte-1h4gtph {
    font-size: 1.2rem !important;
}
.svelte-opdjbj {
    font-size: 1.2rem !important;
}
.gallery {
    font-size: 1rem !important;
}
"""

with gr.Blocks(css=css) as iface: 
    gr.Markdown("## 請輸入情境（至少 4 個詞彙）")
    
    # 輸入欄位
    input_text = gr.Textbox(
        label = "input_text", 
        placeholder = "請輸入情境（至少 4 個詞彙）", 
        max_lines = 1,
        show_label = False
    )
    # 生成按鈕
    btn_generate = gr.Button("製作迷因")
    
    # 範例情境
    gr.Markdown("#### 範例情境")
    gr.Examples(
        examples = [
            ["你們抓捕周樹人跟我魯迅有甚麼關係"], 
            ["學習 python 之後，再學習 C++ 令人絕望"],
            ["是不小心還是故意的 是故意不小心的"]
        ],
        inputs = [input_text],
        fn = meme_generator
    )
    gr.Markdown("---")
    
    # 輸出欄位
    gr.Markdown("## 輸出迷因")
    output_img = gr.Image(
        type = "filepath", 
        label = "output_img",
        show_label = False
    )
    
    # 點擊按鈕事件
    btn_generate.click(
        fn = meme_generator, 
        inputs = input_text,
        outputs = output_img
    )
    
if __name__ == "__main__":
    # share=True
    iface.launch(share=True, inbrowser=True)