import tkinter as tk
from tkinter import filedialog, scrolledtext, ttk
from PIL import Image, ImageTk  
from model_text import TextModelHandler
from model_image import ImageModelHandler

# Handlers
text_model = TextModelHandler()
image_model = ImageModelHandler()

selected_image = [None]  # store image path

# ----- GUI Functions -----
def run_model():
    """Run the chosen model and display formatted output."""
    output_box.config(state="normal")
    output_box.delete("1.0", "end")
    if choice.get() == "Text":
        user_text = text_entry.get()
        if not user_text.strip():
            output_box.insert("end", "Please enter some text.\n")
            return
        result = text_model.run(user_text)
        output_box.insert("end", f"Text input: {user_text}\n")
        output_box.insert("end", f"Model result: {result}\n")

    elif choice.get() == "Image":
        if not selected_image[0]:
            output_box.insert("end", "Please choose an image first.\n")
            return
        result = image_model.run(selected_image[0])
        output_box.insert("end", f"Image: {selected_image[0]}\n")
        output_box.insert("end", f"Top predictions:\n{result}\n")
    output_box.config(state="disabled")

def choose_image():
    """Open file dialog to choose image and preview it."""
    path = filedialog.askopenfilename(
        initialdir="sample_inputs", title="Select image",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
    )
    if path:
        selected_image[0] = path
        # Display path in output box
        output_box.config(state="normal")
        output_box.insert("end", f"Selected image: {path}\n")
        output_box.config(state="disabled")
        # Display preview
        img = Image.open(path)
        img.thumbnail((200, 200))
        img_tk = ImageTk.PhotoImage(img)
        preview_label.config(image=img_tk)
        preview_label.image = img_tk  # keep reference

def update_inputs(*args):
    """Disable irrelevant inputs based on selection."""
    if choice.get() == "Text":
        text_entry.config(state="normal")
        choose_button.config(state="disabled")
    else:
        text_entry.config(state="disabled")
        choose_button.config(state="normal")

# ----- GUI Layout -----
root = tk.Tk()
root.title("HIT137 AI Model GUI")
root.geometry("800x600")

# Input type selection
choice = tk.StringVar(value="Text")
choice.trace("w", update_inputs)
tk.Label(root, text="Select input type:").pack()
tk.Radiobutton(root, text="Text", variable=choice, value="Text").pack()
tk.Radiobutton(root, text="Image", variable=choice, value="Image").pack()

# Text entry
text_entry = tk.Entry(root, width=60)
text_entry.insert(0, "Type your text here...")
text_entry.pack(pady=5)

# Image selection button
choose_button = tk.Button(root, text="Choose Image", command=choose_image)
choose_button.pack()
choose_button.config(state="disabled")

# Image preview
preview_label = tk.Label(root)
preview_label.pack(pady=5)

# Run button
tk.Button(root, text="Run Model", command=run_model).pack(pady=10)

# Output box
tk.Label(root, text="Model output:").pack()
output_box = scrolledtext.ScrolledText(root, height=10)
output_box.pack(fill="both", expand=True, padx=10, pady=5)
output_box.config(state="disabled")

# OOP explanation
tk.Label(root, text="OOP concepts used:").pack()
oop_box = tk.Text(root, height=5)
oop_box.pack(fill="both", expand=True, padx=10, pady=5)
oop_box.insert("1.0",
    "Encapsulation: model classes keep their own state (loaded or not).\n"
    "Polymorphism: both text and image classes use the same run() method.\n"
    "Inheritance: handlers inherit from a base class and Logger.\n"
    "Decorator: simple_timer shows how long model runs take.\n"
    "Overriding: load() and run() methods are overridden in each child class.\n"
)
oop_box.config(state="disabled")

# Model info section
tk.Label(root, text="Model Information:").pack()
model_info = tk.Text(root, height=5)
model_info.pack(fill="both", expand=True, padx=10, pady=5)
model_info.insert("1.0",
    "Text Model:\n"
    "  Name: distilbert-base-uncased-finetuned-sst-2-english\n"
    "  Category: Text Classification\n"
    "  Link: https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english\n\n"
    "Image Model:\n"
    "  Name: google/vit-base-patch16-224\n"
    "  Category: Image Classification\n"
    "  Link: https://huggingface.co/google/vit-base-patch16-224\n"
)
model_info.config(state="disabled")

root.mainloop()