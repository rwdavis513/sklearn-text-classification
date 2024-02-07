# import google.generativeai as genai

# model = genai.GenerativeModel('gemini-pro')

# response = model.generate_content("Please tell me about the history of Natural Language Processing")

# print(response)
# !pip install --upgrade google-cloud-aiplatform
#import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part

def generate():
  model = GenerativeModel("gemini-pro")
  responses = model.generate_content(
    """Please tell me the history of Natural Language Processing highlighting the various techniques developed over the past 30 years. Please utilize language that a college student in Computer Science would understand.""",
    generation_config={
        "max_output_tokens": 2048,
        "temperature": 0.9,
        "top_p": 1
    },
    safety_settings=[],
  stream=True,
  )
  
  for response in responses:
      print(response.text, end="")


generate()