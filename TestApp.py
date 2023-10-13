import tkinter as tk
import customtkinter as ctk
import torch
from diffusers import StableDiffusionPipeline
import os

from PIL import ImageTk, Image

from authtoken import auth_token 

IMAGE_WIDTH = 300
IMAGE_HEIGHT = 300
IMAGE_PATH = "Picture.png"

def on_entry_click(event):
    #function that gets called whenever entry is clicked
    if prompt.get() == "Generate a picture":
       prompt.delete(0, "end") # delete all the text in the entry
       prompt.insert(0, '') #Insert blank for user input
       prompt.configure("color", text_color="black")

#Create the App Window
App = tk.Tk()   
App.geometry("400x500")
App.title("Image Generator")
#App.resizable(width = True, height = True)
ctk.set_appearance_mode("dark") 

prompt = ctk.CTkEntry(master=App, height=40, width=380, text_color="grey", fg_color="white") 
prompt.place(x=10, y=10)
prompt.insert(0, "Generate a picture")
prompt.bind("<FocusIn>", on_entry_click)

device = "cuda"
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", revision="fp16", torch_dtype=torch.float16, use_auth_token=auth_token, device_map="auto")

def button_function():
    image = pipe(prompt.get()).images[0]
    image.save(f"Picture.png")

    your_image = ctk.CTkImage(Image.open(os.path.join(IMAGE_PATH)), size=(IMAGE_WIDTH , IMAGE_HEIGHT))
    label = ctk.CTkLabel(master=App, image=your_image, text='')
    label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

button = ctk.CTkButton(master=App, corner_radius=10, command=button_function, text="Generate")
button.configure(text="Generate") 
button.place(x=130,y=60)

App.mainloop()