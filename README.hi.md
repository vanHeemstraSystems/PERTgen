# PERTGEN

> PERT ग्राफ़ और गैंट चार्ट उत्पन्न करने के लिए पायथन कोड को एक कार्य शेड्यूल दिया गया है।

"फ्लास्क ब्लूप्रिंट और फ्लास्क-SQLAlchemy के साथ एक बड़े फ्लास्क अनुप्रयोग की संरचना कैसे करें" पर आधारित<https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy>

"फ्लास्क SQLAlchemy" पर आधारित<https://github.com/vanHeemstraSystems/flask-sqlalchemy/>

"फ़ैक्टरी पैटर्न" पर आधारित<https://github.com/vanHeemstraSystems/factory-pattern>

"Mermaid.js के साथ पाठ-आधारित इकाई संबंध आरेख" पर आधारित<https://newdevsguide.com/2023/04/08/creating-erds-with-mermaid/>

"फ्लोबाइट" पर आधारित<https://github.com/themesberg/flowbite>

इस URL को इसके साथ खोलें`https://github.dev/`के बजाय`https://github.dev/`विज़ुअल स्टूडियो कोड वेब-आधारित आईडीई का उपयोग करने के लिए।

इस एप्लिकेशन को इस प्रकार चलाएँ:

1) दर्ज करें`flask_app`निर्देशिका:`$ cd flask_app`2) यदि अस्तित्व में नहीं है, तो अंदर एक आभासी वातावरण बनाएं`flask_app`निर्देशिका:`$ python3 -m venv .venv`(मैक ओएस:`$ virtualenv .venv`)

निम्नलिखित के मामले में, इसकी सलाह का पालन करें:

वर्चुअल वातावरण सफलतापूर्वक नहीं बनाया गया क्योंकि एनिश्चेपिप नहीं है
उपलब्ध।

डेबियन/उबंटू सिस्टम पर, आपको Python3-venv इंस्टॉल करना होगा
निम्नलिखित कमांड का उपयोग करके पैकेज।

    sudo apt-get update
    sudo apt install python3.10-venv

आपको उस कमांड के साथ sudo का उपयोग करने की आवश्यकता हो सकती है।  Python3-venv स्थापित करने के बाद
पैकेज, अपने आभासी वातावरण को फिर से बनाएं।

MacOS पर देखें<https://sourabhbajaj.com/mac-setup/Python/virtualenv.html>

3) आभासी वातावरण प्रारंभ करें और दर्ज करें:`. .venv/bin/activate`(मैक ओएस:`source .venv/bin/activate`)
4) भागो`$ pip install -r requirements.txt`5) भागो:`$ npm install`6) फ्लास्क ऐप को ऐप डायरेक्टरी पर सेट करें:`(.venv) $ export FLASK_APP=app`7) विकास के लिए फ्लास्क पर्यावरण को सही पर सेट करें:`(.venv) $ export FLASK_DEBUG=True`8) SQLAlchemy डेटाबेस URI सेट करें:`(.venv) $ export SQLALCHEMY_DATABASE_URI=...`, डिफ़ॉल्ट है`sqlite:///app.db`9) SQLAlchemy ट्रैक संशोधन सेट करें:`(.venv) $ export SQLALCHEMY_TRACK_MODIFICATIONS=True`10) गुप्त कुंजी सेट करें:`(.venv) $ export SECRET_KEY=********`11) फ्लास्क ऐप चलाएँ:`(.venv) $ flask run`12) संकेतानुसार वेब इंटरफ़ेस खोलें
13) प्रयोग करें`CTRL+c`वेब सर्वर से बाहर निकलने के लिए.
14) वैकल्पिक रूप से फ्लास्क कमांड लाइन इंटरफ़ेस चलाएँ:`(.venv) $ flask shell`15) किसी भी फ्लास्क कमांड को निष्पादित करें: >>>
16) उपयोग करें`exit()`कमांड लाइन इंटरफ़ेस से बाहर निकलने के लिए।

## आवश्यकताएं

यह प्रोजेक्ट Python3 का उपयोग करता है, और इसे चलाने के लिए निम्नलिखित लाइब्रेरी स्थापित होनी चाहिए:

-   [नेटवर्कएक्स](https://networkx.github.io/)- PERT ग्राफ़ बनाने के लिए उपयोग किया जाता है।
-   [matplotlib](https://matplotlib.org/)- गैंट चार्ट बनाने के साथ-साथ पीईआरटी ग्राफ़ और गैंट चार्ट दोनों को दिखाने और सहेजने के लिए उपयोग किया जाता है।

## डेटा इनपुट

कार्य डेटा सीएसवी फ़ाइल में दिए गए नमूना प्रारूप में दिया जाना चाहिए (`tasks.csv` and `tasks2.csv`),
यानी दूसरी से शुरू होने वाली प्रत्येक पंक्ति में एक कार्य, उसकी अवधि और उसकी सभी निर्भरताएँ रिक्त स्थान से अलग होनी चाहिए

## इसका परीक्षण करें

प्रोजेक्ट को सरल टिंकर जीयूआई के साथ चलाकर परीक्षण किया जा सकता है`gui.py`Python3 दुभाषिया के साथ, हालाँकि सभी महत्वपूर्ण कोड मौजूद हैं`pert.py`जिसे यह निर्दिष्ट करने के बाद भी चलाया जा सकता है कि कौन सी फ़ाइल लोड की जानी है।
