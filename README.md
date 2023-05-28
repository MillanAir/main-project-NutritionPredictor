# Recipe Recommender

A food recommendation system which predicts the calories based on ingredients provided and give you similar recipes.

## Problem Statement

Due to fast paced life of the individuals it is very tedious task to calculate the nutritional information for informed dietary choices. There is a need for a quick way of calculating the nutrition by ingredients used in making a recipe.

## Scope

The project focuses on analyzing the nutritional content of recipes by considering the ingredients and servings used. It predicts the approximate values of calories, proteins, carbohydrates, and fats based on these factors.

## Project Flow

- Acquaring Data
- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Model Building
- Saving the Model
- Deployment
- Testing

## Data

The data is taken from [AllRecipe](https://www.allrecipes.com/) which contains 14,000+ recipes. The data is in the form of JSON file which contains the recipe name, ingredients, steps to cook, calories, rating, etc.

## Limitations

There were various limitations on my data for eg. my data didn’t contain  the actual values of each ingredient and was trained on collection of ingredients which lead to differences in the predicted nutritional values.

## Future Scope

To acquire a dataset of each ingredient nutritional information and then standardized the units into single unit
For eg:
- Kilograms to Grams
- Litres to Millilitres