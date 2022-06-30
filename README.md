# RecipeFinder

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) ![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white) ![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)

RecipeFinder is a recipe application that helps users to find the perfect recipe.

* Registering can be done either as an User or an Admin.

* Both may view their profile details and edit them.

* Both Users and Admins may view recipes as well as add the recipe into favorites.

* Only Users may give reviews for recipes. Review can only be done once.

* Only Admins may add, modify and delete recipes.

I have created a product backlog and listed the functionalities in detail [here](https://github.com/riikkayoki/RecipeApp/projects/1).

## Hosting

The application is hosted on Heroku: https://tsoha-recipefinder.herokuapp.com/

## Documentation

* [Installation Instructions](https://github.com/riikkayoki/RecipeApp/blob/master/documentation/installation_instructions.md)

## Security

I have been focusing on the security e.g. by

  * Role of the user (admin or user) is checked when calling POST-method.
  * Users do not have access to pages/information which are not their own information.
  * Input validations are processed when users attempt to pass data to database.

## Browser recommendation

The app works the best on Google Chrome browser, and therefore I would suggest to use this browser.

## Future development for the app

* To be able also to remove old ingredients when modifying recipe. This would need more javascript coding.
