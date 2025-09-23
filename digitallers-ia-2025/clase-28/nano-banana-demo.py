from google import genai
from google.generativeai import types
from PIL import Image
from io import BytesIO


api_key = input("ingrese su api key de google")
prompt_str = input("ingrese su prompt para generar la imagen")


client = genai.Client(api_key)

prompt = ( prompt_str)

response = client.models.generate_content(
    model="gemini-2.5-flash-image-preview",
    contents=[prompt],
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = Image.open(BytesIO(part.inline_data.data))
        image.save("generated_image.png")