# This program although looks correct does not do what you would expect. 
# Prompt: 
# Please write a new program in python which utilizes the Gemini model in VertexAI to teach a person about the history of Natural Language PRocessing


import gemini

# Create a Gemini client
client = gemini.GeminiClient()

# Create a new text generator assistant
assistant = client.create_text_generator(
   project_id="YOUR_PROJECT_ID",
   location="YOUR_LOCATION",
   assistant_id="YOUR_ASSISTANT_ID",
)

# Select the Gemini model
model_name = "text-bison-001"

# Create the text generation request
request = gemini.TextGenerationRequest(
   model=model_name,
   prompt="Provide a brief history of natural language processing.",
)

# Use the text generation assistant to generate text for the prompt
response = assistant.generate_text(request)

# Print the generated text
print(response.generated_text)