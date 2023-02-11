<h1 align="center">GlutenFree Recipes</h1>

[View live project](https://glutenfree-recipes.herokuapp.com/)

This project, is a Gluten-Free recipe database where you can can enter your recipes on the home page, and they will show up on the appropriate pages, i.e Starters , Mains etc.
There is also the option to edit or delete these recipes.
I chose this project because a family member has celiac disease and has to maintian a gluten-free diet. 
This is my 2nd attempt at this project because my first project failed, and I had to start the project again due to the amount of errors I was getting which I never had previously


screen shots here

## User Experience

The target audience of this site is for people with celiac disease or who need to maintain a gluten free diet.

As a user I would:

1. I want to see the recipes broken into various categories  so I can decide what I would like to prepare and when.

     The recipes are broken into Starters, Mains, Desserts and Drinks

2. I want to view a list of gluten-free recipes that is healthy for me to eat.

     All the recipes will be added when you type them in and save them.

3. I want to know the preparations for each meal so I can allocate my time accordingly.

      There is a section on each recipe for the preparations.

4. I want to be able to save my recipes so I can have quick access to all my favorites.

      All recipes are automatically added to the database where you can edit or delete them,

5. I want to view a complete list of ingredients so I  know what’s needed to prepare the dish.

      There is a section on each recipe for ingredients.

6. I want to be able to remove ingredients from the list so I don’t double-up on items I may already
have.

      There is an option to remove the items from the database.

7. I want to be able to add in notes to each dish so I can add my own thoughts, experiences or
things I want to remember about cooking the dish.

      There is a directions section where you can add this and also cooking times.

8. I want to be able to have my own personel profile where only I can add or delete items.

      You must register and log into the site before you can view, delete, or add items.

9. I want the site to be easy navigate

      When you enter the site you, you will have a page with a gluten-free picture, on the left hand side in the nav bar are links to either register or login, if you have already registered.
      To add a recipe there is a link on the right hand side called Add to Database where you will be taken to a page where you can add starters, mains, desserts and drinks.
      On the left hand side in the Navbar there are links which will take you to the the link that you require. When you click on these recipes , the fields will show Tools Ingredients and the directions required, there is also a edit button where you can edit these fields, when you have updated the fields, a message will come up to tell you it has been updated, then just click in the category of food you edited and the edited recipe will be there.
      There is also a option to delete the recipe aswell.
      

## Wireframes



## Design



## Typography



## Technologies Used



## Frameworks, Libraries & Programs Used



## Testing
 -  The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the front ednd of the project to ensure there were no syntax errors in the project.

  -   [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)

Here is the Registration Page:
<h2 align="center"><img src="static/img/registration.png" width="400px"></h2>

Here is the Login Page:
<h2 align="center"><img src="static/img/login.png" width="400px"></h2>

Here is the profile page:
<h2 align="center"><img src="static/img/profile.png" width="400px"></h2>

Here Is the home page:
<h2 align="center"><img src="static/img/home.png" width="400px"></h2>

Here are the tests from the starters:

Starters:

<img src="static/img/starters.png" width="400px">

Edit Starters:

<img src="static/img/edit_starters.png" width="400px">

Add Starters:

<img src="static/img/add_starters.png" width="400px">

Mains:

<img src="static/img/mains.png" width="400px">

Edit mains:

<img src="static/img/edit_mains.png" width="400px">

Add mains:

<img src="static/img/add_mains.png" width="400px">


## Bugs
I could not get postgres to work , I kept having the error:

 psql: error: connection to server on socket "/var/run/postgresql/.s.PGSQL.5432" failed: No such file or directory Is the server running locally and accepting connections on that socket?

Everything I tried did not work so I have decided to use MongoDB instead.
I also had an error which was:

'Collection' object is not callable. If you meant to call the 'update' method on a 'Collection' object it is failing because no such method exists 

This was related to the line mongo.db.starter.update({"_id": ObjectId(starter_id)}, edited_starter) in my edit_starters function in app.py, so I had downgrade pymongo from  4.3.3 to 3.12.3.








## Deployment




## Acknowledgements




