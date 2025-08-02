A.Compose([
    A.Resize(224, 224),
    A.HorizontalFlip(),
    A.RandomBrightnessContrast(),
    A.Rotate(limit=30),
    A.Normalize()
])
