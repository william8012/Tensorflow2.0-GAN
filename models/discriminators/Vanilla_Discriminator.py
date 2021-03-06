from easydict import EasyDict as edict

from tensorflow.python.keras import Input
from tensorflow.python.keras import Model
from tensorflow.python.keras import layers


from models import model
class VanillaDiscriminator(model.Model):
  def __init__(self, model_parameters: edict):
    super().__init__(model_parameters)
  

  def define_model(self):
    input_img = Input(shape=[
        self.model_parameters.img_height,
        self.model_parameters.img_width,
        self.model_parameters.num_channels,
    ])

    x = layers.Conv2D(filters=64, kernel_size=(5, 5), strides=(2, 2), padding='same')(input_img)
    x = layers.LeakyReLU()(x)
    x = layers.Dropout(0.3)(x)

    x = layers.Conv2D(filters=128, kernel_size=(5, 5), strides=(2, 2), padding='same')(x)
    x = layers.LeakyReLU()(x)
    x = layers.Dropout(rate=0.3)(x)

    x = layers.Flatten()(x)
    x = layers.Dense(units=1)(x)
    model = Model(name='VanillaDiscriminator', inputs=input_img, outputs=x)

    return model

  