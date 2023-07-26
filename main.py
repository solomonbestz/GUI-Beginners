from settings import *

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


def create_frame(parent, bg_color = 'transparent', **others):
    frame = ctk.CTkFrame(
        parent,
        width= int(others.get("width", 0)),
        height= int(others.get("height", 0)),
        corner_radius=others.get("corner_radius"),
        border_width=others.get("border_width"),
        fg_color=others.get("fg_color"),
        bg_color=bg_color,
        border_color=others.get("border_color"),
        background_corner_colors=others.get("background_corner_colors"),
    )
    return frame




if __name__ == "__main__":
    root = ctk.CTk()
    root.title("Foodie")
    root.iconbitmap("images/logo.ico")
    root.geometry("700x400")
    root.columnconfigure((0, 1), weight=1)
    root.rowconfigure(0, weight=1)

    # Side Frame
    side_frame = create_frame(root, fg_color=SIDE_COLOR, width=350, corner_radius=0)
    side_frame.grid(row=0, column=0, sticky="nswe")

    # Main Frame
    main_frame = create_frame(root, fg_color=MAIN_COLOR, width=350, corner_radius=0)
    main_frame.grid(row=0, column=1, columnspan=2, padx=(0, 0), sticky="nswe")

    main_frame.columnconfigure(0, weight=1)
    main_frame.rowconfigure(0, weight=1)

    # Create a Frame Inside Main Frame
    form_frame = create_frame(main_frame, fg_color=FORM_COLOR, height=300)
    form_frame.grid(row=0, column=0, ipady=150, ipadx=200)

    form_frame.columnconfigure(0, weight=1)

    form_label = ctk.CTkLabel(form_frame, text='SIGN IN', width=50, text_color=TEXT_COLOR)
    form_label.grid(row=0, column=0, pady=(10, 0))
    

    root.mainloop()
