from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
            
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()


class Note(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'dnd'

# class Race(models.Model):
#     name = models.CharField(max_length=30, null=True)
#     race_str_mod = models.IntegerField(null=True)
#     race_con_mod = models.IntegerField(null=True)
#     race_int_mod = models.IntegerField(null=True)
#     race_wis_mod = models.IntegerField(null=True)
#     race_dex_mod = models.IntegerField(null=True)
#     race_cha_mod = models.IntegerField(null=True)
#     size = models.CharField(max_length=25)
#     speed = models.IntegerField()
#     language1 = models.CharField(max_length=30)
#     language2 = models.CharField(max_length=30, null=True)
        
#     class Meta:
#         abstract = True

# class Dragonborn(Race):
#     name = models.CharField(max_length=35, default="Dracónido")
#     race_str_mod = 2
#     race_con_mod = 0
#     race_int_mod = 0
#     race_wis_mod = 0
#     race_dex_mod = 0
#     race_cha_mod = 1
#     size = "Medio"
#     speed = 30
#     language1 = "Common"
#     language2 = "Dracónico"
    

# class Dwarf(Race):
#     name = models.CharField(max_length=35, default="Enano")
#     race_str_mod = 0
#     race_con_mod = 2
#     race_int_mod = 0
#     race_wis_mod = 0
#     race_dex_mod = 0
#     race_cha_mod = 0
#     size = "Medio"
#     speed = 25
#     language1 = "Common"
#     language2 = "Enano"

# class HillDwarf(Dwarf):
#     name = models.CharField(max_length=35, default="Enano de Colina")
#     race_str_mod = 0
#     race_con_mod = 2
#     race_int_mod = 0
#     race_wis_mod = 1
#     race_dex_mod = 0
#     race_cha_mod = 0
#     size = "Medio"
#     speed = 25
#     language1 = "Common"
#     language2 = "Enano"

# class MountainDwarf(Dwarf):
#     name = models.CharField(max_length=35, default="Enano de Montaña")
#     race_str_mod = 2
#     race_con_mod = 2
#     race_int_mod = 0
#     race_wis_mod = 0
#     race_dex_mod = 0
#     race_cha_mod = 0
#     size = "Medio"
#     speed = 25
#     language1 = "Common"
#     language2 = "Enano"

# class Elf(Race):
#     name = models.CharField(max_length=35, default="Elfo")
#     race_str_mod = 0
#     race_con_mod = 0
#     race_int_mod = 0
#     race_wis_mod = 0
#     race_dex_mod = 2
#     race_cha_mod = 0
#     size = "Medio"
#     speed = 30
#     language1 = "Common"
#     language2 = "Élfico"


# class DrowElf(Elf):
#     name = models.CharField(max_length=35, default="Elfo Oscuro")
#     race_str_mod = 0
#     race_con_mod = 0
#     race_int_mod = 0
#     race_wis_mod = 0
#     race_dex_mod = 2
#     race_cha_mod = 0
#     size = "Medio"
#     speed = 30
#     language1 = "Common"
#     language2 = "Élfico"

# class HighElf(Elf):
#     pass

# class WoodElf(Elf):
#     pass

# class Gnome(Race):
#     pass

# class ForestGnome(Gnome):
#     pass

# class RockGnome(Gnome):
#     pass

# class HalfElf(Race):
#     pass

# class HalfOrc(Race):
#     pass

# class Halfling(Race):
#     pass

# class LightfootHalfling(Halfling):
#     pass

# class StoutHalfling(Halfling):
#     pass

# class Human(Race):
#     pass

# class Tiefling(Race):
#     pass

class Character(models.Model):
    
    valminmax = [
    MinValueValidator(0, message='El valor debe ser igual o mayor que 0.'),
    MaxValueValidator(30, message='El valor debe ser igual o menor que 30.')]
    
    name = models.CharField(max_length=30, null=True)
    level = models.IntegerField(null=True)
    exp = models.IntegerField(null=True)
    race = models.CharField(max_length=30, null=True)
    #subrace = models.CharField(null=True, max_length=25) # null=True permite que quede vacío a menos que se especifique.
    alignment = models.CharField(max_length=40, null=True)
    class1 = models.CharField(max_length=30, null=True)
    # class2 = models.CharField(max_length=30, null=True) No lo voy a tirar a la presentación, específicamente para evitar atados.
    strength = models.IntegerField(validators=valminmax, null=True)
    dexterity = models.IntegerField(validators=valminmax, null=True)
    constitution = models.IntegerField(validators=valminmax, null=True)
    intelligence = models.IntegerField(validators=valminmax, null=True)
    wisdom = models.IntegerField(validators=valminmax, null=True)
    charisma = models.IntegerField(validators=valminmax, null=True)
    prof_bonus = models.IntegerField(null=True)
    armor_class = models.IntegerField(null=True)
    iniciative = models.IntegerField(null=True)
    move_speed = models.IntegerField(null=True)
    str_mod = models.IntegerField(null=True)
    con_mod = models.IntegerField(null=True)
    int_mod = models.IntegerField(null=True)
    wis_mod = models.IntegerField(null=True)
    dex_mod = models.IntegerField(null=True)
    cha_mod = models.IntegerField(null=True)
    acrobacias = models.IntegerField(null=True)
    conocimiento_arcano = models.IntegerField(null=True)
    atletismo = models.IntegerField(null=True)
    engaño = models.IntegerField(null=True)
    historia = models.IntegerField(null=True)
    interpretacion = models.IntegerField(null=True)
    investigación = models.IntegerField(null=True)
    juego_de_manos = models.IntegerField(null=True)
    medicina = models.IntegerField(null=True)
    naturaleza = models.IntegerField(null=True)
    percepcion = models.IntegerField(null=True)
    perspicacia = models.IntegerField(null=True)
    persuasion = models.IntegerField(null=True)
    religion = models.IntegerField(null=True)
    sigilo = models.IntegerField(null=True)
    supervivencia = models.IntegerField(null=True)
    trato_con_animales = models.IntegerField(null=True)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=None)
    
    @classmethod
    def calculate_modifier(cls, attribute_value):
        return (attribute_value - 10) // 2

    def save(self, *args, **kwargs):
        self.str_mod = self.calculate_modifier(self.strength)
        self.con_mod = self.calculate_modifier(self.constitution)
        self.int_mod = self.calculate_modifier(self.intelligence)
        self.wis_mod = self.calculate_modifier(self.wisdom)
        self.dex_mod = self.calculate_modifier(self.dexterity)
        self.cha_mod = self.calculate_modifier(self.charisma)
        self.acrobacias = self.dex_mod
        self.conocimiento_arcano = self.int_mod
        self.atletismo = self.str_mod
        self.engaño = self.cha_mod
        self.historia = self.int_mod
        self.interpretacion = self.cha_mod
        self.investigación = self.int_mod
        self.juego_de_manos = self.dex_mod
        self.medicina = self.wis_mod
        self.naturaleza = self.int_mod
        self.percepcion = self.wis_mod
        self.perspicacia = self.wis_mod
        self.persuasion = self.cha_mod
        self.religion = self.int_mod
        self.sigilo = self.dex_mod
        self.supervivencia = self.wis_mod
        self.trato_con_animales = self.wis_mod
        self.iniciative = self.dex_mod

        super().save(*args, **kwargs)
    
    
    def __str__(self):
        return self.name