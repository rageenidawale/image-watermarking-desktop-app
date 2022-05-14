import tkinter
from PIL import ImageTk, Image

FONT_NAME = "Courier"


def show_frame(frame):
    frame.tkraise()


def add_file():
    pass


def save_new_image():
    pass


def add_image_wm():
    pass


def add_text_wm():
    pass


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
                                 command=lambda: [add_file, show_frame(main_frame)])
add_file_button.grid(column=0, row=1, padx=10, pady=10)

show_frame(start_frame)

# ------------- MAIN FRAME ------------- #
timer_label = tkinter.Label(main_frame, text="Image Watermarker", font=(FONT_NAME, 25, "bold"))
timer_label.grid(row=0, columnspan=2, pady=25)

add_text_button = tkinter.Button(main_frame, text="Add Text", width=15, command=add_text_wm)
add_text_button.grid(column=1, row=1, padx=10, pady=10)

timer_label = tkinter.Label(main_frame, text="or", font=(FONT_NAME, 12, "bold"))
timer_label.grid(column=1, row=2)

add_img_button = tkinter.Button(main_frame, text="Add Image", width=15, command=add_image_wm)
add_img_button.grid(column=1, row=3, padx=10, pady=10)

save_button = tkinter.Button(main_frame, text="Save", width=25, command=save_new_image)
save_button.grid(columnspan=2, row=4, padx=10, pady=25)

window.mainloop()
