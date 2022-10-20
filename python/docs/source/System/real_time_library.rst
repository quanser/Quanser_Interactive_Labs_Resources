.. _Real_Time_Library:

Real-Time
---------

.. _realTimeDescription:

Description
^^^^^^^^^^^

The Real-Time library is a helper class to assist with spawning pre-compiled models designed to interface with QLabs.
Note that these methods assume the Quanser's QUARC has been installed on the system and the quarc_run executable is accessible.

.. _realTimeLibrary:

System Library
^^^^^^^^^^^^^^

.. autoclass:: library_qlabs_real_time.QLabsRealTime

.. _realTimeConstants:

Constants
^^^^^^^^^

This class has no public constants.


.. _realTimeMethods:

Methods
^^^^^^^

.. automethod:: library_qlabs_real_time.QLabsRealTime.start_real_time_model
.. automethod:: library_qlabs_real_time.QLabsRealTime.terminate_real_time_model
.. automethod:: library_qlabs_real_time.QLabsRealTime.terminate_all_real_time_models
