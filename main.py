import tkinter as tk
from tkinter import ttk

class EcommerceWebsite:
    def __init__(self, master):
        self.master = master
        self.master.title("Ecommerce Website")
        self.master.geometry("900x600")  # Adjust size as needed
        
        self.create_cover_page()

    def create_cover_page(self):
        # Top bar with rounded buttons
        top_bar = tk.Frame(self.master, bg="#007bff")
        top_bar.pack(side="top", fill="x")

        # Hamburger icon
        self.hamburger_icon = tk.Label(top_bar, text="\u2630", font=("Arial", 12), bg="#007bff", fg="white", padx=10, pady=10)
        self.hamburger_icon.pack(side="left", padx=10, pady=10)
        self.hamburger_icon.bind("<Button-1>", self.toggle_menu)

        # Phonekart label
        phonekart_label = tk.Label(top_bar, text="PhoneKart", font=("Riona Sans Bold Italic", 14), bg="#007bff", fg="white", padx=10, pady=5)
        phonekart_label.pack(side="left", padx=10, pady=10)
        login_button = tk.Button(top_bar, text="Login", font=("Arial", 12), bg="#007bff", fg="white", padx=10, pady=5, relief="flat")
        login_button.pack(side="right", padx=10, pady=10)

        # Home button
        home_button = tk.Button(top_bar, text="Home", font=("Arial", 12), bg="#007bff", fg="white", padx=10, pady=5, relief="flat")
        home_button.pack(side="right", padx=10, pady=10)

        # Become a Seller
        home_button = tk.Button(top_bar, text="Become a Seller", font=("Arial", 12), bg="#007bff", fg="white", padx=10, pady=5, relief="flat")
        home_button.pack(side="right", padx=10, pady=10)

        # Search bar with rounded edges
        search_frame = ttk.Frame(top_bar)
        search_frame.pack(side="left", padx=200, pady=10)

        search_entry = ttk.Entry(search_frame, width=20, font=("Arial", 12))
        search_entry.grid(row=0, column=0, padx=5, pady=5)

        search_button = ttk.Button(search_frame, text="Search", style="TButton")
        search_button.grid(row=0, column=1, padx=5, pady=5)

          # Toggle menu
        self.menu_frame = None  # Placeholder for menu frame
        self.menu_visible = False

    def toggle_menu(self, event=None):
        if self.menu_visible:
            self.slide_out_menu()
        else:
            self.slide_in_menu()

    def slide_in_menu(self):
        if not self.menu_frame:
            self.menu_frame = tk.Frame(self.master, bg="white", width=0)
            menu_options = ["My Account", "Saved Address", "PhoneKart Coins","My Orders","Download App"]
            for option in menu_options:
                menu_label = tk.Label(self.menu_frame, text=option, font=("Arial", 12), bg="white", fg="#333333", padx=10, pady=5)
                menu_label.pack(fill="x", padx=2, pady=2)
            self.menu_frame.place(relx=0, rely=0, relheight=1)
            self.menu_visible = True
            self.animate_slide_in()

    def animate_slide_in(self):
        width = 0
        while width < 200:  # Adjust width as needed
            self.menu_frame["width"] = width
            self.master.update_idletasks()
            width += 10  # Adjust speed of animation as needed
        self.menu_frame["width"] = 200  # Final width

    def slide_out_menu(self):
        if self.menu_frame:
            self.menu_frame.destroy()
            self.menu_frame = None
            self.menu_visible = False

    def check_click_outside_menu(self, event):
        if self.menu_visible:
            x = event.x_root
            y = event.y_root
            menu_x = self.master.winfo_rootx()
            menu_y = self.master.winfo_rooty()
            menu_width = self.menu_frame.winfo_width()
            if x < menu_x or x > menu_x + menu_width or y < menu_y:
                self.slide_out_menu()

    def round_corners(self, event):
        width = event.width
        height = event.height
        self.master.geometry(f"{width}x{height}+{self.master.winfo_x()}+{self.master.winfo_y()}")
        self.master.update_idletasks()
        self.master.overrideredirect(1)
        self.master.overrideredirect(0)

def main():
    root = tk.Tk()
    app = EcommerceWebsite(root)
    root.bind("<Button-1>", app.check_click_outside_menu)
    root.mainloop()

if __name__ == "__main__":
    main()
