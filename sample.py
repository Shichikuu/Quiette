from tkinter import *
from tkinter import filedialog
from pydub import AudioSegment

def create_text_field():
    def get_name():
        # Function to get the name entered by the user
        user_name = name_entry.get()
        print("User entered name:", user_name)
        name_window.destroy()

    def upload_file():
        # Function to upload an MP3 file
        mp3_file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])

        if mp3_file_path:
            # Load and process the MP3 file (you can customize this part)
            audio = AudioSegment.from_mp3(mp3_file_path)
            print("Selected MP3 file:", mp3_file_path)
            print("MP3 Duration:", len(audio), "milliseconds")

    # Create a new window with a text field
    name_window = Tk()
    name_window.title('Enter Your Name')

    # Entry widget for the user to input their name
    name_entry = Entry(name_window, font=("Times bold", 14))
    name_entry.pack(padx=20, pady=20)

    # Button to get the entered name
    get_name_button = Button(name_window, text="Get Name", font=("Times bold", 14), command=get_name)
    get_name_button.pack(pady=10)

    # Button to upload an MP3 file
    upload_button = Button(name_window, text="Upload MP3 File", font=("Times bold", 14), command=upload_file)
    upload_button.pack(pady=10)

    name_window.mainloop()

# Example usage
if __name__ == "__main__":
    create_text_field()
