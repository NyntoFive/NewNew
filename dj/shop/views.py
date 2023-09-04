import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts.chat import (
    HumanMessagePromptTemplate,
    ChatPromptTemplate,

)

from pages.models import DJItem

from django.shortcuts import render

from django.core import serializers
from django.http import HttpResponse
import json

def get_data(file="TEST.json"):
    print(os.getcwd())
    with open(file) as f:
        data = json.load(f)
    return data

def some_view(request):
    qs = DJItem.objects.all()
    qs_json = serializers.serialize('json', qs)
    return HttpResponse(qs_json, content_type="application/json")

def last_crawl_view(request, data=None):
    if data is None:
        data = get_data()
    # data_json = serializers.serialize('json', data)
    return HttpResponse(data, content_type="application/json")


load_dotenv()

OPENAI_MODEL = "gpt-4"
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
PROMPT_COUNTRY_INFO = """
    Provide information about {country}.
    """


def main(request):
    llm = OpenAI(openai_api_key=OPENAI_API_KEY)
    result = llm.predict("Give me 5 topics for interesting YouTube videos about Python")

def index(request):
    return render(request, template_name="index.html", )