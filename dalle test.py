import asyncio
import openai
from openai import Image

from func import convertImage

async def create_edit(image_path,mask_path):
    image = Image()
    openai.api_key = ''
    
    response = await image.acreate_edit(
        model="dall-e-2",
        image=open(image_path, "rb"),
        mask=open(mask_path, "rb"),
        prompt="A woman lying on the bed",
        n=1,
        size="1024x1024"
    )

    image_url = response.data[0].url

    return image_url

  
result = asyncio.run(create_edit("roomDecor.png_converted.png","bedinpaint.png_converted.png"))
print(result)

#So right now it is left with how we will add a prompt and another image