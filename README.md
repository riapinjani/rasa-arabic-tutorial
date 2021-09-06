# rasa-arabic-tutorial

Medium Draft

Build your chatbot in Arabic with Rasa: A Complete Guide

1. Short intro about chatbots and need for multilingual agents

2. Set up 
Suggest/Include resource for creating a python virtual env
```
pip3 install rasa==2.7.1
rasa init
```
StanzaTokenizer - download stanza for "ar" 
Elaborate on pre trained language models
```
pip install "rasa_nlu_examples[stanza] @ git+https://github.com/RasaHQ/rasa-nlu-examples.git"
```
requirement.py 
```python
import stanza
stanza.download('ar', processors={'ner': 'AQMAR'})
nlp = stanza.Pipeline('ar', processors={'ner': 'AQMAR'})
```
```
python requirements.py
```
3. Describe RASA NLU; Specify intents & entities
```yml
version: "2.0"
nlu:
- intent: greet
examples: |
- أهلا
- مهلا
- صباح الخير
- مساء الخير
- السلام عليكم عربي
- تحية

- intent: goodbye
examples: |
- يجب أن أذهب لاحقًا
- وداعا لاحقا
- أراك لاحقا
- في وقت لاحق
- وداعا
- مع السلامة

- intent: location
examples: |
- اين موقعك
- اين فرعك
- اين العنوان
- [دبي](LOC) هل انت موجود في
- [الشارقة](LOC) ل انت موجود في
- [الهند](LOC) ل انت موجود في
- [لندن](LOC) هل انت موجود في

- intent: timings
examples: |
- متى تفتحون
- متى تغلق
- توقيتك
- ساعات عملك
- في أي وقت يمكن أن آتي
- هل تفتح 24 ساعة في اليوم
```
4. Describe NLG; Specify responses
```yml
responses:
utter_greet:
- text: كيف حالك اليوم؟ .DScale.io يا هذا هو
utter_goodbye:
- text: وداعا أتمنى لك يوما سعيدا
utter_location:
- text: يمكنك أن تجدنا في إعمار سكوير دبي
utter_timings:
- text: نحن منفتحون من الأحد إلى الخميس ، من الساعة 9:00 إلى الساعة 6:00 مساءً
```
5. Specify rules
```yml
version: "2.0"
rules:
- rule: Say goodbye anytime the user says goodbye
steps:
- intent: goodbye
- action: utter_goodbye

- rule: Greet anytime the user says hi
steps:
- intent: greet
- action: utter_greet

- rule: Utter location when user asks for location
steps:
- intent: location
- action: utter_location

- rule: Utter timings when user asks for timings
steps:
- intent: timings
- action: utter_timings
```
6. Configuration
[Insert github link for config.yml]

  Elaborate on pipeline used

7. Train your model
```
rasa train
```
8.Interact with your bot using Rasa X
```
rasa x
```
9.Include example image

![rasax](rasax.png)

10. Ending Note

