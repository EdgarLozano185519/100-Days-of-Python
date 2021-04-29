#Import required Image library
from PIL import Image as img
from PIL import ImageDraw, ImageFont
# Import screen reader library
import accessible_output2.outputs.auto
from tkinter import filedialog
from tkinter import *
from sr_label import Sr_Label as sl
from sr_button import Sr_Button as sb
from sr_input import Sr_Input as si

# Initialize screen reader library
s = accessible_output2.outputs.auto.Auto()

def watermark():
    #Create an Image Object from an Image
    im = img.open(window.filename)
    width, height = im.size

    draw = ImageDraw.Draw(im)
    text = watermark_input.get()

    font = ImageFont.truetype('arial.ttf', 36)
    textwidth, textheight = draw.textsize(text, font)

    # calculate the x,y coordinates of the text
    margin = 10
    x = width - textwidth - margin
    y = height - textheight - margin

    # draw watermark in the bottom right corner
    draw.text((x, y), text, font=font)
    im.show()

    #Save watermarked image
    im.save('images/watermark.jpg')


# UI Setup
window = Tk()
window.title("WaterMark")

# Set label
watermark_label = sl("Watermark")
watermark_label.grid(column=1, row=1)

# Input to enter text to be used as watermark
watermark_input_label = sl("Watermark text: ")
watermark_input_label.grid(column=1, row=2)
watermark_input = si("Watermark text: ")
watermark_input.grid(column=2, row=2)


# Function to open browse dialog
def get_file():
    window.filename = filedialog.askopenfilename(
      initialdir=".",
      title="Select file",
      filetypes=(
        ("jpeg files","*.jpg"),
        ("all files","*.*")
      )
    )
    print(window.filename)


# Button to browse for file
browse_file = sb("Find file.", command=get_file)
browse_file.grid(column=3, row=2)

# Watermark
watermark_button = sb("Watermark", command=watermark)
watermark_button.grid(column=1, row=3)

# Run window
window.mainloop()
