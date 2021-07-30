import tensorflow as tf
import tensorflow_addons as tfa
from GNN_NIDS_tensorflow.GNN import GNN
import os


def _get_compiled_model(params):
    model = GNN(params)
    decayed_lr = tf.keras.optimizers.schedules.ExponentialDecay(float(params['HYPERPARAMETERS']['learning_rate']),
                                                                int(params['HYPERPARAMETERS']['decay_steps']),
                                                                float(params['HYPERPARAMETERS']['decay_rate']),
                                                                staircase=True)

    optimizer = tf.keras.optimizers.Adam(learning_rate=decayed_lr)
    loss_object = tf.keras.losses.CategoricalCrossentropy()
    metrics = [tf.keras.metrics.CategoricalAccuracy(), tf.keras.metrics.SpecificityAtSensitivity(0.1),
               tf.keras.metrics.Recall(top_k=1,class_id=0, name='rec_0'), tf.keras.metrics.Precision(top_k=1, class_id=0, name='pre_0'),
               tf.keras.metrics.Recall(top_k=1,class_id=1, name='rec_1'), tf.keras.metrics.Precision(top_k=1,class_id=1, name='pre_1'),
               tf.keras.metrics.Recall(top_k=1,class_id=2, name='rec_2'), tf.keras.metrics.Precision(top_k=1,class_id=2, name='pre_2'),
               tf.keras.metrics.Recall(top_k=1,class_id=3, name='rec_3'), tf.keras.metrics.Precision(top_k=1,class_id=3, name='pre_3'),
               tf.keras.metrics.Recall(top_k=1,class_id=4, name='rec_4'), tf.keras.metrics.Precision(top_k=1,class_id=4, name='pre_4'),
               tf.keras.metrics.Recall(top_k=1,class_id=5, name='rec_5'), tf.keras.metrics.Precision(top_k=1,class_id=5, name='pre_5'),
               tf.keras.metrics.Recall(top_k=1,class_id=6, name='rec_6'), tf.keras.metrics.Precision(top_k=1,class_id=6, name='pre_6'),
               tf.keras.metrics.Recall(top_k=1,class_id=7, name='rec_7'), tf.keras.metrics.Precision(top_k=1,class_id=7, name='pre_7'),
               tf.keras.metrics.Recall(top_k=1,class_id=8, name='rec_8'), tf.keras.metrics.Precision(top_k=1,class_id=8, name='pre_8'),
               tf.keras.metrics.Recall(top_k=1,class_id=9, name='rec_9'), tf.keras.metrics.Precision(top_k=1,class_id=9, name='pre_9'),
               tf.keras.metrics.Recall(top_k=1,class_id=10, name='rec_10'), tf.keras.metrics.Precision(top_k=1, class_id=10, name='pre_10'),
               tf.keras.metrics.Recall(top_k=1,class_id=11, name="rec_11"), tf.keras.metrics.Precision(top_k=1, class_id=11, name="pre_11"),
               tf.keras.metrics.Recall(top_k=1,class_id=12, name="rec_12"), tf.keras.metrics.Precision(top_k=1, class_id=12, name='prec_12'),
               tf.keras.metrics.Recall(top_k=1,class_id=13, name='rec_13'), tf.keras.metrics.Precision(top_k=1, class_id=13, name='prec_13'),
               tf.keras.metrics.Recall(top_k=1,class_id=14, name='rec_14'), tf.keras.metrics.Precision(top_k=1, class_id=14, name='prec_14'),
               tfa.metrics.F1Score(15,average='macro',name='macro_F1'),tfa.metrics.F1Score(15,average='weighted',name='weighted_F1')]

    model.compile(loss=loss_object,
                  optimizer=optimizer,
                  metrics= metrics,
                  run_eagerly=False)
    return model


def make_model(params):
    print("Creating a new model")
    return _get_compiled_model(params)