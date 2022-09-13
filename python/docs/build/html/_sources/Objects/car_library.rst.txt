.. _car_library:

QCars
-----

.. image:: ../pictures/qcar.png
    :scale: 25%
    :align: center

.. _carDescription: 

Description
^^^^^^^^^^^

QCars are considered "actors" in the Virtual Self-Driving Car Studio.
The QCar library can be used to acquire sensor data from the virtual environment and controls the motion of the vehicles.

.. _carLibrary:

Library
^^^^^^^

.. autoclass:: library_qlabs_qcar.QLabsQCar

.. _carConstants:

Constants
^^^^^^^^^

.. literalinclude:: ../../../libraries/library_qlabs_qcar.py
   :language: python
   :lines: 16,45-50

.. code-block:: python

    ID_QCAR = 160 #Class ID
    FCN_QCAR_SET_VELOCITY_AND_REQUEST_STATE = 10
    FCN_QCAR_VELOCITY_STATE_RESPONSE = 11
    FCN_QCAR_SET_TRANSFORM_AND_REQUEST_STATE = 12
    FCN_QCAR_TRANSFORM_STATE_RESPONSE = 13
    FCN_QCAR_POSSESS = 20
    FCN_QCAR_POSSESS_ACK = 21
    FCN_QCAR_CAMERA_DATA_REQUEST = 100
    FCN_QCAR_CAMERA_DATA_RESPONSE = 101
    CAMERA_CSI_RIGHT = 0
    CAMERA_CSI_BACK = 1
    CAMERA_CSI_LEFT = 2
    CAMERA_CSI_FRONT = 3
    CAMERA_RGB = 4
    CAMERA_DEPTH = 5
    CAMERA_OVERHEAD = 6 #Note: The mouse scroll wheel can be used to zoom in and out in this mode.
    CAMERA_TRAILING = 7 #Note: The mouse scroll wheel can be used to zoom in and out in this mode.



.. autoattribute:: library_qlabs_qcar.QLabsQCar.ID_QCAR
.. 
 autoattribute:: library_qlabs_qcar.QLabsQCar.FCN_QCAR_SET_VELOCITY_AND_REQUEST_STATE
.. 
 autoattribute:: library_qlabs_qcar.QLabsQCar.FCN_QCAR_VELOCITY_STATE_RESPONSE
.. 
 autoattribute:: library_qlabs_qcar.QLabsQCar.FCN_QCAR_SET_TRANSFORM_AND_REQUEST_STATE
.. 
 autoattribute:: library_qlabs_qcar.QLabsQCar.FCN_QCAR_TRANSFORM_STATE_RESPONSE
.. 
 autoattribute:: library_qlabs_qcar.QLabsQCar.FCN_QCAR_POSSESS
.. 
 autoattribute:: library_qlabs_qcar.QLabsQCar.FCN_QCAR_POSSESS_ACK
.. 
 autoattribute:: library_qlabs_qcar.QLabsQCar.FCN_QCAR_CAMERA_DATA_REQUEST
.. 
 autoattribute:: library_qlabs_qcar.QLabsQCar.FCN_QCAR_CAMERA_DATA_RESPONSE
.. autoattribute:: library_qlabs_qcar.QLabsQCar.CAMERA_CSI_RIGHT
.. autoattribute:: library_qlabs_qcar.QLabsQCar.CAMERA_CSI_BACK
.. autoattribute:: library_qlabs_qcar.QLabsQCar.CAMERA_CSI_LEFT
.. autoattribute:: library_qlabs_qcar.QLabsQCar.CAMERA_CSI_FRONT
.. autoattribute:: library_qlabs_qcar.QLabsQCar.CAMERA_RGB
.. autoattribute:: library_qlabs_qcar.QLabsQCar.CAMERA_DEPTH
.. autoattribute:: library_qlabs_qcar.QLabsQCar.CAMERA_OVERHEAD
.. autoattribute:: library_qlabs_qcar.QLabsQCar.CAMERA_TRAILING

.. _carMethods:

Methods
^^^^^^^

.. automethod:: library_qlabs_qcar.QLabsQCar.spawn_id
.. automethod:: library_qlabs_qcar.QLabsQCar.spawn_id_degrees
.. automethod:: library_qlabs_qcar.QLabsQCar.set_transform_and_request_state
.. automethod:: library_qlabs_qcar.QLabsQCar.set_transform_and_request_state_degrees
.. automethod:: library_qlabs_qcar.QLabsQCar.set_velocity_and_request_state
.. automethod:: library_qlabs_qcar.QLabsQCar.set_velocity_and_request_state_degrees
.. automethod:: library_qlabs_qcar.QLabsQCar.possess
.. automethod:: library_qlabs_qcar.QLabsQCar.ghost_mode
.. automethod:: library_qlabs_qcar.QLabsQCar.get_image
.. automethod:: library_qlabs_qcar.QLabsQCar.get_lidar
.. automethod:: library_qlabs_qcar.QLabsQCar.destroy
.. automethod:: library_qlabs_qcar.QLabsQCar.ping
.. automethod:: library_qlabs_qcar.QLabsQCar.get_world_transform
.. automethod:: library_qlabs_qcar.QLabsQCar.get_world_transform_degrees

.. _carConfig:

Configurations
^^^^^^^^^^^^^^

There are no configurations options for the QCar.

.. _carConnect:

Connection Points
^^^^^^^^^^^^^^^^^

.. image:: ../pictures/qcar_connection_points.png
    :scale: 50%
    :align: center
	
.. .. list-table
..    :widths: 10, 10, 30, 50
..    :header-rows: 1
.. 
..    * - Reference Frame Number
..      - Parent Frame
..      - Relative Transform to Parent (Location, Rotation, Deg)
..      - Description
..    * - 0
..      - 
..      - 
..      - The base frame is located at ground level, centered between the two rear wheels. This represents the location of the car with no filtering, suspension, or dynamics. Collision detection is connected to this reference frame.
..    * - 1
..      - 0
..      - [0,0,0] [0,0,0]
..      - The filtered frame is co-located with connection point 0, but it is a filtered position to simulated the suspension and dynamic effects. All the visual elements and sensors of the QCar are connected to this frame.

.. table::
    :widths: 11, 11, 25, 53
    :align: center

    ====================== ============ ====================================================== ===========
    Reference Frame Number Parent Frame Relative Transform to Parent (Location, Rotation, Deg) Description
    ====================== ============ ====================================================== ===========
    0                                                                                          The base frame is located at ground level, centered between the two rear wheels. This represents the location of the car with no filtering, suspension, or dynamics. Collision detection is connected to this reference frame. 
    1                      0            [0,0,0] [0,0,0]                                        The filtered frame is co-located with connection point 0, but it is a filtered position to simulated the suspension and dynamic effects. All the visual elements and sensors of the QCar are connected to this frame.
    ====================== ============ ====================================================== ===========


.. _carTutorial:

Tutorial
^^^^^^^^

.. dropdown:: Example 1

.. dropdown:: Example 2

.. dropdown:: Example 3


Driving Cars
^^^^^^^^^^^^

**See Also:**
