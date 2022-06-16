# -*- encoding: utf-8 -*-

"""Gated Residual Network (GRN) Module"""

from typing import Iterable

import tensorflow as tf
from tensorflow.keras import layers

class GatedLinearUnit(layers.Layer):

    def __init__(self, units, **kwargs) -> None:
        super(GatedLinearUnit, self).__init__()
        
        self.linear = layers.Dense(units)
        self.activation = layers.Dense(units, activation = kwargs.get("activation", "sigmoid"))


    def call(self, inputs : Iterable) -> Iterable:
        return self.linear(inputs) * self.activation(inputs)


class GatedResidualNetwork(layers.Layer):

    def __init__(self, units, dropout, **kwargs) -> None:
        super(GatedResidualNetwork, self).__init__()

        # get activation of input dense layer
        activation_ = kwargs.get("activation", "swish")

        self.units = units
        self.in_dense = layers.Dense(
            units,
            activation = activation_,
            # name = f"iGRUDense-{activation_}"
        )
        self.lin_dense = layers.Dense(units)
        self.in_dropout = layers.Dropout(dropout)

        # insert gated linear units
        self.glu = GatedLinearUnit(units)
        self.glu_norm = layers.LayerNormalization()

        self.projection = layers.Dense(units)


    def call(self, inputs : Iterable) -> Iterable:
        x = self.in_dense(inputs)
        x = self.lin_dense(x)
        x = self.in_dropout(x)

        if inputs.shape[-1] != self.units:
            inputs = self.projection(inputs)

        x = inputs + self.glu(x)
        x = self.glu_norm(x)

        return x


class VariableSelection(layers.Layer):

    def __init__(self, n, units, dropout, **kwargs) -> None:
        super(VariableSelection, self).__init__()

        # create a grn for each `n`-feature
        self.grns = [GatedResidualNetwork(units, dropout) for _ in range(n)]
        self.grns_concat = GatedResidualNetwork(units, dropout)
        self.activation = layers.Dense(n, activation = kwargs.get("activation", "softmax"))


    def call(self, inputs : Iterable) -> Iterable:
        v = layers.concatenate(inputs)
        v = self.grns_concat(v)
        v = tf.expand_dims(self.activation(v), axis = 1)

        x = []
        for idx, xs in enumerate(inputs):
            x.append(self.grns[idx](xs))

        x = tf.stack(x, axis = 1)
        outputs = tf.squeeze(tf.matmul(v, x, transpose_a = True), axis = 1)
        return outputs
