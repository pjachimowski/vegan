import os
from flask import Flask, render_template, redirect, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'vegan'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-xvp8g.mongodb.net/vegan?retryWrites=true&w=majority'

mongo = PyMongo(app)


# route that shows main page with all the recipes set in 3 categories.
# brecipes is a variable representing breakfast recipes
# lrecipes is a variable representing lunch recipes
# drecipes is a variable representing dinner recipes
@app.route('/')
@app.route('/get_vegan_day')
def get_vegan_day():
    brecipes = mongo.db.recipes.find()
    lrecipes = mongo.db.recipes.find()
    drecipes = mongo.db.recipes.find()
    print(brecipes)
    print(lrecipes)
    print(drecipes)
    return render_template("vegan_day.html", brecipes=brecipes, lrecipes=lrecipes, drecipes=drecipes)


# route for new recipe form display
@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html',
                           categories=mongo.db.categories.find())


# route for inserting data into recipe acordeon
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipe = mongo.db.recipes
    recipe.insert_one(request.form.to_dict())
    return redirect(url_for('get_vegan_day'))


# route for full recipe display
@app.route('/full_recipe/<recipe_id>')
def full_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template('full_recipe.html', recipe=the_recipe,
                           categories=all_categories)


# route for form page that takes existing date and display it for editing
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template('edit_recipe.html', recipe=the_recipe,
                           categories=all_categories)


# route that injects data from database
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update({'_id': ObjectId(recipe_id)},
                   {
                    'recipe_name': request.form.get('recipe_name'),
                    'category_name': request.form.get('category_name'),
                    'recipe_short': request.form.get('recipe_short'),
                    'recipe_description': request.form.get('recipe_description'),
                    'recipe_ingredients': request.form.get('recipe_ingredients'),
                    'recipe_method': request.form.get('recipe_method'),
                    'recipe_image': request.form.get('recipe_image'),
                    'gluten_free': request.form.get('gluten_free'),
                })
    return redirect(url_for('get_vegan_day'))


# route that delete existing recipe from dataset
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_vegan_day'))


# route that injects categories
@app.route('/get_categories')
def get_categories():
    return render_template('categories.html',
                           categories=mongo.db.categories.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
