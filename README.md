# foodkg-search-tool
a tool to search recipes in foodkg and display its data by specific search

Here is the raw data source collected from FoodKG, https://foodkg.github.io/foodkg.html, http://im2recipe.csail.mit.edu/dataset/download/
We downloaded Layers (used layer 1.json (all the recipes), det_ingrs.json, and recipe_nutri_info.json.

In this version of the code, a smaller extract of Layers (partial_layers_json) is used instead of the full dataset.

We used Whoosh to do the search.
