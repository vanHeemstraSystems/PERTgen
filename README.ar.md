# بيرتجن

كود بايثون لإنشاء رسم بياني PERT ومخطط جانت مع إعطاء جدول المهام.

## متطلبات

This project uses python3, and the following libraries must be installed to run it:

-   [نتورككس](https://networkx.github.io/)- يستخدم لعمل الرسم البياني PERT.
-   [ماتبلوتليب](https://matplotlib.org/)- يستخدم لإنشاء مخطط جانت، بالإضافة إلى إظهار وحفظ كل من الرسم البياني PERT ومخطط جانت.

## إدخال البيانات

The task data must be given in a CSV file, in the format of the sample ones given (`tasks.csv`و`tasks2.csv`)،
أي أن كل صف يبدأ من الصف الثاني يجب أن يكون له مهمة ومدتها وجميع تبعياتها مفصولة بمسافات

## اختبره

يمكن اختبار المشروع باستخدام واجهة المستخدم الرسومية tkinter البسيطة عن طريق التشغيل`gui.py`مع مترجم python3، على الرغم من أن كل التعليمات البرمجية المهمة موجودة`pert.py`والتي يمكن تشغيلها أيضًا بعد تحديد الملف الذي سيتم تحميله.
