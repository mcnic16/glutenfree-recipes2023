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
