# Generated by Django 4.0.4 on 2022-06-12 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_company_id_alter_notification_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='companies',
            field=models.ManyToManyField(null=True, related_name='requests', related_query_name='request', to='main.company', verbose_name='Companies'),
        ),
    ]
