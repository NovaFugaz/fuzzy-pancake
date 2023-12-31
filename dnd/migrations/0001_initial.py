# Generated by Django 4.2.2 on 2023-07-07 19:52

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('user_profile', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='dnd.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('level', models.IntegerField(null=True)),
                ('exp', models.IntegerField(null=True)),
                ('race', models.CharField(max_length=30, null=True)),
                ('alignment', models.CharField(max_length=40, null=True)),
                ('class1', models.CharField(max_length=30, null=True)),
                ('strength', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0, message='El valor debe ser igual o mayor que 0.'), django.core.validators.MaxValueValidator(30, message='El valor debe ser igual o menor que 30.')])),
                ('dexterity', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0, message='El valor debe ser igual o mayor que 0.'), django.core.validators.MaxValueValidator(30, message='El valor debe ser igual o menor que 30.')])),
                ('constitution', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0, message='El valor debe ser igual o mayor que 0.'), django.core.validators.MaxValueValidator(30, message='El valor debe ser igual o menor que 30.')])),
                ('intelligence', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0, message='El valor debe ser igual o mayor que 0.'), django.core.validators.MaxValueValidator(30, message='El valor debe ser igual o menor que 30.')])),
                ('wisdom', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0, message='El valor debe ser igual o mayor que 0.'), django.core.validators.MaxValueValidator(30, message='El valor debe ser igual o menor que 30.')])),
                ('charisma', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0, message='El valor debe ser igual o mayor que 0.'), django.core.validators.MaxValueValidator(30, message='El valor debe ser igual o menor que 30.')])),
                ('prof_bonus', models.IntegerField(null=True)),
                ('armor_class', models.IntegerField(null=True)),
                ('iniciative', models.IntegerField(null=True)),
                ('move_speed', models.IntegerField(null=True)),
                ('str_mod', models.IntegerField(null=True)),
                ('con_mod', models.IntegerField(null=True)),
                ('int_mod', models.IntegerField(null=True)),
                ('wis_mod', models.IntegerField(null=True)),
                ('dex_mod', models.IntegerField(null=True)),
                ('cha_mod', models.IntegerField(null=True)),
                ('acrobacias', models.IntegerField(null=True)),
                ('conocimiento_arcano', models.IntegerField(null=True)),
                ('atletismo', models.IntegerField(null=True)),
                ('engaño', models.IntegerField(null=True)),
                ('historia', models.IntegerField(null=True)),
                ('interpretacion', models.IntegerField(null=True)),
                ('investigación', models.IntegerField(null=True)),
                ('juego_de_manos', models.IntegerField(null=True)),
                ('medicina', models.IntegerField(null=True)),
                ('naturaleza', models.IntegerField(null=True)),
                ('percepcion', models.IntegerField(null=True)),
                ('perspicacia', models.IntegerField(null=True)),
                ('persuasion', models.IntegerField(null=True)),
                ('religion', models.IntegerField(null=True)),
                ('sigilo', models.IntegerField(null=True)),
                ('supervivencia', models.IntegerField(null=True)),
                ('trato_con_animales', models.IntegerField(null=True)),
                ('user_profile', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='dnd.userprofile')),
            ],
        ),
    ]
