from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

model_name = "llama3.2:latest"
llm=ChatOllama(model=model_name)
parser=StrOutputParser()

article = """The Mysuru Dasara is a 10-day festival celebrated in Karnataka.
The Mysuru Palace is lit with nearly 100,000 bulbs, and the Jamboo Savari procession
on the last day features decorated elephants and  the iconic antique gold ambari the elephant carries."""

summary_chain=PromptTemplate.from_template("Summarize: {text}") | llm |parser 
sentiment_chain=PromptTemplate.from_template("Identify sentiment in: {text}") | llm |parser
keywords_chain=PromptTemplate.from_template("Identify Keywords in: {text}") | llm |parser



analysis_chain = RunnableParallel({
    "original_article": RunnablePassthrough(),
    "analysis": RunnableParallel({
        "summary": summary_chain,
        "sentiment": sentiment_chain,
        "keywords": keywords_chain
    })
})

def format_report(results):
    article_text = results["original_article"]["text"]
    analysis = results["analysis"]

    return f"""
========== ARTICLE ANALYSIS ==========

ORIGINAL ARTICLE:
{article_text}

SUMMARY:
{analysis["summary"]}

SENTIMENT:
{analysis["sentiment"]}

KEYWORDS:
{analysis["keywords"]}

======================================
"""

results = analysis_chain.invoke({"text": article})
print(format_report(results))