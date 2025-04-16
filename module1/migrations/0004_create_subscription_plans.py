

from django.db import migrations

def create_subscription_plans(apps, schema_editor):
    SubscriptionPlan = apps.get_model('your_app_name', 'SubscriptionPlan')
    
    # Create Free plan
    SubscriptionPlan.objects.create(
        name='free',
        price=0,
        download_limit=5,  # Limited download for free tier
        has_enhanced_support=False,
        has_enhanced_catalog=False
    )
    
    # Create Standard plan
    SubscriptionPlan.objects.create(
        name='standard',
        price=300,
        download_limit=50,  # 50 GB limit
        has_enhanced_support=True,
        has_enhanced_catalog=False
    )
    
    # Create Premium plan
    SubscriptionPlan.objects.create(
        name='premium',
        price=500,
        download_limit=None,  # No limit (None)
        has_enhanced_support=True,
        has_enhanced_catalog=True
    )

def delete_subscription_plans(apps, schema_editor):
    SubscriptionPlan = apps.get_model('your_app_name', 'SubscriptionPlan')
    SubscriptionPlan.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('your_app_name', '0003_initial'),  # Adjusted to reference migration 0003
    ]

    operations = [
        migrations.RunPython(create_subscription_plans, delete_subscription_plans),
    ]
