.. _Camera_Library:

Cameras
-------

.. _cameraDescription:

Description
^^^^^^^^^^^

Cameras in the Virtual Self Driving Car Studio are used for observing the workspace from different views and taking images.
Cameras are considered "actors" in the Virtual Self Driving Car Studio.  The camera library controls the camera actors.

A camera must be initialized first by spawning the camera in the location (or attached to the parent actor of choice) in order to use it.

See the :ref:`cameraTutorial` to get a better understanding of using cameras in the Quanser Interactive Labs.


.. _cameraLibrary:

Camera Library
^^^^^^^^^^^^^^

.. autoclass:: library_qlabs_free_camera.QLabsFreeCamera

.. _cameraConstants:

Constants
^^^^^^^^^

.. autoattribute:: library_qlabs_free_camera.QLabsFreeCamera.ID_FREE_CAMERA
.. autoattribute:: library_qlabs_free_camera.QLabsFreeCamera.FCN_FREE_CAMERA_POSSESS
.. autoattribute:: library_qlabs_free_camera.QLabsFreeCamera.FCN_FREE_CAMERA_POSSESS_ACK
.. autoattribute:: library_qlabs_free_camera.QLabsFreeCamera.FCN_FREE_CAMERA_SET_CAMERA_PROPERTIES
.. autoattribute:: library_qlabs_free_camera.QLabsFreeCamera.FCN_FREE_CAMERA_SET_CAMERA_PROPERTIES_ACK
.. autoattribute:: library_qlabs_free_camera.QLabsFreeCamera.FCN_FREE_CAMERA_SET_TRANSFORM
.. autoattribute:: library_qlabs_free_camera.QLabsFreeCamera.FCN_FREE_CAMERA_SET_TRANSFORM_ACK
.. autoattribute:: library_qlabs_free_camera.QLabsFreeCamera.FCN_FREE_CAMERA_SET_IMAGE_RESOLUTION
.. autoattribute:: library_qlabs_free_camera.QLabsFreeCamera.FCN_FREE_CAMERA_SET_IMAGE_RESOLUTION_RESPONSE
.. autoattribute:: library_qlabs_free_camera.QLabsFreeCamera.FCN_FREE_CAMERA_REQUEST_IMAGE
.. autoattribute:: library_qlabs_free_camera.QLabsFreeCamera.FCN_FREE_CAMERA_RESPONSE_IMAGE

.. _cameraMethods:

Methods
^^^^^^^

.. automethod:: library_qlabs_free_camera.QLabsFreeCamera.spawn
.. automethod:: library_qlabs_free_camera.QLabsFreeCamera.spawn_degrees
.. automethod:: library_qlabs_free_camera.QLabsFreeCamera.spawn_and_parent_with_relative_transform
.. automethod:: library_qlabs_free_camera.QLabsFreeCamera.spawn_and_parent_with_relative_transform_degrees
.. automethod:: library_qlabs_free_camera.QLabsFreeCamera.possess
.. automethod:: library_qlabs_free_camera.QLabsFreeCamera.set_camera_properties
.. automethod:: library_qlabs_free_camera.QLabsFreeCamera.set_transform
.. automethod:: library_qlabs_free_camera.QLabsFreeCamera.set_transform_degrees
.. automethod:: library_qlabs_free_camera.QLabsFreeCamera.destroy
.. automethod:: library_qlabs_free_camera.QLabsFreeCamera.ping
.. automethod:: library_qlabs_free_camera.QLabsFreeCamera.get_world_transform
.. automethod:: library_qlabs_free_camera.QLabsFreeCamera.set_image_capture_resolution
.. automethod:: library_qlabs_free_camera.QLabsFreeCamera.get_image

.. _cameraConfigs:

Configurations
^^^^^^^^^^^^^^

There are no configuration options for the camera actor.

.. _cameraConnect:

Connection Points
^^^^^^^^^^^^^^^^^

There are no connection points for the free camera actor.

.. _cameraTutorial:

Camera Tutorial
^^^^^^^^^^^^^^^

.. dropdown:: Example 1

.. dropdown:: Example 2

.. dropdown:: Example 3


.. tip:: 
  
  There is a few easy steps to initializing a new camera in an environment using the interface as well as the code:
  
  #. Pick a Location for your camera using the :ref:`Coordinate Helper (Determining Locations)` section.
  #. Copy the location and rotation desired.
  #. Use spawn or spawn_degrees to initialize a new camera. Paste the copied location and rotation into their respective places.

**See Also:** 
 