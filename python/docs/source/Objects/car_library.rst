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

.. autoattribute:: library_qlabs_qcar.QLabsQCar.ID_QCAR
.. autoattribute:: library_qlabs_qcar.QLabsQCar.CAMERA_CSI_RIGHT
.. autoattribute:: library_qlabs_qcar.QLabsQCar.CAMERA_CSI_BACK
.. autoattribute:: library_qlabs_qcar.QLabsQCar.CAMERA_CSI_LEFT
.. autoattribute:: library_qlabs_qcar.QLabsQCar.CAMERA_CSI_FRONT
.. autoattribute:: library_qlabs_qcar.QLabsQCar.CAMERA_RGB
.. autoattribute:: library_qlabs_qcar.QLabsQCar.CAMERA_DEPTH
.. autoattribute:: library_qlabs_qcar.QLabsQCar.CAMERA_OVERHEAD
.. autoattribute:: library_qlabs_qcar.QLabsQCar.CAMERA_TRAILING


.. _carMemberVars:

Member Variables
^^^^^^^^^^^^^^^^

.. autoattribute:: library_qlabs_qcar.QLabsQCar.actorNumber

.. _carMethods:

Methods
^^^^^^^

.. automethod:: library_qlabs_qcar.QLabsQCar.__init__
.. automethod:: library_qlabs_qcar.QLabsQCar.spawn
.. automethod:: library_qlabs_qcar.QLabsQCar.spawn_degrees
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
.. automethod:: library_qlabs_qcar.QLabsQCar.destroy_all_actors_of_class
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
