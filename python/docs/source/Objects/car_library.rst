.. _Car_Library:

QCars
-----

.. image:: ../pictures/qcar_crop_banner.png
    :scale: 120%
    :align: center

.. _carDescription:

Description
^^^^^^^^^^^

QCars are considered "actors" in Quanser Interactive Labs.The QCar library can
be used to acquire sensor data from the virtual environment and controls the
motion of the vehicles.

See the QCar :ref:`carTutorial` to get a better understanding of using QCars in
Quanser Interactive Labs.

.. _carLibrary:

Library
^^^^^^^

.. autoclass:: qvl.qcar.QLabsQCar

.. _carConstants:

Constants
^^^^^^^^^

.. autoattribute:: qvl.qcar.QLabsQCar.ID_QCAR
.. autoattribute:: qvl.qcar.QLabsQCar.CAMERA_CSI_RIGHT
.. autoattribute:: qvl.qcar.QLabsQCar.CAMERA_CSI_BACK
.. autoattribute:: qvl.qcar.QLabsQCar.CAMERA_CSI_LEFT
.. autoattribute:: qvl.qcar.QLabsQCar.CAMERA_CSI_FRONT
.. autoattribute:: qvl.qcar.QLabsQCar.CAMERA_RGB
.. autoattribute:: qvl.qcar.QLabsQCar.CAMERA_DEPTH
.. autoattribute:: qvl.qcar.QLabsQCar.CAMERA_OVERHEAD
.. autoattribute:: qvl.qcar.QLabsQCar.CAMERA_TRAILING


.. _carMemberVars:

Member Variables
^^^^^^^^^^^^^^^^

.. autoattribute:: qvl.qcar.QLabsQCar.actorNumber

.. _carMethods:

Methods
^^^^^^^

.. automethod:: qvl.qcar.QLabsQCar.__init__
.. automethod:: qvl.qcar.QLabsQCar.spawn
.. automethod:: qvl.qcar.QLabsQCar.spawn_degrees
.. automethod:: qvl.qcar.QLabsQCar.spawn_id
.. automethod:: qvl.qcar.QLabsQCar.spawn_id_degrees
.. automethod:: qvl.qcar.QLabsQCar.set_transform_and_request_state
.. automethod:: qvl.qcar.QLabsQCar.set_transform_and_request_state_degrees
.. automethod:: qvl.qcar.QLabsQCar.set_velocity_and_request_state
.. automethod:: qvl.qcar.QLabsQCar.set_velocity_and_request_state_degrees
.. automethod:: qvl.qcar.QLabsQCar.possess
.. automethod:: qvl.qcar.QLabsQCar.ghost_mode
.. automethod:: qvl.qcar.QLabsQCar.get_image
.. automethod:: qvl.qcar.QLabsQCar.get_lidar
.. automethod:: qvl.qcar.QLabsQCar.destroy
.. automethod:: qvl.qcar.QLabsQCar.destroy_all_actors_of_class
.. automethod:: qvl.qcar.QLabsQCar.ping
.. automethod:: qvl.qcar.QLabsQCar.get_world_transform
.. automethod:: qvl.qcar.QLabsQCar.get_world_transform_degrees

.. _carConfig:

Configurations
^^^^^^^^^^^^^^

There is only one configuration of the QCar actor.

.. image:: ../pictures/qcar.png
    :scale: 50%
    :align: center


.. _carConnect:

Connection Points
^^^^^^^^^^^^^^^^^

.. image:: ../pictures/qcar_connection_points.png
    :scale: 50%
    :align: center

.. table::
    :widths: 11, 11, 25, 53
    :align: center

    ====================== ============ ====================================================== ===========
    Reference Frame Number Parent Frame Relative Transform to Parent (Location, Rotation, Deg) Description
    ====================== ============ ====================================================== ===========
    0                                                                                          The base frame is located at ground level, centered between the two rear wheels. This represents the location of the car with no filtering, suspension, or dynamics. Collision detection is connected to this reference frame.
    1                      0            [0,0,0] [0,0,0]                                        The filtered frame is co-located with connection point 0, but it is a filtered position to simulated the suspension and dynamic effects. All the visual elements and sensors of the QCar are connected to this frame.
    ====================== ============ ====================================================== ===========

.. image:: ../pictures/qcar_connection_points.png


Component Extrinsics
^^^^^^^^^^^^^^^^^^^^
"Extrinsics" refer to the external relationship of an object with respect to a
specific frame of reference (in this case the body center of the QCar).
Sometimes it's important to know specific distances and orientation of
extrinsic components, for instance, this can be use for obstacle detection and
camera calibration.
You will find a list of the important extrinsics below.

Distances From Body Center
""""""""""""""""""""""""""
Distances of the QCar in its virtual environment are 10 times larger then in
real life when scaled at [1,1,1].
Therefore the distances to important components have been scaled accordingly
below to match a scale of [1,1,1]:

.. table::
    :widths: 11, 11, 11, 11
    :align: center

    ========== ====== ====== ======
    Component  x (m)  y (m)  z (m)
    ========== ====== ====== ======
    CG          0.248 -0.074  0.606
    Front axle  1.300  0      0.207
    Rear axle  -1.300  0      0.207
    CSI front   1.930  0      0.850
    CSI left    0.140  0.438  0.850
    CSI rear   -1.650  0      0.850
    CSI right   0.140 -0.674  0.850
    IMU         1.278  0.223  0.792
    RealSense   0.822  0.003  1.479
    RPLIDAR    -0.108 -0.001  1.696
    ========== ====== ====== ======

Transformation Matrices
"""""""""""""""""""""""

.. image:: ../pictures/bodyframe.png
    :scale:  65%
    :align: center

All transformation matrices are built off of the body frame and camera frames
for the QCar.
To read more about this check out our documentation
`here <https://www.quanser.com/products/self-driving-car-studio/>`__
by clicking on resources button and looking inside the zip folder for
User Guides/System Hardware.pdf

.. image:: ../pictures/qcar_extrinsic_matrices.png
    :scale:  65%
    :align: center

.. _carTutorial:

QCar Tutorial
^^^^^^^^^^^^^

.. dropdown:: Example

    Raw to download this tutorial: |qcar_tutorial1.py|.

    .. |qcar_tutorial1.py| replace::
        :download:`QCar Tutorial <../../../tutorials/qcar_tutorial1.py>`
    
    .. literalinclude:: ../../../tutorials/qcar_tutorial1.py
        :language: python
        :linenos:
    

.. **See Also:**
