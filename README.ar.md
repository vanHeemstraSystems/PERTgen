# بيرتجن

كود بايثون لإنشاء رسم بياني PERT ومخطط جانت مع إعطاء جدول المهام.

## متطلبات

يستخدم هذا المشروع python3، ويجب تثبيت المكتبات التالية لتشغيله:

-   [نتورككس](https://networkx.github.io/) - Used to make the PERT graph.
-   [ماتبلوتليب](https://matplotlib.org/)- يستخدم لإنشاء مخطط جانت، بالإضافة إلى إظهار وحفظ كل من الرسم البياني PERT ومخطط جانت.

## إدخال البيانات

يجب تقديم بيانات المهمة في ملف CSV، بتنسيق العينات المقدمة (`tasks.csv` and `tasks2.csv`),
i.e. each row starting from the second one should have a task, its duration and all its dependencies seperated by spaces

## اختبره

The project can be tested with the simple tkinter GUI by running `gui.py`مع مترجم python3، على الرغم من أن كل التعليمات البرمجية المهمة موجودة`pert.py`والتي يمكن تشغيلها أيضًا بعد تحديد الملف الذي سيتم تحميله.
