# Generated by Django 4.2 on 2023-12-07 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matabase', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mag', models.CharField(max_length=255)),
                ('magRef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mag_references', to='matabase.matabasemodel')),
            ],
        ),
    ]
