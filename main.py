from tkinter import *
from PIL import ImageTk, Image
import os

# Initialize Counter
counter = 0


def rotate_image():
    global counter
    counter = (counter + 1) % len(img_array)
    img_label.config(image=img_array[counter])


root = Tk()
root.title('Wallpaper Viewer')
root.geometry('500x700')
root.configure(background='black')

# Load images
files = os.listdir('wallpapers')
img_array = []

for file in files:
    try:
        img = Image.open(os.path.join('wallpapers', file))
        resized_img = img.resize(
            (400, 600))  # Adjusted size for better display
        img_array.append(ImageTk.PhotoImage(resized_img))
    except Exception as e:
        print(f"Error loading image {file}: {e}")

if img_array:
    img_label = Label(root, image=img_array[0], background='black')
    img_label.pack(pady=(20, 10))

    next_btn = Button(root,
                      text='Next Image',
                      bg='#007BFF',
                      fg='white',
                      font=('Verdana', 12),
                      width=20,
                      height=2,
                      command=rotate_image,
                      relief=RAISED,
                      borderwidth=2)
    next_btn.pack(pady=20)
else:
    img_label = Label(root,
                      text="No images found",
                      bg='black',
                      fg='white',
                      font=('Verdana', 16))
    img_label.pack(pady=(20, 10))

root.mainloop()
