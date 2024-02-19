# Wiki-Generate-Text

## 研究動機

最近，基於 Transformer 的生成式 AI 模型如 GPT、LLaMA、PaLM 等，因其文字接龍式的文本生成能力而備受關注。受此啟發，我決定創建「Wiki-Generate-Text」這個專案，目的是嘗試利用純粹的 Python 代碼、資料處理技術和演算法，不依賴任何神經網路套件或元素，手工打造一個簡易的文本生成模型。這個專案的核心是完全基於我自己撰寫的代碼，不使用任何外來的神經網路、AI 或機器學習相關套件，從而探索文本生成的另一種可能性。

## 專案描述

Wiki-Generate-Text 是一個使用維基百科數據訓練的文本生成器。本專案通過分析大量維基百科文本，建立機率模型，以此來預測和生成文本。用戶可輸入一個或多個字符作為開始，系統將基於這些字符，利用訓練好的機率集生成一段連貫的文本。

## 訓練資料來源

訓練資料來自於 [brightmart/nlp_chinese_corpus](https://github.com/brightmart/nlp_chinese_corpus) 提供的中文語料庫。

## 安裝指南

1. 克隆倉庫到本地：
   ```
   git clone https://github.com/JustinHsu1019/Wiki-Generate-Text.git
   ```
2. 確保安裝了Python及所需的庫：
   - `tqdm`：一個快速、擴展性強的 Python 進度條工具，用於在長時間運行的操作中提供視覺反饋。
   - `opencc-python-reimplemented`：一個簡繁轉換工具，用於將簡體中文文本轉換為繁體中文。
   - `tkinter`：Python 的標準 GUI 工具包，用於建立和運行 GUI 應用程序。

## 使用說明

專案包含三個主要的Python腳本：

1. `Process.py` - 處理和準備數據
2. `Training.py` - 訓練機率模型
3. `Generate.py` - 生成文本和 GUI 介面

### 數據處理

首先運行 `Process.py` 腳本來處理原始數據。

```python
python Process.py
```

### 模型訓練

接著運行 `Training.py` 腳本來訓練機率模型。

```python
python Training.py
```

### 文本生成

最後，運行 `Generate.py` 來啟動文本生成器的GUI界面。

```python
python Generate.py
```

在 GUI 界面中，輸入開始的字符，然後點擊 “生成文本” 按鈕來生成文本。

## 貢獻指南

我們歡迎任何形式的貢獻，包括但不限於新功能的建議、代碼改進、文檔更新等。請遵循以下步驟：

1. Fork該倉庫
2. 創建您的功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 提交Pull Request

## 聯繫方式

如有任何疑問或建議，請通過以下方式與我們聯繫：

- Email: [justin.hsu.1019@gmail.com](mailto:justin.hsu.1019@gmail.com)
- GitHub Issue: [提交 Issue](https://github.com/JustinHsu1019/Wiki-Generate-Text/issues)
