# Generated by Django 5.1.6 on 2025-02-20 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('afiliacao', models.CharField(max_length=50)),
                ('aliados', models.CharField(max_length=150)),
                ('inimigos', models.CharField(max_length=150)),
            ],
        ),
    ]
