# Generated by Django 4.1.7 on 2023-04-03 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='center_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='center.center'),
        ),
    ]
