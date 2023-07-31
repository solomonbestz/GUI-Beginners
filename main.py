from settings import *

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


def event_listener(event):
    if event == 'click':
        authentication()
    
def authentication():
    if first_name_entry.get() and last_name_entry.get() and password_entry.get() == con_password_entry.get():
        print(f'Welcome {first_name_entry.get()} {last_name_entry.get()}, Your Password is {password_entry.get()}')
        first_name_entry.delete(0, ctk.END)
        last_name_entry.delete(0, ctk.END)
        password_entry.delete(0, ctk.END)
        con_password_entry.delete(0, ctk.END)
        form_frame.destroy()
        auth_frame.grid(row=0, column=0, ipady=100, ipadx=200)
        


def create_frame(parent, bg_color="transparent", **others):
    frame = ctk.CTkFrame(
        parent,
        width=int(others.get("width", 0)),
        height=int(others.get("height", 0)),
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
    root.grid_columnconfigure()
    
    # Main Frame
    main_frame = create_frame(root, fg_color=MAIN_COLOR, width=350, corner_radius=0)
    main_frame.grid(row=0, column=0, columnspan=2, padx=(0, 0), sticky="nswe")

    main_frame.columnconfigure(0, weight=1)
    main_frame.rowconfigure(0, weight=1)

    # Create a Frame Inside Main Frame
    form_frame = create_frame(main_frame, fg_color=FORM_COLOR, height=300)
    form_frame.grid(row=0, column=0, ipady=100, ipadx=200)
    form_frame.columnconfigure(0, weight=1)

    auth_frame = create_frame(main_frame, fg_color=BLACK_COLOR, height=300)
    
    
    form_label = ctk.CTkLabel(
        form_frame, text="SIGN UP", width=50, text_color=BLACK_COLOR
    )
    form_label.grid(row=0, column=0, pady=(20, 0))

    input_frame1 = create_frame(form_frame, fg_color=FORM_COLOR)
    input_frame1.grid(row=1, column=0, pady=(0, 10))
    input_frame2 = create_frame(form_frame, fg_color=FORM_COLOR)
    input_frame2.grid(row=2, column=0)

    # input_frame1.columnconfigure(0, weight=1)
    # input_frame1.rowconfigure(0, weight=1)
    # input_frame2.columnconfigure(0, weight=1)
    # input_frame2.rowconfigure(0, weight=1)

    first_name_label = ctk.CTkLabel(input_frame1, text="Frist Name")
    first_name_label.grid(row=0, column=0)
    first_name_entry = ctk.CTkEntry(
        input_frame1,
        border_width=0,
        fg_color=WHITE_COLOR,
        text_color=BLACK_COLOR,
        placeholder_text_color=BLACK_COLOR
    )
    first_name_entry.grid(row=1, column=0, padx=(0, 10))

    last_name_label = ctk.CTkLabel(input_frame1, text="Last Name")
    last_name_label.grid(row=0, column=1)
    last_name_entry = ctk.CTkEntry(
        input_frame1,
        border_width=0,
        fg_color=WHITE_COLOR,
        text_color=BLACK_COLOR,
        placeholder_text_color=BLACK_COLOR,
    )
    last_name_entry.grid(row=1, column=1)

    password_label = ctk.CTkLabel(input_frame2, text="Password")
    password_label.grid(row=0, column=0)
    password_entry = ctk.CTkEntry(
        input_frame2,
        border_width=0,
        fg_color=WHITE_COLOR,
        text_color=BLACK_COLOR,
        placeholder_text_color=BLACK_COLOR,
        show='*'
    )
    password_entry.grid(row=1, column=0, padx=(0, 10))

    con_password_label = ctk.CTkLabel(input_frame2, text="Confirm Password")
    con_password_label.grid(row=0, column=1)
    con_password_entry = ctk.CTkEntry(
        input_frame2,
        border_width=0,
        fg_color=WHITE_COLOR,
        text_color=BLACK_COLOR,
        placeholder_text_color=BLACK_COLOR,
        show='*'
    )
    con_password_entry.grid(row=1, column=1)

    button = ctk.CTkButton(form_frame, width=100, fg_color=WHITE_COLOR)
    button.grid(row=3, column=0, padx=(0, 2), pady=(0, 2))
    button = ctk.CTkButton(
        form_frame,
        text="Submit",
        width=100,
        fg_color=BLACK_COLOR,
        text_color=WHITE_COLOR,
        hover_color="gray",
        corner_radius=5,
        command=lambda: event_listener('click')
    )
    button.grid(row=3, column=0, pady=(10, 10))

    root.mainloop()
