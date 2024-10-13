# PERT基因

> 用于在给定任务计划的情况下生成 PERT 图和甘特图的 Python 代码。

基于“如何使用 Flask 蓝图和 Flask-SQLAlchemy 构建大型 Flask 应用程序”，位于<https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy>

基于“Flask SQLAlchemy”，位于<https://github.com/vanHeemstraSystems/flask-sqlalchemy/>

基于“工厂模式”<https://github.com/vanHeemstraSystems/factory-pattern>

基于“基于文本的实体关系图与 Mermaid.js”，位于<https://newdevsguide.com/2023/04/08/creating-erds-with-mermaid/>

基于“FlowBite”<https://github.com/themesberg/flowbite>

打开此网址`https://github.dev/`而不是`https://github.dev/`使用基于 Web 的 Visual Studio Code IDE。

按如下方式运行该应用程序：

1) 输入`flask_app`目录：`$ cd flask_app`2）如果不存在，则在内部创建一个虚拟环境`flask_app`目录：`$ python3 -m venv .venv`（苹果系统：`$ virtualenv .venv`)

如果出现以下情况，请遵循其建议：

虚拟环境没有创建成功，因为ensurepip没有
可用的。

在 Debian/Ubuntu 系统上，需要安装 python3-venv
使用以下命令进行打包。

    sudo apt-get update
    sudo apt install python3.10-venv

您可能需要将 sudo 与该命令一起使用。  安装 python3-venv 后
包，重新创建您的虚拟环境。

On macOS see <https://sourabhbajaj.com/mac-setup/Python/virtualenv.html>

3）启动虚拟环境，输入：`. .venv/bin/activate`（苹果系统：`source .venv/bin/activate`）
4）运行`$ pip install -r requirements.txt`5）运行：`$ npm install`6）将Flask App设置到app目录：`(.venv) $ export FLASK_APP=app`7）将Flask环境设置为True进行开发：`(.venv) $ export FLASK_DEBUG=True`8) 设置 SQLAlchemy 数据库 URI：`(.venv) $ export SQLALCHEMY_DATABASE_URI=...`，默认为`sqlite:///app.db`9）设置SQLAlchemy轨道修改：`(.venv) $ export SQLALCHEMY_TRACK_MODIFICATIONS=True`10) 设置密钥：`(.venv) $ export SECRET_KEY=********`11）运行烧瓶应用程序：`(.venv) $ flask run`12）根据提示打开Web界面
13) 使用`CTRL+c`退出网络服务器。
14) 或者运行flask命令行界面：`(.venv) $ flask shell`15) 执行任何 Flask 命令：>>>
16) 使用`exit()`退出命令行界面。

## 要求

该项目使用python3，必须安装以下库才能运行：

-   [网络X](https://networkx.github.io/)- 用于制作 PERT 图。
-   [Matplotlib](https://matplotlib.org/)- 用于制作甘特图，以及显示和保存 PERT 图和甘特图。

## 数据输入

任务数据必须以 CSV 文件的形式提供，格式为给定的示例数据 (`tasks.csv`和`tasks2.csv`),
即从第二行开始的每一行都应该有一个任务、其持续时间及其所有依赖项，并用空格分隔

## 测试一下

可以通过运行简单的 tkinter GUI 来测试该项目`gui.py`使用 python3 解释器，尽管所有重要的代码都在`pert.py`也可以在指定要加载的文件后运行。
