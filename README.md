#### rasa-arabic-tutorial

## **Build your chatbot in Arabic with Rasa: A Complete Guide**

Chatbots are computer programs build to simulate conversations with human users. This can be achived through NLP, a branch of Artificial Intellegence that helps computers understand human language. As chatbots gain popularity globally, there is increasing need to build multilingual agents that can cater to regions with linguistic diversity. This is likely to have a huge impact on customer engagement and satisfaction, and can prove to be a great asset for any organization. 


### Set up
 
I would highly recommend you to create a python virtual environment for your project before getting started. You can do so by following a few simple steps listed below:

Install the virtualenv package using pip

```
pip install virtualenv
```

Next, specify the local directory where you would like to create your virtual environment. I used my project directory 'rasa-arabic'.

```
virtualenv rasa-arabic
```

Lastly, activate the virtual environment

Mac OS / Linux

```
source rasa-arabic/bin/activate
```

Windows

```
rasa-arabic\Scripts\activate
```

Once your virtual environment is activated, install Rasa using pip 
```
pip3 install rasa
```

Create a project using the following command:
```
rasa init
```

These are the files created for the initial project structure;

- actions: code for custom actions

- data: training data for Rasa NLU & Core

- models: where your model is stored

- config.yml: configuration for Rasa NLU & Core

- credentials.yml: credentials for the voice and/or chat platforms the bot is using

- domain.yml: all intents, entities, slots and action your bot should know about are defined here

- endpoints.yml: endpoints the bot can use for connecting to actions or databases etc.

To build a bot in Arabic, it's a good idea to use a pre-trained language model. We are going to make use of Stanza; a Python NLP Package that supports many languages including Arabic. Once the project has been initiated, run the below command so that you are able to use stanza in your Rasa NLU pipeline. You can view performance metrics for Stanza's pre-trained model here.

```
pip install "rasa_nlu_examples[stanza] @ git+https://github.com/RasaHQ/rasa-nlu-examples.git"
```
Within your current project directory, create a new python file named download_stanza.py and paste the below code.

```python
import stanza
stanza.download('ar', processors={'ner': 'AQMAR'})
nlp = stanza.Pipeline('ar', processors={'ner': 'AQMAR'})
```
Run download_stanza.py to download stanza for arabic. 
```
python download_stanza.py
```
### RASA NLU; Specify intents & entities

You are now ready to add training data for your Arabic Language Bot!

Our first step is to specify user utterances in data/nlu.yml. User utterances are classified unter distinct intents.
For the intent 'greet', i have specified multiple ways in which one may greet in arabic. Generally speaking, higher number of training examples generally lead to better performance. 

We can also define entities in our data/nlu.yml file. Entities are essentially defined as structured information inside a user's message. Common examples include names, dates, money etc. Here, i have defined the 'LOC' entity which is a part of Stanza’s pretrained NER model for Arabic.


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
### RASA CORE; Specify responses

Specify responses for each of the intents defined above in domain.yml.

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
### Specify rules

Once you have specified intents, entities and responses, you must define the conversation pattern the bot should follow. This can be done using stories or rules. Stories are generally used for more complex, multi-turn conversations. For our example, we will stick to rules. For writing rules, you should start with the intent that starts the conversation and then specify the action that the bot should respond with. These can be defined in data/rules.yml as:


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
### Model Configuration

The next step is to specify the Pipeline Components that your NLU model would use, as well as the Policies your core model would use to predict the next action. You can specify the pipeline and policies you would like to use in config.yml.

```
language: ar

pipeline:
- name: rasa_nlu_examples.tokenizers.StanzaTokenizer
  lang: "ar"
  cache_dir: ".../stanza_resources"
- name: LexicalSyntacticFeaturizer
- name: CountVectorsFeaturizer
- name: CountVectorsFeaturizer
  analyzer: char_wb
  min_ngram: 1
  max_ngram: 4
- name: DIETClassifier
  epochs: 100
  
policies:
- name: MemoizationPolicy
- name: RulePolicy
```


### Train your model

To train your rasa model, you just need to run:
```
rasa train
```
### Interact with your bot using Rasa X

To interact with your bot, just run:
```
rasa x
```
![rasax](rasax.png)

You are done! The chatbot is ready to be deployed and integrated with any number of channels including Facebook, Slack or your own website. You can find instructions to do so here. Additionally, you can connect Rasa to an external database for storing conversation history. Details for the configuration can be found here.

