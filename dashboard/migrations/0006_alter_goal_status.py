# Generated by Django 4.0.4 on 2022-05-30 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_goal_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='status',
            field=models.CharField(choices=[('В процесі', 'В процесі'), ('Виконано', 'Виконано'), ('Відхилено', 'Відхилено')], default='В процесі', max_length=50),
        ),
    ]