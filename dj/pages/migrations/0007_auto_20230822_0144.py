# Generated by Django 3.2.20 on 2023-08-22 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20230822_0133'),
    ]

    operations = [
        migrations.AddField(
            model_name='additionalimage',
            name='link',
            field=models.URLField(default='https://example.com'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='additionalimage',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='additionalimage',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='djitem',
            name='image_urls',
            field=models.TextField(blank=True, default='[]'),
        ),
        migrations.AlterField(
            model_name='djitem',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
