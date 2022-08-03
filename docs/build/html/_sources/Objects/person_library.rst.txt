.. _Person_Library:

Person
------

.. _personDescription: 

Description
^^^^^^^^^^^

People are considered "actors" in the Virtual Self Driving Car Studio.  
The person library controls the people placed in the Virtual Self Driving Car Studio workspaces of the Quanser Interactive Labs.

See the tutorial to get a better understanding of using cameras in the Quanser Interactive Labs.

.. _personlibrary:

Library
^^^^^^^

.. autoclass:: library_qlabs_silhouette_person.QLabsSilhouettePerson

.. _personConstants:

Constants
^^^^^^^^^

.. autoattribute:: library_qlabs_silhouette_person.QLabsSilhouettePerson.ID_SILHOUETTE_PERSON
.. autoattribute:: library_qlabs_silhouette_person.QLabsSilhouettePerson.FCN_SILHOUETTE_PERSON_MOVE_TO
.. autoattribute:: library_qlabs_silhouette_person.QLabsSilhouettePerson.FCN_SILHOUETTE_PERSON_MOVE_TO_ACK

.. _personMethods:

Methods
^^^^^^^

.. automethod:: library_qlabs_silhouette_person.QLabsSilhouettePerson.spawn
.. automethod:: library_qlabs_silhouette_person.QLabsSilhouettePerson.spawn_degrees
.. automethod:: library_qlabs_silhouette_person.QLabsSilhouettePerson.move_to

.. _personConfig:

Configurations
^^^^^^^^^^^^^^

There are several configurations for a person generated in the Quanser Interactive Labs.

.. image:: pictures/people.png 

.. _personConnect:

Connection Points
^^^^^^^^^^^^^^^^^

.. _personTutorial:

Tutorial
^^^^^^^^

.. dropdown:: Example 1

.. dropdown:: Example 2

.. dropdown:: Example 3

**See Also:**




.. code-block:: python
    :caption: Spawning a Person 

    QLabsSilhouettePerson().spawn(qlabs, deviceNumber, location, rotation, scale, configuration=0, waitForConfirmation=True)

.. code-block:: python
    :caption: Spawning a Person using Degrees

    QLabsSilhouettePerson().spawn_degrees(qlabs, deviceNumber, location, rotation, scale, configuration=0, waitForConfirmation=True)

.. code-block:: python
    :caption: Making the Person to move to a secondary location

    QLabsSilhouettePerson().move_to(qlabs, deviceNumber, location, speed, waitForConfirmation=True)

