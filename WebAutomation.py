import tkinter as tk
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# Initialize the web driver
driver = None

# Function to start the automation
def start_automation():
    global driver
    if driver is None:
        if len(site_link.get("1.0", "end-1c")) == 0 or len(site_username.get("1.0", "end-1c")) == 0 or site_pass.get("1.0", "end-1c") == 0:
            alertLabel.config(text='Please enter site link or username or password.')
            return
        
        alertLabel.config(text='')
        driver = webdriver.Chrome()
        driver.get(site_link.get("1.0", "end-1c"))
        time.sleep(1)
        username_input = driver.find_element(By.ID, 'email')
        password_input = driver.find_element(By.ID, 'pass')
        login_button = driver.find_element(By.NAME, 'login')
        username_input.send_keys('test@gmail.com')
        password_input.send_keys('test')
        login_button.click()
        status_label.config(text="Automation started")
        refresh_page()

# Function to stop the automation
def stop_automation():
    global driver
    if driver:
        driver.quit()
        driver = None
        status_label.config(text="Automation stopped")

# Function to periodically refresh the page
def refresh_page():
    while driver:
        time.sleep(5)
        driver.refresh()

# Create the main window
root = tk.Tk()
root.title("Website Automation")

# Create and configure widgets
start_button = tk.Button(root, text="Start Automation", command=start_automation)
stop_button = tk.Button(root, text="Stop Automation", command=stop_automation)
label_site_link = tk.Label(root, text="Site Link")
site_link = tk.Text(root,width=50,height=1)
label_username = tk.Label(root, text="Username")
site_username = tk.Text(root,width=50,height=1)
label_pass = tk.Label(root, text="Password")
site_pass = tk.Text(root,width=50,height=1)
status_label = tk.Label(root, text="Status: Idle")
alertLabel = tk.Label(root,fg='#f00')

# Place widgets in the window
label_site_link.pack()
site_link.pack(pady=10,padx=20)
label_username.pack()
site_username.pack(pady=10,padx=20)
label_pass.pack()
site_pass.pack(pady=10,padx=20)
alertLabel.pack(pady=10)
start_button.pack(pady=10)
stop_button.pack()
status_label.pack()

# Start the Tkinter main loop
root.mainloop()