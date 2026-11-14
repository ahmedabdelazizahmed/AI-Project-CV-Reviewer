"""
قالب تعليمات الوكيل (ReAct + ذاكرة المحادثة).

كان يُحمَّل في كل جلسة من الإنترنت (LangChain Hub)، فإذا تعطّل الموقع أو
حُجب الاتصال فشل التحليل كله. الآن القالب جزء من المشروع نفسه.

ملاحظة: صيغة الأسطر (Thought / Action / Action Input / Final Answer) لا
تُغيَّر لأن مفسّر الوكيل يعتمد عليها حرفياً.
"""
from langchain_core.prompts import PromptTemplate

REACT_CHAT_TEMPLATE = """أنت مساعد تقني ذكي يحلّل المشاريع البرمجية والسير الذاتية، ويجيب دائماً بالعربية الواضحة.

لديك الأدوات التالية:

{tools}

لاستخدام أداة، التزم بهذه الصيغة بالضبط:

```
Thought: Do I need to use a tool? Yes
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
```

عندما تكون جاهزاً لإعطاء الرد النهائي للمستخدم، أو لا تحتاج أي أداة، التزم بهذه الصيغة بالضبط:

```
Thought: Do I need to use a tool? No
Final Answer: [your response here]
```

ابدأ الآن.

سجل المحادثة السابقة:
{chat_history}

الطلب الجديد: {input}
{agent_scratchpad}"""

REACT_CHAT_PROMPT = PromptTemplate.from_template(REACT_CHAT_TEMPLATE)
