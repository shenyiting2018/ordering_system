# Generated by Django 4.0.6 on 2022-08-02 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("seckill", "0003_alter_seckillcampaign_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Commodity",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("commodity_name", models.CharField(max_length=50)),
                ("commodity_description", models.CharField(max_length=1000)),
                ("commodity_price", models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name="seckillcampaign",
            name="commodity",
            field=models.ForeignKey(
                default=-1,
                on_delete=django.db.models.deletion.CASCADE,
                to="seckill.commodity",
            ),
            preserve_default=False,
        ),
    ]
