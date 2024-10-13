# PERTGEN

PERT ग्राफ़ और गैंट चार्ट उत्पन्न करने के लिए पायथन कोड को एक कार्य शेड्यूल दिया गया है।

## आवश्यकताएं

यह प्रोजेक्ट Python3 का उपयोग करता है, और इसे चलाने के लिए निम्नलिखित लाइब्रेरी स्थापित होनी चाहिए:

-   [नेटवर्कएक्स](https://networkx.github.io/)- PERT ग्राफ़ बनाने के लिए उपयोग किया जाता है।
-   [matplotlib](https://matplotlib.org/) - Used to make the Gantt chart, as well as show and save both the PERT graph and Gantt chart.

## डेटा इनपुट

कार्य डेटा सीएसवी फ़ाइल में दिए गए नमूना प्रारूप में दिया जाना चाहिए (`tasks.csv`और`tasks2.csv`),
i.e. each row starting from the second one should have a task, its duration and all its dependencies seperated by spaces

## इसका परीक्षण करें

प्रोजेक्ट को सरल टिंकर जीयूआई के साथ चलाकर परीक्षण किया जा सकता है`gui.py`Python3 दुभाषिया के साथ, हालाँकि सभी महत्वपूर्ण कोड मौजूद हैं`pert.py`जिसे यह निर्दिष्ट करने के बाद भी चलाया जा सकता है कि कौन सी फ़ाइल लोड की जानी है।
