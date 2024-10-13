# PERT基因

用於在給定任務計劃的情況下產生 PERT 圖和甘特圖的 Python 程式碼。

## 要求

此專案使用python3，必須安裝以下程式庫才能運作：

-   [網路X](https://networkx.github.io/)- 用於製作 PERT 圖。
-   [Matplotlib](https://matplotlib.org/)- 用於製作甘特圖，以及顯示和保存 PERT 圖和甘特圖。

## 資料輸入

任務資料必須以 CSV 檔案的形式提供，格式為給定的範例資料 (`tasks.csv`和`tasks2.csv`),
即從第二行開始的每一行都應該有一個任務、其持續時間及其所有依賴項，並用空格分隔

## 測試一下

可以透過執行簡單的 tkinter GUI 來測試該項目`gui.py`使用 python3 解釋器，儘管所有重要的程式碼都在`pert.py`也可以在指定要載入的檔案後運行。
