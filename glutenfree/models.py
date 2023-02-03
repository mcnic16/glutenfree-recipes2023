from glutenfree import db


class Starter(db.Model):
    # For Starters
    id = db.Column(db.Integer, primary_key=True)
    starter_names = db.Column(db.Text, unique=True, nullable=False)
    starter_tools = db.Column(db.Text, unique=True, nullable=False)
    starter_ingredients = db.Column(db.Text, unique=True, nullable=False)
    starter_directions = db.Column(db.Text, unique=True, nullable=False)

    def __repr__(self):
        return f"Starter('{self.id}', '{self.starter_names}',\
            '{self.starter_tools}', '{self.starter_ingredients},\
                '{self.starter_directions}')"


class Main(db.Model):
    # For Main Course
    id = db.Column(db.Integer, primary_key=True)
    main_names = db.Column(db.Text, unique=True, nullable=False)
    main_tools = db.Column(db.Text, unique=True, nullable=False)
    main_ingredients = db.Column(db.Text, unique=True, nullable=False)
    main_directions = db.Column(db.Text, unique=True, nullable=False)

    def __repr__(self):
        return f"Main('{self.id}', '{self.main_names}',\
            '{self.main_tools}', '{self.main_ingredients},\
                '{self.main_directions}')"


class Dessert(db.Model):
    # For Desserts
    id = db.Column(db.Integer, primary_key=True)
    dessert_names = db.Column(db.Text, unique=True, nullable=False)
    dessert_tools = db.Column(db.Text, unique=True, nullable=False)
    dessert_ingredients = db.Column(db.Text, unique=True, nullable=False)
    dessert_directions = db.Column(db.Text, unique=True, nullable=False)

    def __repr__(self):
        return f"Dessert('{self.id}', '{self.dessert_names}',\
            '{self.dessert_tools}', '{self.dessert_ingredients},\
                '{self.dessert_directions}')"


class Drink(db.Model):
    # For Drinks
    id = db.Column(db.Integer, primary_key=True)
    drink_names = db.Column(db.Text, unique=True, nullable=False)
    drink_tools = db.Column(db.Text, unique=True, nullable=False)
    drink_ingredients = db.Column(db.Text, unique=True, nullable=False)
    drink_directions = db.Column(db.Text, unique=True, nullable=False)

    def __repr__(self):
        return f"Drink('{self.id}', '{self.drink_names}',\
            '{self.drink_tools}', '{self.drink_ingredients},\
                '{self.drink_directions}')"

