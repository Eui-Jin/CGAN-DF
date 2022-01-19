import tensorflow as tf
from tensorflow.keras.layers import Layer
import sys


def gumbel_distribution(input_shape):
    """Samples a tensor from a Gumbel distribution.
    Args:
        input_shape (tuple): Shape of tensor to be sampled.
    Returns:
        An input_shape tensor sampled from a Gumbel distribution.
    """

    # Samples an uniform distribution based on the input shape
    uniform_dist = tf.random.uniform(input_shape, 0, 1)

    # Samples from the Gumbel distribution
    gumbel_dist = -1 * tf.math.log(-1 * tf.math.log(uniform_dist +  sys.float_info.epsilon) +  sys.float_info.epsilon)

    return gumbel_dist


class GumbelSoftmax(Layer):
    """A GumbelSoftmax class is the one in charge of a Gumbel-Softmax layer implementation.
    References:
        E. Jang, S. Gu, B. Poole. Categorical reparameterization with gumbel-softmax.
        Preprint arXiv:1611.01144 (2016).
    """

    def __init__(self, axis=-1, **kwargs):
        """Initialization method.
        Args:
            axis (int): Axis to perform the softmax operation.
        """

        # Overrides its parent class with any custom arguments if needed
        super(GumbelSoftmax, self).__init__(**kwargs)

        # Defining a property for holding the intended axis
        self.axis = axis

    def call(self, inputs, tau):
        """Method that holds vital information whenever this class is called.
        Args:
            x (tf.Tensor): A tensorflow's tensor holding input data.
            tau (float): Gumbel-Softmax temperature parameter.
        Returns:
            Gumbel-Softmax output and its argmax token.
        """

        # Adds a sampled Gumbel distribution to the input
        x = inputs + gumbel_distribution(tf.shape(inputs))

        # Applying the softmax over the Gumbel-based input
        x = tf.nn.softmax(x / tau, self.axis)

        return x

    def get_config(self):
        """Gets the configuration of the layer for further serialization.
        """

        # Defining a dictionary holding the configuration
        config = {'axis': self.axis}

        # Overring the base configuration
        base_config = super(GumbelSoftmax, self).get_config()

        return dict(list(base_config.items()) + list(config.items()))