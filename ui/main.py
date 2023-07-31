from settings import *



def load_image(image_path):
    img = ctk.CTkImage(Image.open(image_path))
    return img


def switch_frames(event):
    if event == 'home':
        setting_page.grid_remove()
        home_page.grid(padx=(50, 50), sticky='we')
    elif event == 'settings':
        home_page.grid_remove()
        setting_page.grid(padx=(50, 50), sticky='we')

        

if __name__=='__main__':
    ctk.set_appearance_mode('dark')
    # Height = 600, width = 600
    
    root = ctk.CTk()
    root.minsize(500, 400)
    root.maxsize(900, 600)


    # >>>>>>>>> CREATE FRAMES
    
    menu_frame = ctk.CTkFrame(master=root, width=50, height=500, fg_color=MENU_FRAME, corner_radius=0)
    menu_frame.grid(row = 0, column=0, sticky='nsew')
    side_frame = ctk.CTkFrame(master=root, width=150, height=500, fg_color=SIDE_FRAME, corner_radius=0, border_width=0)
    side_frame.grid(row = 0, column=1, sticky='nsew')
    main_frame = ctk.CTkFrame(master=root, width=400, height=500, fg_color=MAIN_FRAME, corner_radius=0, border_width=0)
    main_frame.grid(row = 0, column=2, sticky='nsew', padx=(0, 0))

    # >>>>>>>>> CONFIGURE FRAMES
    root.columnconfigure(2, weight=1)
    root.rowconfigure(0, weight=1)


    # >>>>>>>>>>> ADD BUTTONS TO OUR MENU FRAME
    home_btn = ctk.CTkButton(master=menu_frame, image=load_image('images/home.png'), fg_color=MENU_FRAME, hover_color=SIDE_FRAME, width=40, corner_radius=0, text='', command=lambda: switch_frames('home'))
    home_btn.grid(row = 0, column=0, ipadx = 5, pady=(25, 0))
    setting_btn = ctk.CTkButton(master=menu_frame, image=load_image('images/settings.png'), fg_color=MENU_FRAME, hover_color=SIDE_FRAME, width=40, corner_radius=0, text='', command=lambda: switch_frames('settings'))
    setting_btn.grid(row = 1, column=0, ipadx = 5, pady=(10, 0))


    # >>>>>>>>>>>>>>>>> ADD PAGES

    home_page = ctk.CTkFrame(master=main_frame, width=300, height=400, fg_color='green', corner_radius=0, border_width=0)
    home_page.grid( padx=(50, 50), sticky='we')

    setting_page = ctk.CTkFrame(master=main_frame, width=300, height=400, fg_color='red', corner_radius=0, border_width=0)
    

    # >>>>>>>>> CONFIGURE MAIN FRAME
    main_frame.columnconfigure(0, weight=1)
    main_frame.rowconfigure(0, weight=1)



    root.mainloop()