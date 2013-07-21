from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=45)
    protein = models.DecimalField(max_digits=4, decimal_places=2)
    carbs = models.DecimalField(max_digits=4, decimal_places=2)
    fat = models.DecimalField(max_digits=4, decimal_places=2)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    notes = models.TextField()
    
    @property
    def calories_tot(self):
        return int(round(self.protein*4 + self.carbs*4 + self.fat*9))
    @property
    def calories_protein(self):
        return self.protein * 4
    @property
    def calories_carbs(self):
        return self.carbs * 4
    @property
    def calories_fat(self):
        return self.fat * 9

class Meal(models.Model):
    name = models.CharField(max_length=45)
    label = models.TextField()
    foods = models.ManyToManyField(Food, through='Quantity')
    
    @property
    def foodlist(self):
        return self.foods.all()
    @property
    def macros(self):
        m = {
            'protein': 0,
            'carbs': 0,
            'fat': 0,
            'kcal': 0,
            'price': 0
        }
        for f in self.foods.all():
            g = self.quantity_set.get(food=f, meal=self).grams
            m['protein'] = m['protein'] + f.protein / 100 * g
            m['carbs'] = m['carbs'] + f.carbs / 100 * g
            m['fat'] = m['fat'] + f.fat / 100 * g
            m['price'] = m['price'] + f.price / 1000 * g
        m['protein'] = int(round(m['protein']))
        m['carbs'] = int(round(m['carbs']))
        m['fat'] = int(round(m['fat']))
        m['kcal'] = m['protein']*4 + m['carbs']*4 + m['fat']*9
        m['price'] = round(m['price'], 2)
        return m

class Quantity(models.Model):
    food = models.ForeignKey(Food)
    grams = models.DecimalField(max_digits=6, decimal_places=2)
    meal = models.ForeignKey(Meal)
