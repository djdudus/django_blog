# Generated by Django 4.1.8 on 2023-09-29 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LEGO', '0006_alter_setbricks_set_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setbricks',
            name='brick_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LEGO.brick'),
        ),
        migrations.AlterField(
            model_name='setbricks',
            name='set_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LEGO.set'),
        ),
    ]
