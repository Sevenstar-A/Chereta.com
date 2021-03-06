# Generated by Django 3.0 on 2020-09-14 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Bid', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='Credit_card',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='bid',
            name='Uploader',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='uploader', to='Bid.Client'),
        ),
        migrations.AddField(
            model_name='client',
            name='Credit_card',
            field=models.CharField(default='', max_length=20),
        ),
    ]
