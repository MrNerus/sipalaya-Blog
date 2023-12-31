# Generated by Django 4.2.2 on 2023-07-16 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                ("sno", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=255)),
                (
                    "image",
                    models.ImageField(default="", null=True, upload_to="images/"),
                ),
                ("content", models.TextField()),
                ("author", models.CharField(max_length=64)),
                ("slug", models.CharField(max_length=150)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
