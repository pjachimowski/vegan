[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://https://github.com/pjachimowski/vegan)

# Vegan Day
...........................................................................................
Vegan day is a cooking blog / app where the user can create, read, edit and delete vegan recipes. Recipes are sorted out by categories: breakfast, lunch and dinner. It this was the user can select his vegan day inspirations. 

# UX Write up
...........................................................................................
## color scheme
- Main body uses generated css gradient (via https://www.ccbg.io/)
Dark gray, black and bright green are the colors I chose to create very modern and appealing look.
Most of the text is in very light gray in order to improve readability. 
I did not want to use 100% white or 100% black. 
Main colors used:
white: #e4e4e4; black: #2e2e2e; green: #00eea7;

- Main buttons and call-to-action buttons:
Used as a contrast to dark background. Eye - catcher. 
green: #00eea7;

Background picture for home page as well as footer and shopping list background were darkened for better contrasting with the font. 

## typography
- Main titles and titles on the product cards:
font-family: 'Merienda'
- Rest:
font-family: 'Roboto'

## USER STORIES
### Epic:
As a user, I want to create, read, edit and delete vegan recipes.
### Detailed:
As a private person who's goal is to keep a daily diet vegan, this app serves as a list of recipes, sorted in 3 categories: breakfast, lunch and dinner.
The websites functionality benefits user with:
- Easy preview of the recipes
- Posibility to edit if necessary
- If user is no longer intersted in recipe there is a possibility to delete it
- Author can connect with others via social medialinks

## WIREFRAMES
An early stage draft of the app. Changes appied. 

### Home page top
![](static/images/wireframes/home_page_top.jpg)
### Home page about
![](static/images/wireframes/home_page_about.jpg)
### Home page benefits
![](static/images/wireframes/home_page_benefits.jpg)
### Home page quotes
![](static/images/wireframes/home_page_quotes.jpg)
### Footer
![](static/images/wireframes/footer.jpg)
### Gallery
![](static/images/wireframes/gallery.jpg)
### Request Form
![](static/images/wireframes/request_form.jpg)


# FEATURES
...........................................................................................
### Navbar 
Navbar is responsive and in mobile version it is displayed as toggle drop down menu.
(elements of the navbar are repeated in the home page panel as weel as in the footer as a logo leading to home page. 
- Logo at the top left corner (self designed)
-a link to home page
- Add recipe btn
-a link to add recipe page 


### Homepage 
- Teaser Page. Brief introduction to the purpose of the website.
- Call-to-action button for adding a new recipe.
- More information ad introduction to the 3 categories.
- All recipes listed as 3 unordered list grouped by categories: breakfast, lunch and dinner. Every recipe is presented as a collapsible element of unordered list inside of an accordion. To get to the main recipe user can click on picture of the selected recipe and see short description. Then later "MORE" button will lead to the separate page of the full recipe description.
- Footer

### Add recipe page
- A form page to create new recipe. Form fields are: 
> Select category
> Recipe name
> Short description
> More about this recipe
> Ingredients
> Method
> Add image 
> Gluten free 

### Edit recipe page
- A form page to create new recipe. Form fields are: 
> Select category
> Recipe name
> Short description
> More about this recipe
> Ingredients
> Method
> Add image 
> Gluten free 

### Footer
- Logo in different color scheme featured (clickable - leads to home page)
- Quote from the author of the page. 
- CONTACT. email provided as well as social media links. 
- COPYRIGHT stripe

### In the future:
- user purchase history
- more content


# TESTING Write up
...........................................................................................
### Forms
- all the form have validation features. all forms passed testing. 
! card with products should accept only numbers. However, they do accept letter 'e'. This error has to be fixed later. 
### Buttons
- all the buttons are linked correctly and fire up successfully 
### Payment 
- test payment with stripe technology was performed successfully 
### Email 
- email sent via REVIEW form as well as REQUEST form
- emails were received in correct form and without errors
### Travis 
- Travis used for automatic validation on deployed site
### Responsivenes
- site terted in google chrome developer tools as well as on desktop and mobile versions. All elements are responsive, the layout does not breat, elements are not overlaping. 
### Code validation
- Python Code tested with PEP8. Python code adheres to PEP8 standards. (http://pep8online.com/checkresult)
    exception being E501 "line is too long"
- HTML code tested with online validator. (https://www.freeformatter.com/html-validator.html)
- CSS code tested with online validator (http://csslint.net/)
    exception being "Using width with padding can sometimes make elements larger than you expect."


# DEPLOYMENT Write up
...........................................................................................
My project was developed using GitPod IDE, committed to git and pushed to GitHub. Finally the code was wired up with AWS S3 where dynamic media content of shop products are stored. The following steps where taken to deploy my project.
### From GitHub
- Logged into GitHub.
- Selected repository from the GitHub dashboard.
- Clicked on "Open in GitPod button"
- From gitpod I accessed the page via terminal coment "python3 manage.py runserver"
### From Heroku
- Logged into Heroku
- Opened the pj-stickers project 
- In Deploy panel I clicked Deploy branch
- After the page is deployed I opened the app vie "Open App" button

Website is now deployed and is available here:
https://pj-stickers.herokuapp.com/
My repository can be found here:
https://github.com/pjachimowski/stickers

## AWS s3
- Media stored in AWS S3 bucket 
- Static files and CSS sored in the project on Heroku


# TECHNOLOGIES USED
...........................................................................................
### Languages
- HTML
- CSS
- JavaScript
- Python
- django
- Stripe payments

### Libraries
- Bootstrap (https://getbootstrap.com/)
- Fontawesome (https://fontawesome.com/)

### Database
- AWS s3
- local sqlite

### Others
- gradient generator CSS (www.ccbg.io)
- Email JS (https://www.emailjs.com/)
- Heroku cloud platform




# Use of other code
...........................................................................................
- footer source(edited)  https://colorlib.com/wp/bootstrap-footer/

- I use fragments of the code from previous lessons of Code Institure.
All codes were sourced from my own profile on GitHub portal
Parts of the code were edited and adjust to page layout.

### Media
Some stickers were downloaded for free picture collection https://www.pexels.com/
Icons were taken from font awesome portal.
Entire text was edited by author.



# TESTING Write up
...........................................................................................
## HTML
- HTML code produces NO errors on being passed through a validator.
https://validator.w3.org/nu/ 

- All the forms passed testing. All the forms featured with form validation code. 


## Password reset
- Password reset tested and passed successfuly. It may display following error:
SMTPAuthenticationError at /accounts/password-reset/
Due to google account default setups. 
Last time updated: 01.05.2020 after which averything was working correctly. 


### Acknowledgments

- I received inspiration for this project from various lessons conducted at Code Institute