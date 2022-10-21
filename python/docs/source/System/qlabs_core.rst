.. _QLabs_Core_Library:

QLabs Core Library
------------------

.. _qlabsCoreDescription:

Description
^^^^^^^^^^^

The QLabs Core library is the base library that manages all communications to the Quanser Interactive Labs 
software. Only the open and close methods are typically used. The remaining methods are for advanced usage.


.. _qlabsCoreLibrary:

QLabs Core Library
^^^^^^^^^^^^^^^^^^

.. autoclass:: library_qlabs.QuanserInteractiveLabs


.. _qlabsCoreConstants:

Constants
^^^^^^^^^

This library has no user constants.


.. _qlabsCoreMethodsBasic:

Basic Methods
^^^^^^^^^^^^^
.. automethod:: library_qlabs.QuanserInteractiveLabs.open
.. automethod:: library_qlabs.QuanserInteractiveLabs.close
.. automethod:: library_qlabs.QuanserInteractiveLabs.set_wait_for_container_timeout
.. automethod:: library_qlabs.QuanserInteractiveLabs.destroy_all_spawned_actors


.. _qlabsCoreMethodsAdvanced:

Advanced Methods
^^^^^^^^^^^^^^^^

To help manage the volume of data in the communications channel and help maintain real-time performance, the
system is built on a request/response system. In a typical control system, a request for information about the state
of the system is made from which a new output can be calculated.  This in turn is sent back to the simulation which
in turn responds with a new set of data.

Most of the library methods implemented follow this approach where the method call will package a single container into
a packet, send the request and wait for the response before proceeding. All requests are processed once each frame so 
the communications rate is directly related to the frame rate. The exception to this is when the wait_for_container 
(typically represented with the waitForConfirmation flag) is used.  Once again a single container is packaged
into a packet and sent, but if the waitForConfirmation is set to False then the method immediately returns allowing
the user code to call more non-blocking methods. If done in quick succession, then multiple packets will be received 
by QLabs and all containers received during that frame will have a return container that will be packed into a single packet.

Using non-blocking methods can significantly improve the data rate as you can now process multiple containers per
animation frame instead of just one. The approach is simple, but the disadvantage is that high volumes of data can 
exceeds the communication buffers resulting lost requests and unreliable communications. This can work well
when spawning hundreds of actors on setup, but you may find a a few actors missing when trying to spawn thousands.

A better method to improve the communication efficiency as well as ensure all communication requests are processed 
during a single animation frame is to use the queue methods.  Rather than sending container immediately, the 
container is queued. Once all the containers have been added, the queue_send is used to package the containers
into a single packet ensuring that all containers will be processed during a single animation frame. To construct a 
container for a given function, refer to the library source code. See :ref:`QLabs Communication Container` for 
details of the container class.

After the data is sent, poll the receive_new_data method to wait for the response packet. If the data exceeds
the size of a TCP/IP frame, this method may need to be called multiple times to collect the entire packet.  Once 
receive_new_data returns True, use the get_next_container method to extract the next container from the packet
until no more containers remain. To decode the contents of the container, again refer to the source code
of the respective libraries the responses. Note that containers may not return in the same order in which
they were sent.

Using these low-level communications functions adds more complexity to the communication process, but it
provides a higher level of control and optimizes the transaction process to improve the data throughput.


.. automethod:: library_qlabs.QuanserInteractiveLabs.send_container
.. automethod:: library_qlabs.QuanserInteractiveLabs.queue_add_container
.. automethod:: library_qlabs.QuanserInteractiveLabs.queue_send
.. automethod:: library_qlabs.QuanserInteractiveLabs.queue_destroy
.. automethod:: library_qlabs.QuanserInteractiveLabs.receive_new_data
.. automethod:: library_qlabs.QuanserInteractiveLabs.get_next_container
.. automethod:: library_qlabs.QuanserInteractiveLabs.wait_for_container
.. automethod:: library_qlabs.QuanserInteractiveLabs.flush_receive
.. automethod:: library_qlabs.QuanserInteractiveLabs.ping
