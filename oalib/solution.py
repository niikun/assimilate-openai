"""Library with OpenAI API solutions as functions

References:

For building code:  https://beta.openai.com/docs/guides/code/introduction

"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


def submit_question(text):
    """
    This function submits a question to the OpenAI API and returns the answer.

    Args:
    text (str): The question to ask the API

    Returns:
    str: The answer from the API
    """
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")
    # api_key = os.getenv("LANGCHAIN_API_KEY")


    model = ChatOpenAI(model="gpt-4o", api_key=api_key)
    prompt = ChatPromptTemplate.from_messages(
        [(
            "system","You are a helpful Osaka woman.Answer all questions in Japanese,Osaka language."
            ),
            MessagesPlaceholder(variable_name="messages")
        ]
    )
    chain = prompt | model

    response = chain.invoke({"messages":[HumanMessage(content=text)]})
    return response.content



# build a function that converts a comment into code in any language
def create_code(text, language):
    """This submits a comment to the OpenAI API to create code in any language

    Example:
        language = '# Python3'
        text = f"Calculate the mean distance between an array of points"
        create_code(text, language)

    """
  
    mission = f"## {language}\n\n{text}"
    model = ChatOpenAI(model="gpt-4o")


    prompt = ChatPromptTemplate.from_messages(
        [(
            "system","build a function that converts a comment into code in any language."
            ),
            MessagesPlaceholder(variable_name="messages")
        ], mission)

    chain = prompt | model

    response = chain.invoke({"messages":[HumanMessage(content=text)]})
    return response.content