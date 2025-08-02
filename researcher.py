import re

from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent

def clean_text(text: str):
    cleaned_text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    return cleaned_text.strip()



model = ChatOllama(model="qwen3:8b")


query_refiner_prompt = (
    "You are a query refiner agent.\n\n"
    "INSTRUCTIONS:\n"
    "- Refine the user's query to make it more specific and actionable\n"
    "- Respond ONLY with the refined query, do NOT include any other text."
)
research_prompt = (
    "You are a research agent.\n\n"
    "INSTRUCTIONS:\n"
    "- Assist ONLY with research-related tasks, DO NOT do anything else\n"
    "- After you're done with your research, respond to the supervisor directly\n"
    "- Respond ONLY with the summary of the results, do NOT include ANY other text."
)
supervisor_prompt = (
    "You are a supervisor agent.\n\n"
    "INSTRUCTIONS:\n"
    "- Manage the workflow between the query refiner and researcher agents\n"
    "- Use the Query Refiner Agent to correct typos and enhance the query for better search relevance\n"
    "- Use the Research Agent to retrieve up-to-date information from the web\n"
    "- Respond ONLY with the final response, do NOT include any other text."
)
