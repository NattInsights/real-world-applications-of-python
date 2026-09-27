def shopping_list(recipe, cupboard):
    missing_items = []
    for i in recipe:
        if i not in cupboard:
            missing_items.append(i)
    return missing_items

print(shopping_list(["apple", "banana", "flour", "peanut"],["banana", "peanut"]))