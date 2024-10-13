# PERT基因

> 用於在給定任務計劃的情況下產生 PERT 圖和甘特圖的 Python 程式碼。

基於“如何使用 Flask 藍圖和 Flask-SQLAlchemy 建立大型 Flask 應用程式”，位於<https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy>

基於“Flask SQLAlchemy”，位於<https://github.com/vanHeemstraSystems/flask-sqlalchemy/>

基於“工廠模式”<https://github.com/vanHeemstraSystems/factory-pattern>

基於“基於文字的實體關係圖與 Mermaid.js”，位於<https://newdevsguide.com/2023/04/08/creating-erds-with-mermaid/>

基於“FlowBite”<https://github.com/themesberg/flowbite>

開啟此網址`https://github.dev/`而不是`https://github.dev/`使用基於 Web 的 Visual Studio Code IDE。

按如下方式運行該應用程式：

1) 輸入`flask_app`目錄：`$ cd flask_app`2）如果不存在，則在內部建立一個虛擬環境`flask_app` directory: `$ python3 -m venv .venv`（蘋果系統：`$ virtualenv .venv`)

若出現以下情況，請遵循其建議：

虛擬環境沒有創建成功，因為ensurepip沒有
可用的。

在 Debian/Ubuntu 系統上，需要安裝 python3-venv
使用以下命令進行打包。

    sudo apt-get update
    sudo apt install python3.10-venv

您可能需要將 sudo 與該命令一起使用。  安裝 python3-venv 後
包，重新建立您的虛擬環境。

在 macOS 上請參閱<https://sourabhbajaj.com/mac-setup/Python/virtualenv.html>

3）啟動虛擬環境，輸入：`. .venv/bin/activate`（蘋果系統：`source .venv/bin/activate`）
4）運行`$ pip install -r requirements.txt`5）運行：`$ npm install`6）將Flask App設定到app目錄：`(.venv) $ export FLASK_APP=app`7）將Flask環境設定為True進行開發：`(.venv) $ export FLASK_DEBUG=True`8) 設定 SQLAlchemy 資料庫 URI：`(.venv) $ export SQLALCHEMY_DATABASE_URI=...`，預設為`sqlite:///app.db`9）設定SQLAlchemy軌道修改：`(.venv) $ export SQLALCHEMY_TRACK_MODIFICATIONS=True`10) 設定密鑰：`(.venv) $ export SECRET_KEY=********`11）運行燒瓶應用程式：`(.venv) $ flask run`12）根據提示開啟Web介面
13) 使用`CTRL+c`退出網路伺服器。
14) 或運行flask命令列介面：`(.venv) $ flask shell`15) 執行任意 Flask 指令：>>>
16) 使用`exit()`退出命令列介面。

## 要求

此專案使用python3，必須安裝以下程式庫才能運作：

-   [網路X](https://networkx.github.io/)- 用於製作 PERT 圖。
-   [Matplotlib](https://matplotlib.org/) - Used to make the Gantt chart, as well as show and save both the PERT graph and Gantt chart.

## 資料輸入

任務資料必須以 CSV 檔案的形式提供，格式為給定的範例資料 (`tasks.csv`和`tasks2.csv`),
即從第二行開始的每一行都應該有一個任務、其持續時間及其所有依賴項，並用空格分隔

## 測試一下

可以透過執行簡單的 tkinter GUI 來測試該項目`gui.py`使用 python3 解釋器，儘管所有重要的程式碼都在`pert.py`也可以在指定要載入的檔案後運行。
