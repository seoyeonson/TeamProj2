# Generated by Django 4.0.4 on 2022-06-08 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_order',
            name='orderstatus',
            field=models.IntegerField(choices=[(1, '주문접수'), (2, '배송준비'), (3, '출고완료'), (4, '배송중'), (5, '배송완료'), (6, '주문취소'), (7, '교환/환불대기'), (8, '교환/환불완료')]),
        ),
    ]
