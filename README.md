# Amazon-PriceDrop
Track an Amazon product price and receive a notification -- Python

<img src="https://lucasgigliozzi.com/wp-content/uploads/2019/11/amazonpricedrop-768x507.png " width="700" height="450" />

### Description: 
The Amazon Price Drop application tracks a user inputted product available on Amazon by checking the price of the product every x amount of minutes, where x is a value inputted by the user. If the price drops below its original price, then the application sends a text message to notify the user.

### Languages/Libraries/Frameworks:
Python, tkinter, Twilio, unittest

### Explanation:
While this is a very simple application, I decided to create it in part due to its practical use case, but also because I added an extra challenge for myself during development — namely, that I would utilize software engineering best practices. For example, I strove to create extremely clean and well commented code — perhaps too many comments… if such a thing is possible. Also, since the application was made in Python, I used object oriented design principles by creating objects for reusable sections of my code. To top it all off, I created unit tests for testing the main functions of the application, such as the product API requests and setting user inputted values from text entry boxes. All in all, while the application is simple in scope, the real learning experience was the software engineering best practices that went into its development.

### How it works: 
The application calls a third party Amazon API to retrieve details about the product the user entered, such as the name and price. The user must also input their phone number. With this number an instance of the client object is created from Twilio (a cloud communication API). When the user enters the time interval, this sets how often the application will call the Amazon API to determine if the price of the product is lower than when it was first called. If it was lower, then an instance of the Twilio client object is used to create a message which is sent to the users phone number. The interface is made using the Python library tkinter. 

![commentedcode](https://lucasgigliozzi.com/wp-content/uploads/2019/11/commentedcode-768x425.png)

Portion of commented code


![unittests](https://i.gyazo.com/b79ff6786584ae6ec2397f402d94f41a.png)

Some unit tests are shown above
