class Recipe:
    # receipe name (from layer1)
    name = "title"
    # receipe uri (from layer1)
    uri = "http://idea.rpi.edu/heals/kb"
    # list of ingredient objects (from det_igrs)
    ingredients = list()

    # dictionary for fsa lights (from recipes with nutritional info)
    fsa_lights_per100g = {
        "fat": "green",
        "salt": "green",
        "saturates": "green",
        "sugars": "green"
    }
    # dictionary for nutritional values (from recipes with nutritional info)
    nutr_values_per100g = {
        "energy": 0,
        "fat": 0,
        "protein": 0,
        "salt": 0,
        "saturates": 0,
        "sugars": 0
    }
