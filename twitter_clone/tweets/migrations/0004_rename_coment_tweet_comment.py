# Generated by Django 4.1.5 on 2023-02-26 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tweets", "0003_tweet_coment"),
    ]

    operations = [
        migrations.RenameField(
            model_name="tweet",
            old_name="coment",
            new_name="comment",
        ),
    ]
