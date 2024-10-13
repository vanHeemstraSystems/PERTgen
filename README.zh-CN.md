# PERT基因

用于在给定任务计划的情况下生成 PERT 图和甘特图的 Python 代码。

## 要求

This project uses python3, and the following libraries must be installed to run it:

-   [网络X](https://networkx.github.io/)- 用于制作 PERT 图。
-   [Matplotlib](https://matplotlib.org/)- 用于制作甘特图，以及显示和保存 PERT 图和甘特图。

## 数据输入

任务数据必须以 CSV 文件的形式提供，格式为给定的示例数据 (`tasks.csv` and `tasks2.csv`),
即从第二行开始的每一行都应该有一个任务、其持续时间及其所有依赖项，并用空格分隔

## 测试一下

The project can be tested with the simple tkinter GUI by running `gui.py`使用 python3 解释器，尽管所有重要的代码都在`pert.py`也可以在指定要加载的文件后运行。
