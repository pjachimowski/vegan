[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://https://github.com/pjachimowski/vegan)

# Vegan Day
...........................................................................................
Vegan day is a cooking blog / app where the user can create, read, edit and delete vegan recipes. Recipes are sorted out by categories: breakfast, lunch and dinner. It this way, the user can select his vegan day inspirations. 

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
- A form page to create new recipe. 
Here all form fields are blank. Form fields are: 
> Select category: for selecting which type of meal (category on the main page) this recipe will be asigned to.
> Recipe name: short name displaied in the full_recipe.html as a title.
> Short description: this short text will be shown in collapsable body of the accordion.
> More about this recipe: full description of the recipe. Show only in the full recipe page. 
> Ingredients: list of ingredients displayed in the small frame titled "Shopping list"
> Method: descriptionof how to prepare a meal.
> Add image: here user can paste the link for the image uploaded to inbb service. Here also user can see instruction on how to upload the image.  
> Gluten free: a check box form.

### Edit recipe page
- A form page to edit existing recipe. All the form fields are filled with the data set of a editable recipe. Page template is filled with data from mongoDB according to recipe Id. Form fields are mirroring add_recipe page: 
> Select category
> Recipe name
> Short description
> More about this recipe
> Ingredients
> Method
> Add image 
> Gluten free 
- Save button save all the implemented changes and redirect back to the main page. 

### Full recipe page
- The page is data representation of the recipe. This page can not be edited or changed. The layout of the page is different than edit_recipe.html or add_recipe.html. Here user see more apealing layout and also a banner image before the header. Page template is filled with data from mongoDB according to recipe Id.
- At the bottom of the page there are two icons: EDIT and DELETE a page. 

### Footer
- Logo in different color scheme featured (clickable - leads to home page)
- Quote from the author of the page. 
- CONTACT. email provided as well as social media links. 
- COPYRIGHT stripe

### In the future:
- Random recipe button 
- more content

# TESTING Write up
...........................................................................................
### Forms
- all the form have validation features. all forms passed testing. 
 
### Buttons
- all the buttons are linked correctly and fire up successfully 

### links
- social media links passed all tests and leads to correct page. 

### Responsivenes
- site terted in google chrome developer tools as well as on desktop and mobile versions. All elements are responsive, the layout does not break, elements are not overlaping. 

### Code validation
- Python Code tested with PEP8. Python code adheres to PEP8 standards. (http://pep8online.com/checkresult)
    exception being E501 "line is too long"
- HTML code tested with online validator. (https://www.freeformatter.com/html-validator.html)
- CSS code tested with online validator (http://csslint.net/)
    exception being "Using width with padding can sometimes make elements larger than you expect."


# DEPLOYMENT Write up
...........................................................................................
My project was developed using GitPod IDE, committed to git and pushed to GitHub. The following steps where taken to deploy my project. Heroku app connected to GitHub Code diffs, manual and auto deploys are available for this app. Automatic deploys from  master branch are enabled.

### From GitHub
- Logged into GitHub.
- Selected repository from the GitHub dashboard.
- Clicked on "Open in GitPod button"
- From gitpod I accessed the page via terminal coment "python3 app.py runserver"

### From Heroku
- Logged into Heroku
- Opened the pj-stickers project 
- In Deploy panel I clicked Deploy branch
- After the page is deployed I opened the app vie "Open App" button

Website is now deployed and is available here:
https://vegan-day.herokuapp.com/
My repository can be found here:
https://github.com/pjachimowski/vegan


# TECHNOLOGIES USED
...........................................................................................
### Languages
- HTML
- CSS
- JavaScript
- Python
- flask


### Libraries
- Materialize (https://materializecss.com/)
- Fontawesome (https://fontawesome.com/)

### Database
- mongoDB
- static files 

### Others
- gradient generator CSS (www.ccbg.io)
- Heroku cloud platform

# Use of other code
...........................................................................................

- I use fragments of the code from previous lessons of Code Institure.
All codes were sourced from my own profile on GitHub portal
Parts of the code were edited and adjust to page layout.

### Media
Some images were downloaded for free picture collection https://www.pexels.com/
Icons were taken from font awesome portal.
Entire text was edited by author.


# TESTING Write up
...........................................................................................
## HTML
- HTML code produces NO errors on being passed through a validator.
https://validator.w3.org/nu/ 

- All the forms passed testing. All the forms featured with form validation code. 

### Acknowledgments

- I received inspiration for this project from various lessons conducted at Code Institute