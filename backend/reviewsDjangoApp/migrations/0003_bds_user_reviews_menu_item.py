# Generated by Django 4.2.5 on 2023-12-10 21:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reviewsDjangoApp", "0002_rename_userreviews_bds_user_reviews"),
    ]

    operations = [
        migrations.AddField(
            model_name="bds_user_reviews",
            name="menu_item",
            field=models.TextField(blank=True, null=True),
        ),
    ]
