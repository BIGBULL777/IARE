# Generated by Django 3.2.8 on 2021-12-18 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CoviSafe', '0005_citizen_profile_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='self_assesment_test',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CoviSafe.citizen'),
        ),
    ]
