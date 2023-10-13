import torch
from diffusers import StableDiffusionPipeline

from authtoken import auth_token

device = "cuda"

pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", revision="fp16", torch_dtype=torch.float16, use_auth_token=auth_token, device_map="auto")

pipe.to(device)

prompt = "hej med dig"

image = pipe(prompt).images[0]

image.save(f"Picture.png")