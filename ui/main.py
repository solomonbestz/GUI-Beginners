from settings import *



def load_image(image_path, size: tuple=(20, 20)):
    img = ctk.CTkImage(Image.open(image_path), size=size )
    return img


def switch_frames(event):
    home_btn.configure(fg_color=SIDE_FRAME if event == "home" else "transparent")
    setting_btn.configure(fg_color=SIDE_FRAME if event == "settings" else "transparent")

    if event == 'home':
        setting_page.grid_remove()
        home_page.grid(padx=(50, 50), sticky='we')
    elif event == 'settings':
        home_page.grid_remove()
        setting_page.grid(padx=(50, 50), sticky='we')

        

if __name__=='__main__':
    # Height = 600, width = 600
    
    root = ctk.CTk()
    root.title('Foodie')
    root.iconbitmap('icons/logo.ico')
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
    home_btn = ctk.CTkButton(master=menu_frame, image=load_image('icons/home.png'), width=40, corner_radius=0, text='', hover_color=HOVER, command=lambda: switch_frames('home'))
    home_btn.grid(row = 0, column=0, ipadx = 5, pady=(25, 0))
    setting_btn = ctk.CTkButton(master=menu_frame, image=load_image('icons/settings.png'), fg_color=MENU_FRAME, hover_color=HOVER, width=40, corner_radius=0, text='', command=lambda: switch_frames('settings'))
    setting_btn.grid(row = 1, column=0, ipadx = 5, pady=(10, 0))


    # >>>>>>>>>>>>>>>>> ADD PAGES UNDER THE MAIN FRAME

    home_page = ctk.CTkFrame(master=main_frame, width=300, height=400, fg_color='green', corner_radius=0, border_width=0)
    home_page.grid( padx=(50, 50), sticky='we')
    
    
    setting_page = ctk.CTkFrame(master=main_frame, width=300, height=400, fg_color='red', corner_radius=0, border_width=0)
    
    switch_frames('home')

    # >>>>>>>>>>>>>>>>>> HOME PAGE CONFIGURATION
    home_page.columnconfigure((0, 1, 2), weight=1)

    # >>>>>>>>>>>>>>>>>> ADD CARDS UNDER THE HOME PAGE



    card1 = ctk.CTkFrame(master=home_page, width=100, height=200, fg_color='pink')
    card1.grid(row = 0, column = 0, sticky='nswe')

    card1_img = ctk.CTkLabel(master=card1, image=load_image('images/card1.jpg', (100, 100)), text='', width=100, height=100)
    card1_img.grid(row = 0, column = 0, columnspan = 2, sticky='nswe')
    card1_desc = ctk.CTkLabel(master=card1, text='Fried Rice', width=100, height=25)
    card1_desc.grid(row = 1, column = 0, columnspan = 2, sticky='nswe')
    card1_view = ctk.CTkButton(master=card1, text='View', compound="left", width=50, height=25)
    card1_view.grid(row = 2, column = 0)
    card1_add_cart = ctk.CTkButton(master=card1, text='Add', compound="left", width=50, height=25)
    card1_add_cart.grid(row = 2, column = 1)

    card1.rowconfigure((0, 1, 2), weight=1)
    card1.columnconfigure(0, weight=1)


    card2 = ctk.CTkFrame(master=home_page, width=100, height=200, fg_color='violet', corner_radius=0, border_width=0)
    card2.grid(row = 0, column = 1, sticky='nswe')
    card3 = ctk.CTkFrame(master=home_page, width=100, height=200, fg_color='blue', corner_radius=0, border_width=0)
    card3.grid(row = 0, column = 2, sticky='nswe')
    card4 = ctk.CTkFrame(master=home_page, width=100, height=200, fg_color='brown', corner_radius=0, border_width=0)
    card4.grid(row = 1, column = 0, sticky='nswe')
    card5 = ctk.CTkFrame(master=home_page, width=100, height=200, fg_color='yellow', corner_radius=0, border_width=0)
    card5.grid(row = 1, column = 1, sticky='nswe')
    card6 = ctk.CTkFrame(master=home_page, width=100, height=200, fg_color='white', corner_radius=0, border_width=0)
    card6.grid(row = 1, column = 2, sticky='nswe')




    # >>>>>>>>> CONFIGURE MAIN FRAME
    main_frame.columnconfigure(0, weight=1)
    main_frame.rowconfigure(0, weight=1)



    root.mainloop()