# Generated by Django 4.1.5 on 2023-02-26 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tweets", "0002_remove_tweet_coment_of_remove_tweet_comments_count_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="tweet",
            name="coment",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="tweets.tweet",
            ),
        ),
    ]