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
    
    @property
    def kcc_cent(self):
        return self._centify(self.kcc, self.kcal)
    @property
    def kcf_cent(self):
        return self._centify(self.kcf, self.kcal)
    @property
    def kcp_cent(self):
        return self._centify(self.kcp, self.kcal)
    @property
    def sugar_cent(self):
        return self._centify(self.sugar, self.carbs)
    @property
    def fiber_cent(self):
        return self._centify(self.fiber, self.carbs)
    @property
    def starch_cent(self):
        return self._centify(self.starch, self.carbs)
    @property
    def monounsat_cent(self):
        return self._centify(self.monounsat, self.fats)
    @property
    def polyunsat_cent(self):
        return self._centify(self.polyunsat, self.fats)
    @property
    def saturated_cent(self):
        return self._centify(self.saturated, self.fats)
    
    def _centify(self, num, den):
        return int(round(num * 100 / den))

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
    notes = models.TextField()
