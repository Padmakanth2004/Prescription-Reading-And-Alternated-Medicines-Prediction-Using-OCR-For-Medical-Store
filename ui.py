import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from OCR import extract_tablet_name
from ml_text_similarity import suggest_alternate_tablets

def upload_file():
    global selected_file_path
    selected_file_path = filedialog.askopenfilename()
    if selected_file_path:
        print("Selected file:", selected_file_path)
    else:
        print("No file selected.")

def generate_ocr_and_ml():
    global tablet_suggestions_listbox
    if selected_file_path:
        try:
            print("Generating OCR...")
            extracted_tablet_name = extract_tablet_name(selected_file_path)
            if extracted_tablet_name:
                print("Extracted Tablet Name:", extracted_tablet_name)

                # Call ML function to suggest alternate tablet names based on extracted tablet name
                suggestions = suggest_alternate_tablets(extracted_tablet_name, 'dataset.csv')
                if suggestions:
                    print("Alternate Tablet Names:")
                    for tablet_name, similarity_index in suggestions:
                        print(f"Tablet Name: {tablet_name}, Similarity Index: {similarity_index}")
                        tablet_suggestions_listbox.insert(tk.END, f"{tablet_name} (Similarity: {similarity_index:.2f})")
                    messagebox.showinfo("Tablet Suggestions", "Tablet suggestions loaded successfully.")
                else:
                    print("No alternate tablet names found.")
                    messagebox.showinfo("No Suggestions", "No alternate tablet names found for this tablet.")
            else:
                print("No text found in the image.")
                messagebox.showwarning("No Text Found", "No text was extracted from the uploaded image.")
        except Exception as e:
            print("Error during OCR and ML:", str(e))
            messagebox.showerror("Error", f"An error occurred during OCR and ML: {str(e)}")
    else:
        print("Please select a file first.")
        messagebox.showwarning("No File Selected", "Please select a file before generating OCR and ML.")

def create_ui():
    global tablet_suggestions_listbox
    root = tk.Tk()
    root.title("File Upload, OCR, and ML")

    # Set window size
    root.geometry("600x400")

    # Load background image
    background_image = Image.open("img.jpg")
    background_image = background_image.resize((600, 400))
    bg_photo = ImageTk.PhotoImage(background_image)

    # Create a canvas
    canvas = tk.Canvas(root, width=600, height=400)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

    # Add descriptive label
    label = tk.Label(canvas, text="Upload your prescription", font=("Arial", 18), bg="black")
    label.pack(pady=20)

    # Create and place upload button with description
    upload_button = tk.Button(canvas, text="Upload File", command=upload_file, font=("Arial", 14))
    upload_button.pack(pady=10)
    upload_desc_label = tk.Label(canvas, text="Select a prescription image file", font=("Arial", 12), bg="black")
    upload_desc_label.pack()

    # Create and place submit button with description
    submit_button = tk.Button(canvas, text="Submit", command=generate_ocr_and_ml, font=("Arial", 14))
    submit_button.pack(pady=10)
    submit_desc_label = tk.Label(canvas, text="Generate OCR and suggest tablets", font=("Arial", 12), bg="black")
    submit_desc_label.pack()

    # Create Listbox to display tablet suggestions
    tablet_suggestions_listbox = tk.Listbox(canvas, font=("Arial", 12), width=50, height=10)
    tablet_suggestions_listbox.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    selected_file_path = None  # Global variable to store selected file path
    create_ui()
