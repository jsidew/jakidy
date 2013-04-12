from django.db import models

class Food(models.Model):
    FRESH = 'F'
    DRY = 'D'
    STATES = (
        (FRESH, 'fresh'),
        (DRY, 'dry'),
    )
    family = models.CharField(max_length=45)
    species = models.CharField(max_length=45)
    kcal = models.DecimalField(max_digits=6, decimal_places=2)
    kcc = models.DecimalField(max_digits=6, decimal_places=2)
    kcf = models.DecimalField(max_digits=6, decimal_places=2)
    kcp = models.DecimalField(max_digits=6, decimal_places=2)
    carbs = models.DecimalField(max_digits=4, decimal_places=2)
    sugar = models.DecimalField(max_digits=4, decimal_places=2)
    fiber = models.DecimalField(max_digits=4, decimal_places=2)
    starch = models.DecimalField(max_digits=4, decimal_places=2)
    fats = models.DecimalField(max_digits=4, decimal_places=2)
    monounsat = models.DecimalField(max_digits=4, decimal_places=2)
    polyunsat = models.DecimalField(max_digits=4, decimal_places=2)
    saturated = models.DecimalField(max_digits=4, decimal_places=2)
    proteins = models.DecimalField(max_digits=4, decimal_places=2)
    water = models.DecimalField(max_digits=4, decimal_places=2)
    ash = models.DecimalField(max_digits=4, decimal_places=2)
    state = models.CharField(max_length=1, choices=STATES, default=FRESH)

class FoodName(models.Model):
    ITALIAN = 'IT'
    ENGLISH = 'EN'
    LANGUAGES = (
        (ITALIAN, 'italiano'),
        (ENGLISH, 'english'),
    )
    name = models.CharField(max_length=45)
    food = models.ForeignKey('Food')
    lang = models.CharField(max_length=2, choices=LANGUAGES, default=ENGLISH)
    notes = models.TextField(null=True)
