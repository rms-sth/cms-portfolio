# Generated by Django 2.1.9 on 2019-06-21 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_cms_integration', '0002_auto_20190621_1233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectpluginmodel',
            old_name='project',
            new_name='author',
        ),
    ]
