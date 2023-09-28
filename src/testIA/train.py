import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Définir le modèle CNN
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(6, activation='softmax')  # 6 classes pour les couleurs
])

# Compiler le modèle
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Prétraitement des images et augmentation des données (à adapter)
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest')

# Charger les données d'entraînement et de validation
train_generator = train_datagen.flow_from_directory(
    'chemin/vers/votre/ensemble/d-entrainement',
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical')

validation_generator = ImageDataGenerator(rescale=1./255).flow_from_directory(
    'chemin/vers/votre/ensemble/de-validation',
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical')

# Entraîner le modèle
history = model.fit(
    train_generator,
    steps_per_epoch=100,
    epochs=10,
    validation_data=validation_generator,
    validation_steps=50)

# Sauvegarder le modèle
model.save('modele_rubiks_cube.h5')

# Vous pouvez maintenant utiliser ce modèle pour prédire la couleur des stickers du Rubik's Cube en temps réel.
