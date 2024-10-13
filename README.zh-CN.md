# PERT基因

用于在给定任务计划的情况下生成 PERT 图和甘特图的 Python 代码。

## 要求

该项目使用python3，必须安装以下库才能运行：

-   [网络X](https://networkx.github.io/) - Used to make the PERT graph.
-   [Matplotlib](https://matplotlib.org/) - Used to make the Gantt chart, as well as show and save both the PERT graph and Gantt chart.

## 数据输入

任务数据必须以 CSV 文件的形式提供，格式为给定的示例数据 (`tasks.csv`和`tasks2.csv`),
即从第二行开始的每一行都应该有一个任务、其持续时间及其所有依赖项，并用空格分隔

## 测试一下

可以通过运行简单的 tkinter GUI 来测试该项目`gui.py`使用 python3 解释器，尽管所有重要的代码都在`pert.py`也可以在指定要加载的文件后运行。
