# Generated by Django 2.0 on 2017-12-31 12:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20171231_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamerow',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='game',
            name='code_colour_1',
            field=models.CharField(choices=[('R', 'Red'), ('G', 'Green'), ('BU', 'Blue'), ('Y', 'Yellow'), ('W', 'White'), ('BA', 'Black')], max_length=1),
        ),
        migrations.AlterField(
            model_name='game',
            name='code_colour_2',
            field=models.CharField(choices=[('R', 'Red'), ('G', 'Green'), ('BU', 'Blue'), ('Y', 'Yellow'), ('W', 'White'), ('BA', 'Black')], max_length=1),
        ),
        migrations.AlterField(
            model_name='game',
            name='code_colour_3',
            field=models.CharField(choices=[('R', 'Red'), ('G', 'Green'), ('BU', 'Blue'), ('Y', 'Yellow'), ('W', 'White'), ('BA', 'Black')], max_length=1),
        ),
        migrations.AlterField(
            model_name='game',
            name='code_colour_4',
            field=models.CharField(choices=[('R', 'Red'), ('G', 'Green'), ('BU', 'Blue'), ('Y', 'Yellow'), ('W', 'White'), ('BA', 'Black')], max_length=1),
        ),
        migrations.AlterField(
            model_name='gamerow',
            name='guess_colour_1',
            field=models.CharField(choices=[('R', 'Red'), ('G', 'Green'), ('BU', 'Blue'), ('Y', 'Yellow'), ('W', 'White'), ('BA', 'Black')], max_length=1),
        ),
        migrations.AlterField(
            model_name='gamerow',
            name='guess_colour_2',
            field=models.CharField(choices=[('R', 'Red'), ('G', 'Green'), ('BU', 'Blue'), ('Y', 'Yellow'), ('W', 'White'), ('BA', 'Black')], max_length=1),
        ),
        migrations.AlterField(
            model_name='gamerow',
            name='guess_colour_3',
            field=models.CharField(choices=[('R', 'Red'), ('G', 'Green'), ('BU', 'Blue'), ('Y', 'Yellow'), ('W', 'White'), ('BA', 'Black')], max_length=1),
        ),
        migrations.AlterField(
            model_name='gamerow',
            name='guess_colour_4',
            field=models.CharField(choices=[('R', 'Red'), ('G', 'Green'), ('BU', 'Blue'), ('Y', 'Yellow'), ('W', 'White'), ('BA', 'Black')], max_length=1),
        ),
    ]