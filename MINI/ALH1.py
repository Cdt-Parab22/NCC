import tkinter as tk
from tkinter import ttk
import speedtest
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def test_internet_speed():
    """Function to test internet speed and display results."""
    st = speedtest.Speedtest()
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    ping = st.results.ping

    # Update labels with speed test results
    download_label.config(text=f"Download Speed: {download_speed:.2f} Mbps")
    upload_label.config(text=f"Upload Speed: {upload_speed:.2f} Mbps")
    ping_label.config(text=f"Ping: {ping} ms")

    # Plotting speed test results
    fig, ax = plt.subplots()
    ax.bar(["Download", "Upload"], [download_speed, upload_speed], color=['blue', 'green'])
    ax.set_ylabel("Speed (Mbps)")
    ax.set_title("Internet Speed Test")
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Creating the main application window
root = tk.Tk()
root.title("Internet Speed Test App")

# Title label
title_label = tk.Label(root, text="Internet Speed Test", font=("Helvetica", 20))
title_label.pack(pady=20)

# Button to start speed test
test_button = ttk.Button(root, text="Test Speed", command=test_internet_speed)
test_button.pack(pady=10)

# Labels to display speed test results
download_label = tk.Label(root, text="", font=("Helvetica", 20))
download_label.pack(pady=5)

upload_label = tk.Label(root, text="", font=("Helvetica", 20))
upload_label.pack(pady=5)

ping_label = tk.Label(root, text="", font=("Helvetica", 20))
ping_label.pack(pady=5)

root.mainloop()
