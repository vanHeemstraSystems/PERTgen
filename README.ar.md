# بيرتجن

> كود بايثون لإنشاء رسم بياني PERT ومخطط جانت مع إعطاء جدول المهام.

استنادًا إلى "كيفية إنشاء تطبيق قارورة كبيرة باستخدام مخططات قارورة وFlask-SQLAlchemy" في<https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy>

استنادا إلى "Flask SQLAlchemy" في<https://github.com/vanHeemstraSystems/flask-sqlalchemy/>

بناءً على "نمط المصنع" في<https://github.com/vanHeemstraSystems/factory-pattern>

استنادًا إلى "الرسوم التخطيطية لعلاقة الكيانات المستندة إلى النص مع Mermaid.js" في<https://newdevsguide.com/2023/04/08/creating-erds-with-mermaid/>

بناء على "FlowBite" في<https://github.com/themesberg/flowbite>

افتح عنوان URL هذا باستخدام`https://github.dev/`بدلاً من`https://github.dev/`لاستخدام IDE المستند إلى الويب لـ Visual Studio Code.

قم بتشغيل هذا التطبيق على النحو التالي:

1) أدخل`flask_app`دليل:`$ cd flask_app`2) في حالة عدم وجودها، قم بإنشاء بيئة افتراضية داخل`flask_app`دليل:`$ python3 -m venv .venv`(ماك:`$ virtualenv .venv`)

وفي حالة ما يلي، اتبع نصيحتها:

لم يتم إنشاء البيئة الافتراضية بنجاح بسبب عدم إنشاء متأكد
متاح.

على أنظمة Debian/Ubuntu، تحتاج إلى تثبيت python3-venv
الحزمة باستخدام الأمر التالي.

    sudo apt-get update
    sudo apt install python3.10-venv

قد تحتاج إلى استخدام Sudo مع هذا الأمر.  بعد تثبيت python3-venv
الحزمة، أعد إنشاء بيئتك الافتراضية.

على نظام التشغيل MacOS، انظر<https://sourabhbajaj.com/mac-setup/Python/virtualenv.html>

3) ابدأ البيئة الافتراضية وأدخل:`. .venv/bin/activate`(ماك:`source .venv/bin/activate`)
4) تشغيل`$ pip install -r requirements.txt`5) تشغيل:`$ npm install`6) قم بتعيين تطبيق Flask على دليل التطبيق:`(.venv) $ export FLASK_APP=app`7) اضبط بيئة Flask على True من أجل التطوير:`(.venv) $ export FLASK_DEBUG=True`8) قم بتعيين URI لقاعدة بيانات SQLAlchemy:`(.venv) $ export SQLALCHEMY_DATABASE_URI=...`، الافتراضي هو`sqlite:///app.db`9) تعيين تعديلات مسار SQLAlchemy:`(.venv) $ export SQLALCHEMY_TRACK_MODIFICATIONS=True`10) تعيين المفتاح السري:`(.venv) $ export SECRET_KEY=********`11) قم بتشغيل تطبيق القارورة:`(.venv) $ flask run`12) افتح واجهة الويب كما هو مطلوب
13) الاستخدام`CTRL+c`للخروج من خادم الويب.
14) بدلاً من ذلك، قم بتشغيل واجهة سطر أوامر القارورة:`(.venv) $ flask shell`15) تنفيذ أي أوامر قارورة: >>>
16) الاستخدام`exit()`للخروج من واجهة سطر الأوامر.

## متطلبات

يستخدم هذا المشروع python3، ويجب تثبيت المكتبات التالية لتشغيله:

-   [نتورككس](https://networkx.github.io/)- يستخدم لعمل الرسم البياني PERT.
-   [ماتبلوتليب](https://matplotlib.org/)- يستخدم لإنشاء مخطط جانت، بالإضافة إلى إظهار وحفظ كل من الرسم البياني PERT ومخطط جانت.

## إدخال البيانات

The task data must be given in a CSV file, in the format of the sample ones given (`tasks.csv`و`tasks2.csv`)،
أي أن كل صف يبدأ من الصف الثاني يجب أن يكون له مهمة ومدتها وجميع تبعياتها مفصولة بمسافات

## اختبره

يمكن اختبار المشروع باستخدام واجهة المستخدم الرسومية tkinter البسيطة عن طريق التشغيل`gui.py`مع مترجم python3، على الرغم من أن كل التعليمات البرمجية المهمة موجودة`pert.py`والتي يمكن تشغيلها أيضًا بعد تحديد الملف الذي سيتم تحميله.
