# Sports Massage Excellence
Project of the web application designed to promote services of a massage therapist based in the area of Hertfordshire UK. Users of the website are able to book and pay for appointments online using STRIPE payment platform.

## Contents:book:
### UX:superhero_man:	
  * **Project Goals** :jigsaw:	
  * **Target Audience Goals** 	:dart:
  * **Site Owner Goals**  	:dart:
  * **User Requirements and Expectations** 	:dart:
  * **Design Choices** :framed_picture:
    * Fonts
    * Icons
    * Colours
  * **Wireframes** :straight_ruler:
  * **Models Structure** :straight_ruler:
  * **Features** :abacus:	
    * Features that have been developed
    * Features that will be implemented in the future
  * **Technologies Used** :computer:	
    * Languages
    * Tools & Libraries
  * **Testing** :magnet:
  * **Bugs** :mosquito:
  * **Deployment** :surfer:
  * **Acknowledgements** :clap:


## UX ( User Experience)
### Project Goals :jigsaw:	
The goal of this project is to provide a massage therapist with his personal online presence where he could promote his services. Users of the website will be available to read information about a therapits and services provided, read a review from previous clients, schedule an appointment and pay for it using safe platfrom provided by STRIPE.

### User Goals :jigsaw: 
* Ability to set up an account
* Ability to log in and log out
* Ability to see available appointments
* Ability to pay for my booked appointment 
* Visual interaction and feedback
* Interact with the website on Desktop tablet and mobile

## User stories 	:dart:
### As a user I want to be able to...
* Register for an account
* Log in or log out from my account
* Have personalised user profile
* Receive an email confirmation after registering
* Recover my password in case I forget it
* Make a purchase without registering for an account

### As a customer I want to be able to...
* Make a purchase without registering for an account
* See available therapies
* See locations where I can get a treatment
* Read reviews about the services provided

### As a registered user I want to be able to...
* See a history of my purchases
* See a personalised profile
* Be able to see my aftercare advice
* Write a review
* Update my billing details

### As an admin I want to be able to...
* Update available therapies
* Write aftercare advice for my patients

## Site Owner Goals	:dart:

* Promote therapist in the local area
* Ability to sell services to online customers
* Maintain a databse of client profiles
* Offer discounts to registered users


## User Requirements and Expectations 	:dart:

* **Requirements**
  * Navigate the website using the menu buttons and drop down selector
  * Ability to use this application on mobile and desktop devices
  * Content displayed in a visually appealing manor
  
* **Expectations**
  * Content is visually satisfying and informative on all screen sizes
  * No information overload
  * Navigation takes user to specific parts of the website
  
## Design choices :framed_picture:	
  
**Fonts**

I chose to use the font **Noto Serif** as it was designed to make the web more beautiful across platforms for all languages. This font style is intended to be visually harmonious, with compatible heights and stroke thicknesses. It can be found [here](https://fonts.google.com/specimen/Noto+Serif?category=Serif,Sans+Serif,Display#standard-styles).

**Icons**

Icons used in this project come from [FontAwesome](https://fontawesome.com/).

**Colours**

Using learned knowledge from prior research, bright and vibrant colours have a higher influence in terms of positivity and therefore more potential interactions.
Link to a color palette made using **coolors.co** is [here](https://coolors.co/d8d4d5-03fcba-ee6352-008dd5-f0803c)

**Colours used**
![Color theme](https://github.com/bartosz-makowski/sme/blob/master/wireframes/sme-colour-palette.png)

## Wireframes :straight_ruler:
I built the wireframes for this project using <a href="https://balsamiq.com/">Balsamiq</a>. Started by doing a very basic wireframe for Mobile/Tablet/Desktop - these were to get a basic understanding of how structurally elements would appear on the page. Wireframes are placed in wireframes [folder](https://github.com/bartosz-makowski/sme/tree/master/wireframes) 

![Desktop view](https://github.com/bartosz-makowski/sme/blob/master/wireframes/sme-desktop.png)
![Tablet view](https://github.com/bartosz-makowski/sme/blob/master/wireframes/sme-tablet.png)
![Mobile view](https://github.com/bartosz-makowski/sme/blob/master/wireframes/sme-mobile.png)
![booking chart](https://github.com/bartosz-makowski/sme/blob/master/wireframes/sme-booking-flow.png)

## **Models Structure**


### **Treatments:**
Key      | Value
---------|-----------
name | models.CharField(max_length=254, blank=False,
description | models.TextField(blank=False)
image | models.ImageField(null=False, blank=False)
featured | models.BooleanField(default=False, null=True, blank=True)

### **Reviews:**
Key      | Value
---------|-----------
title | models.CharField((max_length=50, null=False, blank=False, default='Title')
description | models.TextField()
author | models.CharField(max_length=20, null=False, blank=True)
date | DateTimeField(auto_now_add=True)

### **Deals:**
Key      | Value
---------|-----------
name | models.CharField(max_length=65)
price | models.IntegerField(max_length=3)
description | models.TextField()
image | models.ImageField(null=True, blank=True)
featured | models.BooleanField(default=False, null=True, blank=True)

### **Order:**
Key      | Value
---------|-----------
order_number | models.CharField(max_length=32, null=False, editable=False)
full_name | models.CharField(max_length=50, null=False, blank=False)
email | models.EmailField(max_length=254, null=False, blank=False)
phone_number | models.CharField(max_length=20, null=True, blank=True)
town_or_city | models.CharField(max_length=40, null=True, blank=True)
postcode | models.CharField(max_length=20, null=True, blank=True)
street_address1 | models.CharField(max_length=80, null=True, blank=True)
street_address2 | models.CharField(max_length=80, null=True, blank=True)
date | models.DateTimeField(auto_now_add=True)
order_total | models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
stripe_pid | models.CharField(max_length=254, null=False, blank=False, default='')

### **Order:**
Key      | Value
---------|-----------
order | models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE)
product | models.ForeignKey(Deal, null=False, blank=False, on_delete=models.CASCADE)
quantity | models.IntegerField(null=False, blank=False, default=0)
lineitem_total | models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False, default=0)

### **Location:**
Key      | Value
---------|-----------
description | models.TextField()
image | image = models.ImageField(null=False, blank=False)


## Features :abacus:

**Features that have been developed:**
Featured deals and reviews are visible on home page
Ability to pay for deals using credit cards through Stripe
Adding deals and removing from the shopping basket



**Features to be implemented in the future**
Booking app to allow users to book appointments


## Technologies Used :computer:

### Languages
* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [JavaScript](https://www.w3schools.com/js/)
* [Python](https://www.python.org/)

### Tools & Libraries
* [DJango](https://docs.djangoproject.com/en/3.1/)
* [PopperJS](https://popper.js.org/)
* [jQuery](https://jquery.com/)
* [Git](https://git-scm.com/)
* [Bootstrap](https://getbootstrap.com/)
* [Google Fonts](https://fonts.google.com/)
* [FontAwesome](https://fontawesome.com/)
* [Balsamiq](https://balsamiq.com/)
* [AmIresponsive](http://ami.responsivedesign.is/) - used to generate multi screen view of the webiste on different devices
* [Milanote](https://milanote.com/)
* [Unsplash](https://unsplash.com/)


### Testing :magnet:

### Bugs :mosquito:
#### New user registration form issue :spider:
* **Issue:** 
* **Fix:** 

#### Google dev tools - empty div in the head issue at home page :ant:
* **Issue:** 
* **Fix:** 

### Deployment :surfer:

#### To deploy locally

#### To deploy your project on Heroku, use the following steps: 
    
#### Running Locally

### Acknowledgements :clap:

