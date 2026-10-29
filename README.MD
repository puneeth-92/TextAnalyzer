TextAnalyzer

A simple AI-powered text analysis application built using Python, LangChain, and Ollama. It analyzes an article to generate a summary, identify its sentiment, and extract important keywords using parallel execution.

Features

- Text Summarization: Generates a concise summary of the input article.
- Sentiment Analysis: Identifies the sentiment expressed in the article.
- Keyword Extraction: Extracts important keywords from the text.
- Parallel Execution: Uses LangChain’s RunnableParallel to execute the three analysis chains concurrently.
- Local LLM: Uses Llama 3.2 through Ollama to run inference locally.

Tech Stack

- Python
- LangChain
- Ollama
- Llama 3.2

How It Works

The application uses LangChain Expression Language (LCEL) to compose multiple processing steps into reusable chains.

1. Input: An article is provided as a string.
2. Prompt Templates: Separate prompts are created for summarization, sentiment analysis, and keyword extraction.
3. LLM Processing: Each prompt is passed to the Llama 3.2 model through ChatOllama.
4. Output Parsing: StrOutputParser converts model responses into strings.
5. Parallel Execution: RunnableParallel runs the three analysis chains concurrently.
6. Report Generation: The results are combined into a formatted report alongside the original article.

Architecture

                  Input Article
                        |
                 RunnableParallel
                  /      |      \
                 /       |       \
            Summary   Sentiment   Keywords
              Chain     Chain      Chain
                 \       |        /
                  \      |       /
                   Results Dictionary
                           |
                    Format Report
                           |
                     Final Output

Prerequisites

- Python 3.10 or later recommended.
- Ollama installed and running.
- The llama3.2:latest model available locally.

Installation

1. Clone the repository

git clone https://github.com/puneeth-92/TextAnalyzer.git
cd TextAnalyzer

2. Create a virtual environment

python3 -m venv venv

Activate it on macOS or Linux:

source venv/bin/activate

3. Install dependencies

pip install langchain langchain-core langchain-ollama

4. Download the model

ollama pull llama3.2

Ensure Ollama is running before executing the application.

Usage

Run the application:

python main.py

The program analyzes the predefined article about Mysuru Dasara and prints a report containing:

- Original article
- Summary
- Sentiment
- Keywords

Key LangChain Concepts

Component Purpose
ChatOllama Connects LangChain to the locally running Llama 3.2 model.
PromptTemplate Defines prompts with variables that can be filled dynamically.
StrOutputParser Converts model message outputs into strings.
RunnableParallel Executes multiple independent Runnable branches concurrently.
RunnablePassthrough Preserves the original input without modifying it.
LCEL (|) Composes prompts, models, and output parsers into processing pipelines.

Example Output

========== ARTICLE ANALYSIS ==========
ORIGINAL ARTICLE:
The Mysuru Dasara is a 10-day festival celebrated in Karnataka...
SUMMARY:
[Generated summary]
SENTIMENT:
[Generated sentiment]
KEYWORDS:
[Generated keywords]
======================================

Note: The actual analysis depends on the model’s responses.

Learning Objectives

This project demonstrates:

- Building LLM-powered applications with LangChain.
- Composing processing steps using LCEL.
- Running independent LLM tasks in parallel.
- Preserving input data throughout a pipeline.
- Parsing and formatting LLM outputs.

Future Improvements

- Accept user-provided text instead of a predefined article.
- Stream model responses.
- Add structured output using Pydantic.
- Support PDF and document input.
- Add a simple web interface.

License

This project is available for educational and personal use.

**One technical note:** Your current implementation uses `RunnablePassthrough()` to preserve the original input dictionary, which is why your formatting function accesses the article through `results["original_article"]["text"]`. Also, `RunnableParallel` permits concurrent execution, but actual speed depends on your local hardware and Ollama's resource usage.
