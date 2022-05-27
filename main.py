import tkinter
from tkinter import messagebox
from PIL import ImageTk, Image, ImageDraw, ImageFont, ImageFilter
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.simpledialog import askstring

FONT_NAME = "Courier"
SOURCE_DIRECTORY = "C:/Users/admin/OneDrive/Pictures/Screenshots"
TARGET_DIRECTORY = "C:/Users/admin/OneDrive/Pictures/Watermarked"

global original_image_size, image


def show_frame(frame):
    frame.tkraise()


def add_file():
    global original_image_size, image
    photo_name = askopenfilename(initialdir=SOURCE_DIRECTORY, title="Select A File",
                                 filetypes=(("png files", "*.png"), ("all files", "*.*")))
    image = Image.open(photo_name)
    original_image_size = image.size
    resized_image = image.resize((300, 205), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(resized_image)
    label.configure(image=new_image)
    label.image = new_image


def save_new_image():
    global image
    photo_name = asksaveasfilename(initialdir=TARGET_DIRECTORY, title="Select A File",
                                   filetypes=(("png files", "*.png"), ("all files", "*.*")))
    name = photo_name + ".png"
    image.save(name)
    messagebox.showinfo("Success!", "Your file was saved successfully.")
    show_frame(start_frame)


def add_image_wm():
    global image, original_image_size
    photo_name = askopenfilename(initialdir=SOURCE_DIRECTORY, title="Select A File",
                                 filetypes=(("png files", "*.png"), ("all files", "*.*")))
    watermark = Image.open(photo_name)
    mask_im = Image.new("L", watermark.size, 0)
    draw = ImageDraw.Draw(mask_im)
    draw.rectangle((10, 10, watermark.size[0] - 10, watermark.size[1] - 10), fill=255)
    mask_img_blur = mask_im.filter(ImageFilter.GaussianBlur(10))
    y = original_image_size[0] - 200
    x = original_image_size[1] - 100
    image.paste(watermark, (y, x), mask_img_blur)
    new_image = ImageTk.PhotoImage(image.resize((300, 205), Image.ANTIALIAS))
    label.configure(image=new_image)
    label.image = new_image


def add_text_wm():
    global image, original_image_size
    text = askstring('Text Watermark', 'Enter the text you want as the watermark: ')
    img = ImageDraw.Draw(image)
    my_font = ImageFont.truetype("arial.ttf", 25)
    y = original_image_size[0] - 150
    x = original_image_size[1] - 40
    img.text((y, x), text, font=my_font, fill=(0, 0, 0))
    new_image = ImageTk.PhotoImage(image.resize((300, 205), Image.ANTIALIAS))
    label.configure(image=new_image)
    label.image = new_image


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Image Watermarker")
window.config(padx=100, pady=50)
# window.geometry("800x400")

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

start_frame = tkinter.Frame(window)
main_frame = tkinter.Frame(window)

for frame in (start_frame, main_frame):
    frame.grid(column=0, row=0, sticky="nsew")

# ------------- START FRAME ------------- #
timer_label = tkinter.Label(start_frame, text="Image Watermarker", font=(FONT_NAME, 25, "bold"))
timer_label.grid(column=0, row=0, pady=25)

add_file_button = tkinter.Button(start_frame, text="Add File", width=15,
                                 command=lambda: [add_file(), show_frame(main_frame)])
add_file_button.grid(column=0, row=1, padx=10, pady=10)

show_frame(start_frame)

# ------------- MAIN FRAME ------------- #
timer_label = tkinter.Label(main_frame, text="Image Watermarker", font=(FONT_NAME, 25, "bold"))
timer_label.grid(row=0, columnspan=2, pady=25)

user_image = tkinter.PhotoImage(file="img.png")
label = tkinter.Label(main_frame, image=user_image)
label.image = user_image  # keep a reference!
label.grid(column=0, row=1, rowspan=3, padx=25)

add_text_button = tkinter.Button(main_frame, text="Add Text", width=15, command=add_text_wm)
add_text_button.grid(column=1, row=1, padx=10, pady=10)

timer_label = tkinter.Label(main_frame, text="or", font=(FONT_NAME, 12, "bold"))
timer_label.grid(column=1, row=2)

add_img_button = tkinter.Button(main_frame, text="Add Image", width=15, command=add_image_wm)
add_img_button.grid(column=1, row=3, padx=10, pady=10)

save_button = tkinter.Button(main_frame, text="Save", width=25, command=save_new_image)
save_button.grid(columnspan=2, row=5, padx=10, pady=25)

window.mainloop()
