# Generated by Django 2.2.3 on 2019-09-26 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0003_auto_20190926_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='avatar',
            field=models.FileField(max_length=200, upload_to='static/upload_image/', verbose_name='头像'),
        ),
    ]
