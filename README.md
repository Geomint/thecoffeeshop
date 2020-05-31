# The Coffee Shop ☕️

<img src=""></img>
** insert device screenshot **

<p>Welcome to The Coffee Shop☕️ this e-commerce website was developed by George Pyott as the final milestone project on the Code Institute Full-Stack web developer course. This website is aimed at users who wish to purchase a wide variety of different coffee flavours, blends and grinds that are available. If you would like to reach out to me please use my GitHub contact details.</p>

## Contents: 

- UX 👍
    - Project Goals
    - Target Audience Goals
    - Site Owner Goals
    - User Stories
    - User Requirements and Expectations
- Design Choices 🎨
    - Fonts
    - Icons
    - Colours
    - Styling
    - Images
    - Backgrounds
- Planning✏️
- Wireframes 🔧
    - Website Layout
    - Account Creation Flowchart
    - Database Design
- Features 🎡
    - Features that have been developed
    - Features that will be implemented in the future
- Technologies Used 👨‍💻
- Planning + Testing: ✏️ 🔌
- Bugs 🐞
- Deployment 🚀
	- Deploying to Heroku
    - Locally run this project
- Credits 💳
- Disclaimer

## User Experience: 👍

### Project Goals:
<p>The goal of this project is to offer a wide range of coffee products be it ground coffee, coffee beans or even products & merchandise. The users on the website will be able to create an account, add any combination of items
to a shopping basket, make payments and have their orders viewable on their profile dashboard panel.</p>

### Target Audience Goals:

* Browse various coffee products and be offered information about that product.
* Purchase products shown on the webstore.
* Create an account to track orders and purchase items on the webstore.
* A visually appealing and intuitive design.
* A website that is navigable on any device (mobile/tablet/desktop).
* Track orders made via profile dashboard.

### Site Owner Goals:

* Provide users with a safe and secure e-commerce platform in order to generate revenue from sales.
* Encourage user sales with promotions and discounts.
* Build awareness for the brand and attract coffee suppliers.
* Collect user session data for market research purposes.

### User Stories:

<p>Tim Says: "Ive been looking for a website for a while now that works just as well on my phone as it does my laptop, im far too busy to be sitting at my computer all day 
so I need a site that I can use just as well on my phone."</p>

<p>Mark Says: "Im often skeptical of purchasing on online sites, I like to know that I have a line of communication with the company im paying with just incase there would be an issue
at some point down the line with the order."</p>

<p>Gabe Says: "Shopping on an e-commerce website has got to be easy, if you flood the user with too much choice you can cause them to panic and potentially leave the site and go elsewhere,
make it easy for the user to choose which items they want and buy them, simple!"</p>

### User Requirements and Expectations:
<p>When it comes to shopping on the web, users need to feel safe & comfortable in order for them to actually go through with purchases online, therefore providing the best UX, proper authentication
and using secure payment gateways (in this case Stripe) is necessary to offer the best solution.</p>

#### Requirements:

* Interact with a visually appealing and intuitive website.
* Navigate the website on any device, with ease.
* Consume information about various coffee types and about the brand.
* Add products to a shopping cart & update the cart quantities.
* Purchase products in the shopping cart in a safe and secure way.
* View orders in profile dashboard section.
* Can reach out to the business via email if needed.

#### Expectations:

* The Website will ensure safe storage of user details.
* The users payment information will not be stored in the website's database.
* The Website will load with sufficient speed.
* The Content on the website will be dynamic for any device.
* The Website will be navigable with ease.

## Design Choices: 🎨
<p>I wanted the design of this website to reflect the rustic feel of a family run coffee shop, the pastel colours and various brown colours compliment the imagery used across the site.</p>

### Fonts:

<p>I chose to use Montserrat as the main font family for this website as it provides an elegant & clean style for text and titles. In the essence of keeping the layout clean to encourage user sales, I decided to go with this font.</p>

### Icons:

<p>Thanks to the excellent collection of icons over at font-awesome, selecting icons to use for The Coffee Shop was really simple, I decided to go with typical icons for the 'icon-navigation' section of the navbar, the cart, the user icon and the burger button, as well as using various other intutitive icons across the project. I use icons in place of link text across the site where possible to provide the best UX possible to the user.</p>

### Colours:
<p>The colours I chose to use for this website compliment the rustic tones of a coffee shop, having a visually appealing contrast provides a more elegant user experience for those on the website, below is the list of colours the website uses.</p>

- ![#b2e4c8](https://placehold.it/15/b2e4c8/000000?text=+) Primary: #b2e4c8; "Fringy Flower" - This pastel green colour provides an elegant & efficient contrast for the strong brown colour.
- ![#58493c](https://placehold.it/15/58493c/000000?text=+) Secondary: #58493c; "Kabul" - This strong brown colour is used across the site in the layout, for instance the header and footer, this defines the page well and indicates where the user focus should be.
- ![#f1e2d0](https://placehold.it/15/f1e2d0/000000?text=+) Tertiary: #f1e2d0; "Almond" - This lighter brown colour provides a subtle alternative to the stronger brown and can be used to highlight various elements within the website. 
- ![#ffffff](https://placehold.it/15/ffffff/000000?text=+) White Colour: #ffffff; "White" - This is the standard white colour on the website.
- ![#f2f2f2](https://placehold.it/15/f2f2f2/000000?text=+) Off White Colour: #f2f2f2; "Concrete" - This off white colour provides sufficient layout differences between the white page background.
- ![#017735](https://placehold.it/15/017735/000000?text=+) Text On White Colour: #017735; "Fun Green" - This is a somewhat darker variation of the primary colour to be used when text is positioned on a white background.
- ![#000](https://placehold.it/15/b2e4c8/000000?text=+) Black Colour: #000; "Black" - This is the standard black colour on the website.
- ![#ff0000](https://placehold.it/15/ff0000/000000?text=+) Required Colour: #ff0000; "Required" - This is the standard red colour to be used for required symbols.
- ![#cc0000](https://placehold.it/15/cc0000/000000?text=+) Error Colour: #cc0000; "Guardsman Red" - This is the standard red colour to be used to indicate errors, it is a somewhat stronger red than the last to indicate to the user that something has gone wrong.
- ![#25bd2c](https://placehold.it/15/25bd2c/000000?text=+) Success Colour: #25bd2c; "Success" - This is the standard green colour to be used to indicate successful interactions on the website.

### Base Styles:

TheCoffeeShop Colours: 

```scss
$primary-color: #b2e4c8; // primary
$secondary-color: #58493c; // secondary
$tertiary-color: #f1e2d0; // tertiary 
$white-color: #ffffff; // white
$off-white-color: #f2f2f2; // off-white
$black-color: #000; // black
$required-color: #ff0000; // required-red
$error-color: #cc0000; // error-red
$success-color: #25bd2c; // success-green
```

Layout Colours:

```scss
$text-on-white-color: #017735;
$main-nav-color: $secondary-color;
$main-footer-color: $secondary-color;
$main-background-color: $white-color;
$main-panel-color: darken($off-white-color, 5%);
```

Shadows:

```scss
$panel-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);
$text-shadow: 0.5px 0.5px 1px rgba(0, 0, 0, 0.3);
```

Transitions: 
```scss
$fast-transition: 0.25s all ease-in-out;
$slow-transition: 0.5s all ease-in-out;
```

Borders: 

```scss
$default-border-radius: 6px;
```

### Images:
<p>The images used across the website have been sourced from royalty free image website such as <a href="https://unsplash.com/">this</a>. The images are related to coffee in some way be it baristas, coffee displays or even ground coffee. This helps to provide lifestyle imagery to the user and potentially entice them into making a purchase.</p>

## Wireframes/Flowcharts: 🔧
<p>I used <a href="https://www.sketch.com/">Sketch</a> to develop the wireframes for The Coffee Shop website, this seemless tool allowed me to easily make a wireframe for each page aswell as a wireframe for each device. I could then easily export them via the tool to .png files in order to save to the project.</p> 

<p>The wireframes for this project can be seen <a href="https://github.com/Geomint/thecofffeeshop/tree/master/wireframes">here</a></p>

### Account Creation Flowchart:

<p>The account creation flowchart for this project can be viewed here <a href="https://github.com/Geomint/thecofffeeshop/tree/master/wireframes/account_auth_flowchart.png">here</a></p>

### Database Design:

* During development of The Coffee Shop I worked with the standard <strong>sqlite3</strong> database that comes installed with Django.
* In the production version of The Coffee Shop, the database is a <strong>PostgreSQL</strong> database, hosted and provided by Heroku.

### The Coffee Shop Data Models:

The user model used in this project is that which is provided by Django, click <a href="https://docs.djangoproject.com/en/3.0/ref/contrib/auth/">here</a> to read more about those tables.

#### The Product Model:

The product model within the product app holds the following data for the products in The Coffee Shop.

**Name**|**Key in db**|**Validation**|**Field Type**
:-----:|:-----:|:-----:|:-----:
Name|name|max\_length=254, default=''"|CharField
Grind Size|grind\_size|max\_length=20, choices=GRIND\_OPTIONS, default=FINE,|CharField
Excerpt|excerpt|max\_length=30, default='some string'|TextField
Description|description|default='some string'|TextField
Description2|description2|default='some string'|TextField
Promoted|promoted|default=False|BooleanField
Image|image|upload\_to="static/images"|ImageField
Price|price|max\_digits=6, decimal\_places=2|DecimalField
RRP|recommended\_retail\_price|max\_digits=6, decimal\_places=2, default=0.0|DecimalField

#### The Order Model:

The Order model within the checkout app holds the following data for the orders in The Coffee Shop.

**Name**|**Key in db**|**Validation**|**Field Type**
:-----:|:-----:|:-----:|:-----:
User|user|User, on\_delete=models.PROTECT|ForeignKey
Full Name|full\_name|max\_length=50, blank=False|CharField
Phone Number|phone\_number|max\_length=20, blank=False|CharField
Country|country|max\_length=40, blank=False|CharField
Postcode|postcode|max\_length=40, blank=False|CharField
City|city|max\_length=40, blank=False|CharField
Address Line 1|address\_line\_1|max\_length=40, blank=False|CharField
Address Line 2|address\_line\_2|max\_length=40, blank=False|CharField
Date|date| |DateField

#### The OrderItem Model:

The OrderItem model within the checkout app holds the following data for the OrderItem(s) in The Coffee Shop.

**Name**|**Key in db**|**Validation**|**Field Type**
:-----:|:-----:|:-----:|:-----:
Order|order|Order, null=False|ForeignKey
Product|product|Product, null=False|ForeignKey
Quantity|quantity|blank=False|IntegerField

## Features: 🎡

### Features that have been developed:

* <p>Sliding latest products carousel that allows users to have a quick look at the list of products available to purchase.</p>
* <p>Account creation, user can login and view orders on profile dashboard.</p>
* <p>User can update their details further from the profile dashboard.</p>
* <p>A search bar that returns a list of products based on the users search query.</p>
* <p>A product list and product detail page so the user can click on individual products and find out more if they so wish.</p>
* <p>An active shopping cart that users can add or remove items from and also update the quantities inside.</p>
* <p>Users can take the cart full of items and checkout using the Stripe API which will process the payment details and place an order.</p>
* <p>Users can send a message via the contact form on the contact page, this utilises the sendgrid API to send the messages via email.</p>

### Features that will be developed in the future:

* <p>A reset password link that will send the user a link to reset their password for The Coffee Shop.</p>
* <p>Products will be filterable by a selection of the properties in the model, e.g grind size or price.</p>
* <p>Full integration of the sendgrid API: there are cname records which need to be set at domain level in order to fully utilise this API, however this was beyond the scope of the requried criteria as I do not have a physical domain for The Coffee Shop, just that which Heroku provides. Read more about the sendgrid integration in the planning & testing section below.</p>
* <p>Order confirmation emails to be sent to the customer upon placing an order.</p>
* <p>A promoted section where the users can see all of the products that are flagged as 'promoted' in the database.</p>

## Technologies Used: 👨‍💻
#### Languages:
* <a href="https://developer.mozilla.org/en-US/docs/Web/HTML">HTML</a>
* <a href="https://developer.mozilla.org/en-US/docs/Web/CSS">CSS</a>
* <a href="https://www.w3schools.com/js/">JavaScript</a>
* <a href="https://www.json.org/json-en.html">JSON</a>
* <a href="https://www.python.org/">Python</a>

#### Tools & Libraries: 

* <a href="https://jquery.com/">jQuery</a>
* <a href="https://git-scm.com/">Git</a>
* <a href="https://getbootstrap.com/">Bootstrap</a>
* <a href="https://fontawesome.com/icons?d=gallery">Font-Awesome</a>
* <a href="https://kenwheeler.github.io/slick/">Slick Carousel</a>
* <a href="https://sass-lang.com/">SASS/SCSS</a>
* <a href="https://tinypng.com/">TinyPng (image compression)</a>
* <a href="https://sweetalert2.github.io/">Sweetalert2</a>
* <a href="https://pip.pypa.io/en/stable/installing/">PIP</a>
* <a href="http://whitenoise.evans.io/en/stable/">WhiteNoise</a>
* <a href="https://pypi.org/project/psycopg2/">Psycopg2</a>
* <a href="https://pypi.org/project/gunicorn/">Gunicorn</a>
* <a href="https://stripe.com/">Stripe</a>
* <a href="https://www.djangoproject.com/">Django</a>
* <a href="https://code.visualstudio.com/">Visual Studio Code</a>
* <a href="https://sendgrid.com/">Sendgrid</a>

#### Databases:

* <a href="https://www.postgresql.org/">PostgreSQL - Production</a>
* <a href="https://www.sqlite.org/index.html">SQlite3 - Development</a>

## Planning:  + Testing: ✏️ 🔌

#### Planning: 

#### Testing: 

#### Feature Testing 🎡: 

<strong>Feature -</strong>
- <strong>Plan</strong> 📝: 

- <strong>Implementation</strong> 🏭: 

- <strong>Test</strong> 🧪: 

- <strong>Result</strong> 🏆: 

- <strong>Verdict</strong> ✅: 


## Bugs 🐞

#### Bugs During Development: 



<p>Case Sensitive Confusion:</p>

- <strong>Bug</strong> 🐞:
 
- <strong>Fix</strong> 🔧: 

- <strong>Verdict</strong> ✅: 


## Deployment 🚀


### Cloning The Coffee Shop from GitHub:

### Deploying The Coffee Shop to Heroku:

## Credits 💳

* <a href="https://medium.com/developing-with-sass/creating-a-dead-simple-sass-mixin-to-handle-responsive-breakpoints-889927b37740">Mixin For Breakpoints</a>
* <a href="https://www.favicon-generator.org/">Favicon Generator</a>  
* <a href="https://coolors.co/">Coolors.co</a>
* <a href="https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB">Unicorn Revealer</a>
* <a href="https://hatchful.shopify.com/">Logo Design</a>
* <a href="https://unsplash.com/">Unsplash - Royalty Free Images</a>
* <a href="https://www.shopcoffee.co.uk/">Coffee Images & Content</a>
* <a href="https://ironandfire.co.uk/">Coffee Images & Content</a>

## Disclaimer
The contents of this website are for educational purposes only.


