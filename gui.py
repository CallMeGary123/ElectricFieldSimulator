import tkinter as tk
import customtkinter as ctk
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import pycharge as pc

DEFAULT_SETTINGS = {
    "linthresh":1.01e6, 
    "linscale":1, 
    "vmin":-1e10, 
    "vmax":1e10,
    "lim" :20e-2,
    "npoints":1000,
    "radius":7.22e-2,
    "figsize":[15, 5] 
}

USER_SETTINGS = {
    "linthresh":1.01e6, 
    "linscale":1, 
    "vmin":-1e10, 
    "vmax":1e10,
    "lim" :20e-2,
    "npoints":1000,
    "radius":7.22e-2,
    "figsize":[15, 5] 
}

def CenterWindowToDisplay(Screen: ctk.CTk, width: int, height: int, scale_factor: float = 1.0):
    """Centers the window to the main display/monitor"""
    screen_width = Screen.winfo_screenwidth()
    screen_height = Screen.winfo_screenheight()
    x = int(((screen_width/2) - (width/2)) * scale_factor)
    y = int(((screen_height/2) - (height/2)) * scale_factor)
    return f"{width}x{height}+{x}+{y}"

def check_duplicate(coordinates,x,y):
    for charge in coordinates:
        if charge.get("X") == x and charge.get("Y") == y:
            return True
        else:
            return False
def clear_screen():
    global CHARGES
    CHARGES = []  # Reset CHARGES list
    listbox.config(listvariable=tk.Variable(window, CHARGES))
    canvas.delete("all")  # Clear the canvas
    canvas.create_oval(255.6, 255.6, 544.4, 544.4, width = 4)

def decide_marker(p):
    if p>0:
        return "$+$"
    elif p<0:
        return "$-$"
    else:
        return "$0$"
    
def run_sim():
    plt.rcParams['figure.figsize'] = USER_SETTINGS.get("figsize")
    source = []
    for charge in CHARGES:
        source.append(pc.StationaryCharge(position=(charge.get("X")*pow(10,-2), charge.get("Y")*pow(10,-2), 0), q=charge.get("q")))
    
    plt.rcParams['figure.figsize'] = USER_SETTINGS.get("figsize")

    simulation = pc.Simulation(source)

    # Create meshgrid in x-y plane between -10 m to 10 m at z=0
    lim = USER_SETTINGS.get("lim")
    npoints = USER_SETTINGS.get("npoints")  # Number of grid points
    coordinates = np.linspace(-lim, lim, npoints)  # grid from -lim to lim
    x, y, z = np.meshgrid(coordinates, coordinates, 0, indexing="xy")  # z=0

    # Calculate E field components at t=0
    E_x, E_y, E_z = simulation.calculate_E(t=0, x=x, y=y, z=z)
    # Plot E_x, E_y, and E_z fields
    E_x_plane = E_x[:, :, 0]  # Create 2D array at z=0 for plotting
    E_y_plane = E_y[:, :, 0]
    E_z_plane = E_z[:, :, 0]
    comb = np.sqrt(E_x_plane**2 + E_y_plane**2)

    # Create figs and axes, plot E components on log scale
    fig, axs = plt.subplots(1, 3, sharey=True)
    norm1 = mpl.colors.SymLogNorm(linthresh=USER_SETTINGS.get("linthresh"), linscale=USER_SETTINGS.get("linscale"), vmin=USER_SETTINGS.get("vmin"), vmax=USER_SETTINGS.get("vmax"))
    norm2 = mpl.colors.SymLogNorm(linthresh=USER_SETTINGS.get("linthresh"), linscale=USER_SETTINGS.get("linscale"), vmin=0, vmax=USER_SETTINGS.get("vmax"))
    extent = [-lim, lim, -lim, lim]
    plt.set_cmap("Spectral")
    im_0 = axs[0].imshow(E_x_plane, origin="lower", norm=norm1, extent=extent)
    im_1 = axs[1].imshow(E_y_plane, origin="lower", norm=norm1, extent=extent)
    im_2 = axs[2].imshow(comb, origin="lower", norm=norm2, extent=extent)

    xticks = np.arange(-20e-2, 25e-2, 0.1)
    axs[0].set_xticks(xticks)
    axs[1].set_xticks(xticks)
    axs[2].set_xticks(xticks)
    # Add labels

    axs[0].set_title("E_x")
    axs[1].set_title("E_y")
    axs[2].set_title("E_x-y")

    circle1 = plt.Circle((0, 0), 7.22e-2, fill=False)
    circle2 = plt.Circle((0, 0), 7.22e-2, fill=False)
    circle3 = plt.Circle((0, 0), 7.22e-2, fill=False)
    axs[0].add_patch(circle1)
    axs[1].add_patch(circle2)
    axs[2].add_patch(circle3)
    # Add point positions to plot
    for point in source:
        marker = decide_marker(point.q)
        axs[0].scatter(point.position[0], point.position[1], c="white", s=35,marker=marker)
        axs[1].scatter(point.position[0], point.position[1], c="white", s=35,marker=marker)
        axs[2].scatter(point.position[0], point.position[1], c="white", s=35,marker=marker)


    # Add colorbar to figure
    Ecax0 = inset_axes(
        axs[0],
        width="6%",
        height="100%",
        loc="lower left",
        bbox_to_anchor=(1.05, 0.0, 1, 1),
        bbox_transform=axs[0].transAxes,
        borderpad=0,
    )

    Ecax1 = inset_axes(
        axs[1],
        width="6%",
        height="100%",
        loc="lower left",
        bbox_to_anchor=(1.05, 0.0, 1, 1),
        bbox_transform=axs[1].transAxes,
        borderpad=0,
    )
    Ecax2 = inset_axes(
        axs[2],
        width="6%",
        height="100%",
        loc="lower left",
        bbox_to_anchor=(1.05, 0.0, 1, 1),
        bbox_transform=axs[2].transAxes,
        borderpad=0,
    )

    plt.colorbar(im_0, ax=axs[0], label="E (N/C)", cax=Ecax0)
    plt.colorbar(im_1, ax=axs[1], label="E (N/C)", cax=Ecax1)
    plt.colorbar(im_2, ax=axs[2], label="E (N/C)", cax=Ecax2)

    plt.subplots_adjust(wspace=0.4)

    plt.show()
  
"""
def display_coordinates(event):
    global CHARGES
    x, y = event.x / 40, (canvas.winfo_reqheight() - event.y) / 40
    add_window()
    CHARGES.append({"X": x,"Y": y,"q": -1})
    canvas.create_oval(event.x-5, event.y-5, event.x+5, event.y+5, fill='black')
    listbox.config(listvariable=tk.Variable(window, CHARGES))
"""
def add_window():

    def save():
        x = float(x_entry.get())
        y = float(y_entry.get()) 
        q = float(q_entry.get())
        if check_duplicate(CHARGES,x,y) is True:
            tk.messagebox.showerror('Duplicate Error', 'Error: A charge already exists at this coordinates!\nchnage coordinates or edit/delete the existing charge')
        else:
            CHARGES.append({"X": x,"Y": y,"q": q})
            listbox.config(listvariable=tk.Variable(window, CHARGES))
            center_x = canvas.winfo_reqwidth() / 2
            center_y = canvas.winfo_reqheight() / 2
            canvas.create_oval((x*20) + center_x - 5, center_y - (y*20) + 5, (x*20) + center_x + 5, center_y - (y*20) - 5,fill="black")
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

    y_frame =  ctk.CTkFrame(info_frame, width=100, height=75, bg_color="transparent")
    y_frame.pack(anchor="center", padx=5, pady=5,fill = "both",side="left")
    y_frame.pack_propagate(0)

    q_frame =  ctk.CTkFrame(info_frame, width=100, height=75, bg_color="transparent")
    q_frame.pack(anchor="center", padx=5, pady=5,fill = "both", side="left")   
    q_frame.pack_propagate(0)

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
        placeholder_text="C",
        bg_color="transparent"
    )
    q_entry.pack(anchor="s", padx=5, pady=5,fill = "both")
    
window = ctk.CTk()
ctk.set_appearance_mode("light")
window.title('Charges')
window.geometry(CenterWindowToDisplay(window, 980, 660, window._get_window_scaling()))
window.resizable(False, False)

CHARGES = []

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


title = ctk.CTkLabel(
    app_title_frame, font=("Segoe UI Semibold", 25), text="Electric Field Simulator"
)
title.place(relx=0.5, rely=0.5, anchor="center")
# Create a canvas and bind the mouse click event
canvas = tk.Canvas(display_frame, width=796, height=796, background='white')
"""def get_mouse_coordinates(event):
    x = event.x - canvas.winfo_width() // 2
    y = canvas.winfo_height() // 2 - event.y 
    print(f"Mouse coordinates (centered): x = {x}, y = {y}")

canvas.bind('<Button-1>', get_mouse_coordinates)"""
canvas.pack(padx=5, pady=5)
canvas.create_oval(255.6, 255.6, 544.4, 544.4, width = 4)
listbox = tk.Listbox(
    charge_list_frame,
    listvariable=tk.Variable(window, CHARGES),
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

run = ctk.CTkButton(buttons_list_frame,font=("Segoe UI Semibold", 15), text="Run",command=run_sim)
run.pack(side="bottom",padx=5, pady=5, fill="both")

clear = ctk.CTkButton(buttons_list_frame,font=("Segoe UI Semibold", 15), command=clear_screen, text="Clear All")
clear.pack(side="top", padx=5, pady=5, fill="both")



# Start the main event loop
window.mainloop()