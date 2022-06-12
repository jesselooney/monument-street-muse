# Generated by Django 4.0.4 on 2022-05-24 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0002_alter_magazine_options_magazine_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magazine',
            name='issue',
            field=models.SmallIntegerField(default=None, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='magazine',
            name='publication_date',
            field=models.DateField(default=None, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='magazine',
            name='volume',
            field=models.SmallIntegerField(default=None, editable=False, null=True),
        ),
    ]