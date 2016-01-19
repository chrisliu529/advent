class Ingredient(object):
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories

def parse_ingredient(line):
    l = line.split()
    return Ingredient(l[0][:-1], int(l[2][:-1]), int(l[4][:-1]), int(l[6][:-1]), int(l[8][:-1]), int(l[10]))

def parse_ingredients(path):
    f = file(path)
    lines = f.read().split('\n')
    ingredients = []
    for line in lines:
        if line == '':
            continue
        ing = parse_ingredient(line)
        ingredients.append(ing)
    return ingredients

def menu_include(menu, name):
    for x in menu:
        if x[0].name == name:
            return True
    return False

def menu_score(menu):
    s_cap = 0
    s_dur = 0
    s_fla = 0
    s_text = 0
    for (ing, i) in menu:
        s_cap += ing.capacity * i
        s_dur += ing.durability * i
        s_fla += ing.flavor * i
        s_text += ing.texture * i
    if s_cap < 0 or s_dur < 0 or s_fla < 0 or s_text < 0:
        return 0
    return s_cap*s_dur*s_fla*s_text

def try_recipe(ingredients, menu, amount, bs):
    best_menu = []
    remained = [ing for ing in ingredients if not menu_include(menu, ing.name)]
    if len(remained) == 1:
        menu.append((remained[0], amount))
        s = menu_score(menu)
        if s > bs:
            best_menu = list(menu)
        if best_menu != []:
            print best_menu
        menu.pop()
        return s

    for ing in remained:
        for i in range(amount):
            menu.append((ing, i))
            s = try_recipe(ingredients, menu, amount - i, bs)
            menu.pop()
            if s > bs:
                bs = s
    return bs

def best_score(path):
    ingredients = parse_ingredients(path)
    return try_recipe(ingredients, [], 100, 0)

def main():
    assert 62842880 == best_score('input15a')
    print best_score('input15')
    
main()
