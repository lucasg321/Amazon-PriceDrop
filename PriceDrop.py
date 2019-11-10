import urllib.request
import json
import collections
import time
import hashlib
import hmac
import tkinter as tk
import requests
import threading 
from PIL import ImageTk, Image
import os
from twilio.rest import Client

win = tk.Tk() #create the frame/gui of the application with tkinter, set its name and size
win.title("Amazon Price Drop")
win.geometry("880x550")

frame1 = tk.Frame(win) #instantiating frames for the tkinter toolkit -- a frame is a section of the GUI window
frame2 = tk.Frame(win)
frame3 = tk.Frame(win)
frame4 = tk.Frame(win)
frame5 = tk.Frame(win)
frame6 = tk.Frame(win)
frame7 = tk.Frame(win)

frame1.grid(column = 0, row = 0) #declaring the position of the frames/sections of the window so that textboxes, buttons, etc. can be made inside them
frame2.grid(column = 0, row = 1)
frame3.grid(column = 0, row = 2)
frame4.grid(column = 0, row = 3)
frame5.grid(column = 0, row = 4)
frame6.grid(column = 0, row = 5)
frame7.grid(column = 0, row = 6)

previous_price = 0 #small number so first compare is always false, then this variable is set to current price
phone_num = 0
asin = "0"

#sets phone number variable to users choice
def phone_number():
    global phone_num
    phone_num = str(phone_entry.get()) #take the users inputted phone number

#utilize twilio to send a text to the user defined phone number
def send_twilio():
    account_sid = ""
    auth_token = ""
    client = Client(account_sid, auth_token) #make an instance of Client from twilio 
    client.messages.create(to=phone_num, from_="+12038836650", body="Your products price has dropped!") #define phone numbers and create a new message in Client object
    return client

def set_asin_real():
       global asin
       asin = str(asinentry.get()) #setting the asin that will be used to query the API, to the user input in textbox
       set_asin(asin)
       return asin

  #call the api with the user entered asin number of their chosen product, it also compares previous price and current price to determine if it should call the twilio function
def set_asin(asin1):

    url = "https://amazon-price1.p.rapidapi.com/priceReport"

    querystring = {"asin":asin1,"marketplace":"CA"} #asin user entered is being used to call the API

    headers = { #prepare the hedars to be included in the API call
    'x-rapidapi-host': "amazon-price1.p.rapidapi.com",
    'x-rapidapi-key': ""
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json() #receiving the response after calling the aamzon api and making sure its in json format
    print(response)

    current_price = int(response["prices"]["priceNew"]) #set current_price to the price received from API

    global previous_price  #allows access and modify the global variable previous_price from within this function

    if(current_price < previous_price):    #comparing the current and previous price, if current price is lower it sends the user a notification via twilio
        send_twilio()
        print("twilio activated")

    previous_price = int(response["prices"]["priceNew"])

    #this label will display the name of the current item
    label4.config(text = ""+ str(response["title"]))

    #this label will display text of the current price of the item
    label3.config(text = "The current price is: "+ str(response["prices"]["priceNew"]))

    return response["title"]

#the function thread that is continually called based on the user's input interval which will call set_asin() to check the price
def check_price():
    time_interval_seconds = 1
    if (time_entry.get()):
     time_interval = int(time_entry.get()) #retreive the entered time to continually check
     time_interval_seconds = time_interval*60 #turn the interval from minutes into seconds

    threading.Timer(time_interval_seconds, check_price).start() #calls itself every time interval set by user
    set_asin(asin) # calls the set_asin function to check the price
    
#display the logo
img = ImageTk.PhotoImage(Image.open("amazonlogo.png"))
panel = tk.Label(frame1, image = img)
panel.pack()

#first label text telling user to input asin of the product
label1 = tk.Label(frame4, text = "       Enter the asin number of the Amazon product that you would like to track (the asin can be found in the products description on Amazon)." , font=("Times New Roman", 12))
label1.pack()

#entry box for the asin user input
asinentry = tk.Entry(frame4)
asinentry.pack()

#this button calls the api with the text input from the textbox which should be a valid asin (if not the api will return an error which is displayed)
begintracking = tk.Button(frame4, text = "Search Product", command = set_asin_real)
begintracking.pack()

#this label prompts the user to enter a time interval
label1 = tk.Label(frame6, text = "Please enter the interval of time you would like to check for price changes (in minutes).", font=("Times New Roman", 12))
label1.pack()

#entry box for time interval
time_entry = tk.Entry(frame6)
time_entry.pack()

#this button will set the time limit that the program should continually check for price changes
check_time = tk.Button(frame6, text = "Set Time Interval", command = check_price)
check_time.pack()

#this label prompts the user to enter a time interval
label1 = tk.Label(frame1, text = "Please enter the phone number you would like to receive the text message on. (Use the follwing format: +1'phone number')", font=("Times New Roman", 12))
label1.pack()

#entry box for phone number
phone_entry = tk.Entry(frame2)
phone_entry.pack()

#this button will take in the users phone number
input_phone = tk.Button(frame3, text = "Set Phone Number", command = phone_number)
input_phone.pack()

label5 = tk.Label(frame7, text = "Product Details", font=("Helvetica", 16)) #create space
label5.pack()

label6 = tk.Label(frame7, text = " ", font=("Times New Roman", 20)) #create space
label6.pack()

#blank frame to be updated later on -- button click to display product name
label4 = tk.Label(frame7, text = "", font=("Times New Roman", 16))
label4.pack()

label7 = tk.Label(frame7, text = " ", font=("Times New Roman", 16)) #create space
label7.pack()

#blank frame to be updated later on -- button click to display current price
label3 = tk.Label(frame7, text = "", font=("Times New Roman", 14))
label3.pack()

win.mainloop() #main loop for tkinter gui