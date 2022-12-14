# Generated by Django 4.0.6 on 2022-07-14 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviebook', '0002_remove_zanr_film_film_zanr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uzivatel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=300, unique=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'uživatel',
                'verbose_name_plural': 'uživatelé',
            },
        ),
        migrations.AlterModelOptions(
            name='film',
            options={'verbose_name': 'Film', 'verbose_name_plural': 'Filmy'},
        ),
        migrations.AlterModelOptions(
            name='zanr',
            options={'verbose_name': 'Žánr', 'verbose_name_plural': 'žánry'},
        ),
    ]
