# Generated by Django 4.0 on 2022-01-07 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0002_tag_alter_ems_id_review_ems_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='ems',
            name='vote_ratio',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
