import tkinter as tk
import customtkinter as ctk


def CenterWindowToDisplay(Screen: ctk.CTk, width: int, height: int, scale_factor: float = 1.0):
    """Centers the window to the main display/monitor"""
    screen_width = Screen.winfo_screenwidth()
    screen_height = Screen.winfo_screenheight()
    x = int(((screen_width/2) - (width/2)) * scale_factor)
    y = int(((screen_height/2) - (height/2)) * scale_factor)
    return f"{width}x{height}+{x}+{y}"


def clear_screen():
    global COORDINATES
    COORDINATES = []  # Reset COORDINATES list
    listbox.config(listvariable=tk.Variable(window, COORDINATES))
    canvas.delete("all")  # Clear the canvas
    canvas.create_oval(111.2, 111.2, 688.8, 688.8, width = 4)
    
"""
def display_coordinates(event):
    global COORDINATES
    x, y = event.x / 40, (canvas.winfo_reqheight() - event.y) / 40
    add_window()
    COORDINATES.append({"X": x,"Y": y,"q": -1})
    canvas.create_oval(event.x-5, event.y-5, event.x+5, event.y+5, fill='black')
    listbox.config(listvariable=tk.Variable(window, COORDINATES))
"""
def add_window():

    def save():
        x = float(x_entry.get())
        y = float(y_entry.get()) 
        q = float(q_entry.get())
        COORDINATES.append({"X": x,"Y": y,"q": q})
        listbox.config(listvariable=tk.Variable(window, COORDINATES))
        canvas.create_oval(x*40-5, -y*40+canvas.winfo_reqheight()-5, x*40+5, -y*40+canvas.winfo_reqheight()+5, fill='black')
        add_window.destroy()

    add_window = ctk.CTkToplevel(window)
    add_window.title("Adding new stationary charge")
    add_window.geometry(CenterWindowToDisplay(window, 340, 150, window._get_window_scaling()))
    add_window.resizable(False, False)
    add_window.grab_set()

    info_frame = ctk.CTkFrame(add_window, width=300, height=100, bg_color="transparent")
    info_frame.pack(anchor="center", padx=5, pady=5,fill = "both")

    button_frame = ctk.CTkFrame(add_window, width=300, height=40, bg_color="transparent")
    button_frame.pack(anchor="center", padx=5, pady=5,fill = "both")
    button_frame.pack_propagate(0)

    save_button = ctk.CTkButton(button_frame, font=("Segoe UI Semibold", 15), text="Save", command=save)
    save_button.pack(fill="both", expand=True, anchor="s", padx=5, pady=5)

    x_frame =  ctk.CTkFrame(info_frame, width=100, height=75, bg_color="transparent")
    x_frame.pack(anchor="center", padx=5, pady=5,fill = "both", side="left")
    x_frame.pack_propagate(0)

    q_frame =  ctk.CTkFrame(info_frame, width=100, height=75, bg_color="transparent")
    q_frame.pack(anchor="center", padx=5, pady=5,fill = "both", side="right")   
    q_frame.pack_propagate(0)

    y_frame =  ctk.CTkFrame(info_frame, width=100, height=75, bg_color="transparent")
    y_frame.pack(anchor="center", padx=5, pady=5,fill = "both",side="right")
    y_frame.pack_propagate(0)


    x_label = ctk.CTkLabel(
        x_frame,
        font=("Segoe UI Semibold", 14),
        text="↓ X ↓",
        bg_color="transparent",
    )
    x_label.pack(anchor="s", padx=5, pady=5,fill = "both")

    x_entry = ctk.CTkEntry(
        x_frame,
        font=("Segoe UI Semibold", 16),
        justify="center",
        placeholder_text="cm",
        bg_color="transparent"
    )
    x_entry.pack(anchor="s", padx=5, pady=5,fill = "both")

    y_label = ctk.CTkLabel(
        y_frame,
        font=("Segoe UI Semibold", 14),
        text="↓ Y ↓",
        bg_color="transparent",
    )
    y_label.pack(anchor="s", padx=5, pady=5,fill = "both")

    y_entry = ctk.CTkEntry(
        y_frame,
        font=("Segoe UI Semibold", 16),
        justify="center",
        placeholder_text="cm",
        bg_color="transparent"
    )
    y_entry.pack(anchor="s", padx=5, pady=5,fill = "both")

    q_label = ctk.CTkLabel(
        q_frame,
        font=("Segoe UI Semibold", 14),
        text="↓ q ↓",
        bg_color="transparent",
    )
    q_label.pack(anchor="s", padx=5, pady=5,fill = "both")

    q_entry = ctk.CTkEntry(
        q_frame,
        font=("Segoe UI Semibold", 16),
        justify="center",
        placeholder_text="cm",
        bg_color="transparent"
    )
    q_entry.pack(anchor="s", padx=5, pady=5,fill = "both")
window = ctk.CTk()
ctk.set_appearance_mode("light")
window.title('Charges')
window.geometry(CenterWindowToDisplay(window, 980, 660, window._get_window_scaling()))
window.resizable(False, False)

COORDINATES = []

app_util_frame = ctk.CTkFrame(window, width=300, height=640, bg_color="transparent")
app_util_frame.pack(padx=5, pady=5, side="right", fill = "both")

app_title_frame = ctk.CTkFrame(app_util_frame, width=300, height=80, bg_color="transparent")
app_title_frame.pack(anchor="center", padx=5, pady=5,fill = "both")

charge_list_frame = ctk.CTkFrame(app_util_frame, width=300, height=410, bg_color="transparent")
charge_list_frame.pack(anchor="center", padx=5, pady=5,fill = "both",expand=True)

buttons_list_frame = ctk.CTkFrame(app_util_frame, width=300, height=160, bg_color="transparent")
buttons_list_frame.pack(anchor="center",side = "bottom", padx=5, pady=3,fill = "both")

display_frame = ctk.CTkFrame(window, width=650, height=650, bg_color="transparent")
display_frame.pack(padx=5, pady=5, side="left",fill = "both",expand=True)


# Create a canvas and bind the mouse click event
canvas = tk.Canvas(display_frame, width=800, height=800, background='white')
#canvas.bind('<Button-1>', display_coordinates)
canvas.pack(padx=5, pady=5)
canvas.create_oval(111.2, 111.2, 688.8, 688.8, width = 4)
listbox = tk.Listbox(
    charge_list_frame,
    listvariable=tk.Variable(window, COORDINATES),
    font=("Segoe UI Semibold", 14),
    selectbackground="#0084d0",
    background="#cfcfcf",
    relief="flat"
)
#listbox.bind("<Double-1>", conatct_window)
listbox.pack(side="left", fill="both", expand=True, padx=5, pady=5)
scroll = ctk.CTkScrollbar(
    charge_list_frame,
    orientation="vertical",
    button_color=("#3B8ED0", "#1F6AA5"),
    button_hover_color=("#36719F", "#144870"),
    command=listbox.yview,
)
listbox.config(yscrollcommand = scroll.set)
scroll.pack(fill="y", expand=True, pady=5)

# Create a button to run the convex hull computation
add = ctk.CTkButton(buttons_list_frame,font=("Segoe UI Semibold", 15), text="Add",command=add_window)
add.pack(side="top", padx=5, pady=5, fill="both")

run = ctk.CTkButton(buttons_list_frame,font=("Segoe UI Semibold", 15), text="Run")
run.pack(side="bottom",padx=5, pady=5, fill="both")

clear = ctk.CTkButton(buttons_list_frame,font=("Segoe UI Semibold", 15), command=clear_screen, text="Clear")
clear.pack(side="top", padx=5, pady=5, fill="both")



# Start the main event loop
window.mainloop()