# Generated by Django 3.2.9 on 2021-12-11 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_alter_subcomment_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcomment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply', to='firstapp.subcomment'),
        ),
    ]
