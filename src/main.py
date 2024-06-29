import crypto_module as crypto

import tkinter
import tkinter.messagebox
import tkinter.filedialog
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")


def show_message_box(title, message):
    tkinter.messagebox.showinfo(title, message)


class DecryptionStatusFrame(customtkinter.CTkFrame):
    def __init__(self, parent, tab_view, tab_name="Decryption", column=0, row=0):
        self.parent = parent
        self.tab_view = tab_view
        self.create_status_frame(tab_name, column=0)
        self.update_status("Status initialized.")

    def create_status_frame(self, tab_name, column=0, row=0):

        self.sub_frame = customtkinter.CTkFrame(
            self.tab_view.tab(tab_name),
            # corner_radius=50,
        )
        self.sub_frame.grid(row=1, column=0, columnspan=5,
                            padx=(20, 10), pady=10, sticky="nsew")

        self.text_widget = customtkinter.CTkTextbox(self.sub_frame, text_color="#99FF00", font=customtkinter.CTkFont(
            size=15, family="Courier"), corner_radius=20, fg_color="#000000")
        self.text_widget.pack(expand=True, fill='both')

    def update_status(self, message):
        self.text_widget.insert('end', message + '\n')
        self.text_widget.yview('end')


class StatusFrame(customtkinter.CTkFrame):
    def __init__(self, parent, tab_view, tab_name="Encryption", column=2, row=0):
        self.parent = parent
        self.tab_view = tab_view
        self.create_status_frame(tab_name, column=2)
        self.update_status("Status initialized.")

    def create_status_frame(self, tab_name, column=2):
        self.status_label = customtkinter.CTkLabel(
            self.tab_view.tab(tab_name),
            text="STATUS CHECK",
            font=customtkinter.CTkFont(
                size=25, family="Courier", weight="bold"),
            text_color="#FF70AB"
        )

        self.status_label.grid(row=0, column=2, columnspan=3,
                               padx=20, pady=10, sticky="ew")

        self.sub_frame = customtkinter.CTkFrame(
            self.tab_view.tab(tab_name),
            # corner_radius=50,
        )
        self.sub_frame.grid(row=1, column=2, rowspan=9,
                            columnspan=3, padx=(20, 10), pady=10, sticky="nsew")

        self.text_widget = customtkinter.CTkTextbox(self.sub_frame, text_color="#99FF00", font=customtkinter.CTkFont(
            size=15, family="Courier"), corner_radius=20, fg_color="#000000")
        self.text_widget.pack(expand=True, fill='both')

    def update_status(self, message):
        self.text_widget.insert('end', message + '\n')
        self.text_widget.yview('end')  # Scroll to the end

# class StatusFrame(customtkinter.CTkFrame):
#     def __init__(self, parent, tab_view, tab_name="Encryption", column=2, row=0):
#         super().__init__(parent)
#         self.parent = parent
#         self.tab_view = tab_view
#         self.create_status_frame()
#         self.update_status("Status initialized.")

#     def create_status_frame(self):
#         self.status_label = customtkinter.CTkLabel(
#             self,
#             text="STATUS CHECK",
#             font=customtkinter.CTkFont(size=25, family="Courier", weight="bold"),
#             text_color="#FF70AB"
#         )
#         self.status_label.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

#         self.text_widget = customtkinter.CTkTextbox(self, text_color="#99FF00", font=customtkinter.CTkFont(size=15, family="Courier"), corner_radius=20, fg_color="#000000")
#         self.text_widget.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

#         self.grid_columnconfigure(0, weight=1)
#         self.grid_rowconfigure(1, weight=1)

#     def update_status(self, message):
#         self.text_widget.insert('end', message + '\n')
#         self.text_widget.yview('end')  # Scroll to the end


class cryptography_app(customtkinter.CTk):
    input_file_path = ""
    output_folder_path = ""
    key_path = ""

    # set default font for the app

    def __init__(self):
        super().__init__()

        # configure the window
        self.default_font = customtkinter.CTkFont(family="Comic Sans MS")
        self.title("Cryptography App")
        self.geometry(f"{1100}x{600}")

        # configure grid layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=8)

        # create left sidebar frame
        self.left_sidebar = customtkinter.CTkFrame(
            self, width=140, corner_radius=0)
        self.left_sidebar.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.left_sidebar.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.left_sidebar, text="CRYPTOGRAPHY", font=customtkinter.CTkFont(
            size=25, weight="bold", family="Comic Sans MS"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(40, 10))

        # load logo image
        logo_image = customtkinter.CTkImage(
            light_image=Image.open("src/assets/logo.png"), size=(200, 200))
        my_logo = customtkinter.CTkLabel(
            self.left_sidebar, image=logo_image, text="")
        my_logo.grid(row=1, column=0, padx=20, pady=10)

        self.display_student_name("Minh Minh", "21127528", 2)
        self.display_student_name("Dang Huynh", "21127063", 3)

        # appearance mode
        self.appearance_mode_label = customtkinter.CTkLabel(
            self.left_sidebar, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.left_sidebar, values=["Dark", "Light", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(
            row=6, column=0, padx=20, pady=(10, 30))

        # create 2 main frames: main_frame_1
        self.main_frame_1 = customtkinter.CTkFrame(self, corner_radius=10)
        self.main_frame_1.grid(row=0, column=1, padx=20,
                               pady=(10, 2), sticky="nsew")

        # Set column weights
        self.main_frame_1.grid_columnconfigure(0, weight=1)
        self.main_frame_1.grid_columnconfigure(1, weight=7)
        self.main_frame_1.grid_columnconfigure(2, weight=1)

        # Set row weights
        self.main_frame_1.grid_rowconfigure(0, weight=1)
        self.main_frame_1.grid_rowconfigure(1, weight=1)
        self.main_frame_1.grid_rowconfigure(2, weight=1)

        # Create folder selection widgets
        # self.create_folder_selection_widgets("String Input", self.main_frame_1, row=0)
        self.create_folder_selection_widgets(
            "Input File", self.main_frame_1, row=1)
        self.create_folder_selection_widgets(
            "Output Folder", self.main_frame_1, row=2)

        # Create tab view
        self.tab_view = customtkinter.CTkTabview(self, corner_radius=10)
        self.tab_view.grid(row=1, column=1, padx=(
            10, 10), pady=(5, 10), sticky="nsew")

        # Create tab 1
        self.tab_1 = customtkinter.CTkFrame(self.tab_view, corner_radius=10)
        self.tab_view.add("Encryption")
        self.tab_view.tab("Encryption").grid_columnconfigure(0, weight=2)
        self.tab_view.tab("Encryption").grid_columnconfigure(1, weight=2)
        self.tab_view.tab("Encryption").grid_columnconfigure(2, weight=10)
        self.tab_view.tab("Encryption").grid_columnconfigure(3, weight=3)
        # self.tab_view.tab("Encryption").grid_columnconfigure(4, weight=1)

        # Component in tab 1
        # PART 1 - AES ENCRYPTION
        self.genKs = self.create_custom_label(
            "Encryption", "∙ Generate Ks Key and Encryption", 0, 0)
        self.encrypt_button = self.create_custom_button(
            "Encryption", "ENCRYPT with AES", self.encrypt_with_aes, 0, 1)
        self.separator = self.create_separator("Encryption", 1, 0, 2)

        # PART 2 - RSA ENCRYPTION
        self.RSA_alg = self.create_custom_label(
            "Encryption", "∙ RSA Algorithm", 2, 0)
        self.RSA_keypair = self.create_custom_button(
            "Encryption", "RSA KEY PAIR", self.encrypt_with_rsa, 2, 1)
        self.RSA_encrypt = self.create_custom_button(
            "Encryption", "RSA ENCRYPT", self.encrypt_with_rsa, 3, 1)
        self.create_separator("Encryption", 4, 0, 2)

        # PART 3 - SAVE METADATA
        # Create radio buttons for file structure
        self.file_structure = self.create_custom_label(
            "Encryption", "∙ File Structure", 5, 0)
        # Replace with your actual options
        self.file_structure_options = ["XML", "JSON", "Plaintext"]
        self.file_structure_var = self.create_radio_buttons(
            "Encryption", self.file_structure_options, 5, 1)

        # Save metadata
        self.save_metadata = self.create_custom_label(
            "Encryption", "∙ Save Metadata", 6, 0)
        self.save_button = self.create_custom_button(
            "Encryption", "SAVE METADATA", self.encrypt_with_rsa, 6, 1)
        self.create_separator("Encryption", 7, 0, 2)

        # PART 4 - EXPORT KEY PRIVATE
        self.export_key = self.create_custom_label(
            "Encryption", "∙ Export Key Private", 8, 0)
        self.export_button = self.create_custom_button(
            "Encryption", "EXPORT KPrivate", self.export_Kprivate, 8, 1)

        # PART 5 - STATUS BAR ON THE COLUMN 3
        self.StatusFrame = StatusFrame(
            self.main_frame_1, self.tab_view, tab_name="Encryption", column=0, row=5)
        # self.status_frame_encrypt.update_status("Status initialized.")

        # Component in tab 2
        # Create tab 2
        self.tab_2 = customtkinter.CTkFrame(self.tab_view, corner_radius=10)
        self.tab_view.add("Decryption")
        self.tab_view.tab("Decryption").grid_columnconfigure(0, weight=1)
        self.tab_view.tab("Decryption").grid_columnconfigure(1, weight=5)
        self.tab_view.tab("Decryption").grid_columnconfigure(2, weight=1)
        self.tab_view.tab("Decryption").grid_columnconfigure(3, weight=5)
        self.tab_view.tab("Decryption").grid_columnconfigure(4, weight=1)

        # Create a sub-frame for the decryption tab at the second row
        self.sub_frame_tab2 = customtkinter.CTkFrame(self.tab_view.tab(
            "Decryption"), corner_radius=10, fg_color="#153448")
        self.sub_frame_tab2.grid(
            row=1, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")
        self.sub_frame_tab2.grid_columnconfigure(0, weight=1)
        self.sub_frame_tab2.grid_columnconfigure(1, weight=1)
        self.sub_frame_tab2.grid_columnconfigure(2, weight=1)
        # PART 1 - KPrivate
        self.genKs = self.create_custom_label(
            "Decryption", "∙ KPrivate File", 0, 0)

        # Frame for folder path display
        path_display_frame = customtkinter.CTkFrame(self.tab_view.tab(
            "Decryption"), corner_radius=5, fg_color="#153448")
        path_display_frame.grid(
            row=0, column=1, columnspan=3, padx=(0, 0), pady=5, sticky="ew")
        # File path label
        file_path_label = customtkinter.CTkLabel(path_display_frame, text="", font=customtkinter.CTkFont(
            size=13, family="Courier"), text_color="white", anchor="w", justify="left")
        file_path_label.grid(row=0, column=1, columnspan=3,
                             padx=(8, 0), pady=4, sticky="w")

        # Folder icon label (acts as a button)
        folder_icon_image = customtkinter.CTkImage(
            light_image=Image.open("src/assets/folder.png"), size=(30, 30))
        folder_icon_label = customtkinter.CTkLabel(self.tab_view.tab(
            "Decryption"), text="", image=folder_icon_image, bg_color="transparent", anchor="w", cursor="hand2", justify="right")
        folder_icon_label.grid(row=0, column=4, pady=5)

        # Bind the folder icon label to the browse_file method with the corresponding arguments
        folder_icon_label.bind("<Button-1>", lambda event, fp_label=file_path_label,
                               ft="KPrivate File": self.browse_file(fp_label, ft))

        label_Kprivate = customtkinter.CTkLabel(
            self.sub_frame_tab2,
            text="∙ Verify KPrivate",
            text_color="#95D2B3",
            font=customtkinter.CTkFont(
                size=14, weight="normal", family="Courier"),
            anchor="w",
            justify="center"
        )
        label_Kprivate.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        label_Kprivate = customtkinter.CTkLabel(
            self.sub_frame_tab2,
            text="∙ Descrypt Ks",
            text_color="#95D2B3",
            font=customtkinter.CTkFont(
                size=14, weight="normal", family="Courier"),
            anchor="w",
            justify="center"
        )
        label_Kprivate.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        label_Kprivate = customtkinter.CTkLabel(
            self.sub_frame_tab2,
            text="∙ Decrypt File",
            text_color="#95D2B3",
            font=customtkinter.CTkFont(
                size=14, weight="normal", family="Courier"),
            anchor="w",
            justify="center"
        )
        label_Kprivate.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

        verify_button = customtkinter.CTkButton(
            self.sub_frame_tab2,
            text="VERIFY KPrivate",
            corner_radius=5,
            fg_color="#FFB4C2",
            text_color="black",
            font=customtkinter.CTkFont(
                size=13, weight="bold", family="Trebuchet MS"),
            hover_color="#E0A75E",
            width=15,
            command=self.verify_Kprivate
        )
        verify_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        decrypt1_button = customtkinter.CTkButton(
            self.sub_frame_tab2,
            text="DECRYPT Ks",
            corner_radius=5,
            fg_color="#FFB4C2",
            text_color="black",
            font=customtkinter.CTkFont(
                size=13, weight="bold", family="Trebuchet MS"),
            hover_color="#E0A75E",
            width=15,
            command=self.verify_Kprivate
        )
        decrypt1_button.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        decrypt2_button = customtkinter.CTkButton(
            self.sub_frame_tab2,
            text="DECRYPT FILE",
            corner_radius=5,
            fg_color="#FFB4C2",
            text_color="black",
            font=customtkinter.CTkFont(
                size=13, weight="bold", family="Trebuchet MS"),
            hover_color="#E0A75E",
            width=15,
            command=self.decrypt_with_aes
        )
        decrypt2_button.grid(row=2, column=2, padx=10, pady=10, sticky="ew")
        self.create_separator("Decryption", 2, 0, 5)

        self.tab_view.tab("Decryption").grid_rowconfigure(3, weight=1)
        self.DecryptionStatusFrame = DecryptionStatusFrame(self.tab_view.tab(
            "Decryption"), self.tab_view, tab_name="Decryption", column=0, row=3)
        self.DecryptionStatusFrame.sub_frame.grid(
            row=3, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

    def verify_Kprivate(self):
        show_message_box("Verify KPrivate", "Verifying KPrivate")
        self.DecryptionStatusFrame.update_status("Verifying KPrivate")

    def decrypt_with_aes(self):
        show_message_box("Decrypt File", "Decrypting File")
        self.DecryptionStatusFrame.update_status("Decrypting File")

    def create_radio_buttons(self, tab_name, options, row, column):
        radio_var = tkinter.StringVar(value="")
        radio_frame = customtkinter.CTkFrame(self.tab_view.tab(tab_name))
        radio_frame.grid(row=row, column=column, sticky="w", padx=20, pady=5)

        for i, option in enumerate(options):
            radio = customtkinter.CTkRadioButton(
                radio_frame,
                text=option,
                variable=radio_var,
                value=option,
                command=self.radio_button_event,
                fg_color="#FFB4C2",
                hover_color="#FFB4C2"
            )
            # Adjust pady for vertical spacing
            radio.grid(row=i, column=0, sticky="w", pady=2)

        return radio_var

    def radio_button_event(self):
        selected_option = self.file_structure_var.get()
        print(f"Selected option: {selected_option}")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def display_student_name(self, student_name: str, student_id: str, row_indx):
        student_frame = customtkinter.CTkFrame(
            self.left_sidebar, corner_radius=10)
        student_frame.grid(row=row_indx, column=0, padx=15,
                           pady=(8, 5), sticky="ew")
        student_frame.grid_columnconfigure(0, weight=1)
        student_name_label = customtkinter.CTkLabel(
            student_frame, text=f"{student_id} - {student_name}", font=customtkinter.CTkFont(size=16, weight="bold", family="Candara"), anchor="w")
        student_name_label.grid(row=row_indx, column=0,
                                padx=10, pady=5, sticky="w")

    def create_folder_selection_widgets(self, label_text, frame, row):
        if label_text == "String Input":
            # Label for folder selection
            label = customtkinter.CTkLabel(frame, text=label_text, font=customtkinter.CTkFont(
                size=14, weight="bold", family="Comic Sans MS"))
            label.grid(row=row, column=0, sticky="w",
                       padx=(25, 0), pady=(10, 5))
            # string input entry
            entry = customtkinter.CTkEntry(
                frame, font=customtkinter.CTkFont(size=12))
            entry.grid(row=row, column=1, padx=(
                0, 0), pady=(10, 5), sticky="ew")

            # upload button
            upload_button = customtkinter.CTkButton(
                frame, text="Upload", corner_radius=5, command=self.upload_content)
            upload_button.grid(row=row, column=2, padx=(10, 0), pady=(10, 5))
            return

        # Label for folder selection
        label = customtkinter.CTkLabel(frame, text=label_text, font=customtkinter.CTkFont(
            size=14, weight="bold", family="Courier New"))
        label.grid(row=row, column=0, sticky="w", padx=(25, 0))

        # Frame for folder path display
        path_display_frame = customtkinter.CTkFrame(frame, corner_radius=5)
        path_display_frame.grid(
            row=row, column=1, padx=(0, 0), pady=5, sticky="ew")
        path_display_frame.grid_columnconfigure(0, weight=1)

        # File path label
        file_path_label = customtkinter.CTkLabel(
            path_display_frame, text="", font=customtkinter.CTkFont(size=12), anchor="w", justify="left")
        file_path_label.grid(row=0, column=1, padx=10, pady=4, sticky="w")

        # Folder icon label (acts as a button)
        folder_icon_image = customtkinter.CTkImage(
            light_image=Image.open("src/assets/folder.png"), size=(35, 35))
        folder_icon_label = customtkinter.CTkLabel(
            frame, text="", image=folder_icon_image, anchor="w", cursor="hand2")
        folder_icon_label.grid(row=row, column=2, padx=(0, 10), pady=5)

        # Bind the folder icon label to the browse_file method with the corresponding arguments
        folder_icon_label.bind("<Button-1>", lambda event, fp_label=file_path_label,
                               ft=label_text: self.browse_file(fp_label, ft))

    def upload_content(self):
        show_message_box("Upload Content", "Uploading content")

    def browse_file(self, file_path_label, file_type):
        if file_type == "Input File" or file_type == "KPrivate File":
            file_path = tkinter.filedialog.askopenfilename()
            if file_type == "Input File":
                self.input_file_path = file_path
            elif file_type == "KPrivate File":
                self.key_path = file_path
        else:
            file_path = tkinter.filedialog.askdirectory()
            self.output_folder_path = file_path

        file_path_label.configure(text=file_path)

    def encrypt_with_aes(self):
        show_message_box("Encryption", "Encrypting with AES")
        self.StatusFrame.update_status("Encrypting with AES")

        try:
            # Read the input file
            with open(self.input_file_path, "rb") as file:
                data = file.read()

            # Encrypt the data
            aes_module = crypto.AES(password = "secret", salt = "salt", key_len = 128)
            
            encrypted_data = aes_module.encrypt(data)

            # Write the encrypted data and key to the output folder
            with open(f"{self.output_folder_path}/encrypted_data", "wb") as file:
                file.write(encrypted_data)

            with open(f"{self.output_folder_path}/key", "wb") as file:
                file.write(self.aes_module.key)
            show_message_box("Encryption", "Encryption completed")
        except Exception as e:
            show_message_box("Error", f"An error occurred: {e}")
            return

    def encrypt_with_rsa(self):
        show_message_box("Encryption", "Encrypting with RSA")
        self.StatusFrame.update_status("Encrypting with RSA")

    def export_Kprivate(self):
        show_message_box("Export Key Private", "Exporting Key Private")
        self.StatusFrame.update_status("Exporting Key Private")

    def create_custom_label(self, tab_name, label_text, row_indx, column_indx):
        label = customtkinter.CTkLabel(
            self.tab_view.tab(tab_name),
            text=label_text,
            text_color="#95D2B3",
            font=customtkinter.CTkFont(
                size=14, weight="normal", family="Courier"),
            anchor="w",
            justify="left"
        )
        label.grid(row=row_indx, column=column_indx,
                   padx=10, pady=10, sticky="ew")
        return label

    def create_custom_button(self, tab_name, button_text, button_command, row_indx, column_indx):
        button = customtkinter.CTkButton(
            self.tab_view.tab(tab_name),
            text=button_text,
            corner_radius=5,
            fg_color="#FFB4C2",
            text_color="black",
            font=customtkinter.CTkFont(
                size=13, weight="bold", family="Trebuchet MS"),
            hover_color="#E0A75E",
            command=button_command
        )
        button.grid(row=row_indx, column=column_indx,
                    padx=10, pady=10, sticky="ew")
        return button

    def create_separator(self, tab_name, row, column, columnspan):
        separator = customtkinter.CTkFrame(
            self.tab_view.tab(tab_name), height=2, fg_color="gray")
        separator.grid(row=row, column=column,
                       columnspan=columnspan, sticky="ew", padx=10, pady=10)
        return separator


if __name__ == "__main__":
    app = cryptography_app()
    app.mainloop()
