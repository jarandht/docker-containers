FIELD_CHOICES = {
    'netbox_inventory.Asset.status+': (
        ('repair', 'In repair', 'orange'),
        ('til-disp', 'Til-disp', 'black')
    ),
}

CUSTOM_VALIDATORS = {
    "netbox_inventory.assets": [
        {
            "tags": {
                "required": True,
            }
        }
    ]
}