# بيرتجن

Python code to generate a PERT graph and Gantt chart given a task schedule.

## متطلبات

يستخدم هذا المشروع python3، ويجب تثبيت المكتبات التالية لتشغيله:

-   [نتورككس](https://networkx.github.io/)- يستخدم لعمل الرسم البياني PERT.
-   [ماتبلوتليب](https://matplotlib.org/) - Used to make the Gantt chart, as well as show and save both the PERT graph and Gantt chart.

## إدخال البيانات

يجب تقديم بيانات المهمة في ملف CSV، بتنسيق العينات المقدمة (`tasks.csv`و`tasks2.csv`)،
أي أن كل صف يبدأ من الصف الثاني يجب أن يكون له مهمة ومدتها وجميع تبعياتها مفصولة بمسافات

## اختبره

يمكن اختبار المشروع باستخدام واجهة المستخدم الرسومية tkinter البسيطة عن طريق التشغيل`gui.py`مع مترجم python3، على الرغم من أن كل التعليمات البرمجية المهمة موجودة`pert.py`والتي يمكن تشغيلها أيضًا بعد تحديد الملف الذي سيتم تحميله.
