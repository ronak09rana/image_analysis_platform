# Generated by Django 3.2.23 on 2023-12-29 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('image_api', '0002_alter_analyzedimage_analysis_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='image_api.analyzedimage'),
        ),
    ]