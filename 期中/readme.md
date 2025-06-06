# 使用python實作一個Python 語言轉譯器
1. main.py — 主程式流程控制
完成方式：chatgpt協助構思+參考+自己修改

參考來源：無直接全部複製，結構參考過 CLI 程式慣例

說明：

讀取 Python 原始碼

呼叫 lexer → parser → transpiler → emitter 的模組

採用命令列參數接收輸入 .py 檔案

使用方式：
bash
複製
編輯
python main.py examples/hello.py
2. lexer.py — 詞法分析器
完成方式：部分原創 + AI 協助撰寫正規表達式

參考來源：參考 Python 正規表達式教學（如 re 模組用法）

說明：

使用 Python re 套件定義 Token 規則

支援基本運算符號、數字、識別字、括號等

輸出 token list，如：[('ID', 'x'), ('ASSIGN', '='), ...]

3. parser.py — 語法分析器
完成方式：AI 協助產出架構 + 自行修改調整

參考來源：

沒有直接複製，但參考了「遞迴下降解析器」的基本架構

說明：

使用簡單的遞迴函數建構 AST（抽象語法樹）

支援數字與加減乘除表達式

建立 Number, BinOp 等 AST 節點類別

4. transpiler.py — AST to C 語法轉換
完成方式：chatgpt建議節點轉換方法

參考來源：參考 C 語法風格，但未直接複製

說明：

使用 visit() 走訪 AST 節點並產出 C 語法

包含主程式結構 #include <stdio.h> 和 printf

5. emitter.py — 輸出轉譯檔案
完成方式：完全原創

參考來源：無

說明：

將產生的 C 程式碼寫入指定檔案

簡單封裝 open() 與 write() 函數

6. examples/hello.py — 測試用程式碼
完成方式：原創

內容：

python
複製
編輯
print(1 + 2 * 3)
用途：測試轉譯流程是否正確，是否考慮運算優先順序
 7. output/hello.c — C 語言輸出結果
完成方式：轉譯器自動生成

說明：

由 transpiler.py 產出

可用 GCC 編譯測試輸出是否為 7



