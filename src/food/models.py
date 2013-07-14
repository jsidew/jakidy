from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=45)
    protein = models.DecimalField(max_digits=4, decimal_places=2)
    carbs = models.DecimalField(max_digits=4, decimal_places=2)
    fat = models.DecimalField(max_digits=4, decimal_places=2)
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
