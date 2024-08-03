import tkinter as tk  # Import tkinter library for GUI
import requests  # Import requests library for making HTTP requests

def get_weather():
    city = entry_city.get()  # Retrieve city name entered by user
    api_key = "8aafa6c24bd08812b8126b654e753d8a"  # Replace with your actual API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    response = requests.get(url)  # Send GET request to OpenWeatherMap API
    data = response.json()  # Parse JSON response into Python dictionary
    if data["cod"] == 200:
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        result_text = f"Description: {weather_description}\nTemperature: {temperature}°C\nHumidity: {humidity}%"
    else:
        result_text = "City not found."
    label_result.config(text=result_text)  # Update result label with weather information

root = tk.Tk()  # Create tkinter application window
root.title("Weather App")  # Set window title

label_city = tk.Label(root, text="Enter City:")  # Create label widget for city input
label_city.pack()  # Display label in window

entry_city = tk.Entry(root)  # Create entry widget for city input
entry_city.pack()  # Display entry widget in window

button_get_weather = tk.Button(root, text="Get Weather", command=get_weather)  # Create button to trigger weather retrieval
button_get_weather.pack()  # Display button in window

label_result = tk.Label(root, text="")  # Create label widget to display weather information
label_result.pack()  # Display label in window

root.mainloop()  # Start tkinter event loop
