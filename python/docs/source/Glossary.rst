Glossary
########

.. glossary::

    Actor
        In QLabs, an actor is any object that can be placed in the Open Worlds such as a camera,
        person, QCar, road signage, etc. Each actor class has different capabilities. 
        For a full list of actors, see the 
        :ref:`Python Actors Reference` for more details in controlling these actors in Python.

    Actor Function
        Each actor class has a series of functions that can be accessed with the container system
        using a fixed ID. The function ID's are listed as constants in each of the actor classes.

    Actor Number
        Each actor of a specific class must have a unique actor number assigned to it so it can
        be addressed for further functionality or requesting information.

    Ambient Occlusion
        This is the darkening or shading that occurs in the corners of a room as it receives less
        direct and reflected light due to the proximity of another surface. This is a graphical
        feature used to increase realism.

    Bloom
        The glow that appears around bright light sources. This is a graphical feature used to 
        increase realism.

    Class ID
        Each actor type has a fixed Class ID which is used in the container system.  See the actor
        definitions for the Class ID used.

    Configuration
        Some actors have more than one 3D model or behavior that can set during spawning. For instance, 
        the animal class has one configurations for each type of animal, but they all share the same
        functions of the animal class. See the configurations section under the Actors Reference 
        to see all configurations a particular actor class. 

    Connection Points
        Connection Points are reference frames on an actor that other actors can be attached to. 

    Container
        The communications framework to QLabs addresses each actor in the scene within a container.
        Each container holds the container size, class ID, actor number, actor function and a 
        variable-length payload that depends on the specific function called.

    CPS
        Communication Per Second. A measurement of the number of communication packets the simulation
        is processing per second.  Note that a single packet make contain one or more container
        so the packet composition must be considered when evaluating the communication efficiency.

    FPS
        Frames Per Second. This is an indication of your computer's graphical performance. A minimum
        of 30 FPS will appear as a smooth animation.

    Open World
        In QLabs, an open world is a virtual world or map where the user can move freely and create 
        and place objects to create custom scenarios. There are several different Open Worlds 
        available in QLabs for different types of products. Please 
        `contact <https://www.quanser.com/contact/>`__ a Quanser representative to find out more.

    Packet
        Communication from external scripts or models to QLabs is done with TCP/IP communications.
        This form of communications is packet-based which means the information is bundled into
        chunks of data with a known format to facilitate the transmission from your model to QLabs
        whether that be on the same PC or a computer on the other side of the world.  Each
        packet contains one or more "container" which further divides the data into messages
        for each actor.

    QCar
        The Quanser Virtual QCar is a fully instrumented, dynamically accurate digital twin of the 
        Quanser QCar system. It behaves the  same way as the physical hardware and can be measured 
        and controlled using MATLAB/Simulink or Python development environments. It can enrich your 
        lectures and activities in traditional labs, or bring credible, authentic, model-based lab 
        experiences into your distance and online self-driving course. As with the physical QCar,  
        the virtual system is a self-driving teaching and research platform complete with 
        industrially relevant sensors such as LiDAR and RGB-D cameras. See more on our
        `website <https://www.quanser.com/products/qlabs-virtual-qcar/>`__.
     
    Quanser Interactive Labs (QLabs)
        QLabs or Quanser Interactive Labs is the virtual twin for Quanser's hardware products.
        Using Quanser Interactive Labs, you get a collection of virtual hardware-based laboratory 
        activities that supplement traditional or online courses. The virtual hardware is based 
        on Quanser physical systems and offers credible, academically appropriate experiences on 
        desktops, laptops, or smart devices. See more on our 
        `website <https://www.quanser.com/digital/quanser-interactive-labs/>`__.

    Reference Frame
        Reference Frames are used to specify the relationship between a moving observer and the 
        phenomenon under observation. For instance, a robot arm would typically have a reference
        frame at each joint where the transformation from one reference frame to the next is
        determined by the joint rotations and translations.

    Refraction
        The deflection of light as it passes through one medium to another. Materials such as
        glass require reflection and refraction to accurately recreate it, but it has a high
        computational cost to accurately reproduce.

    Render
        The process of drawing an image on the screen.

    Screen Percentage Scaling
        Renders the image on the screen at a lower resolution than your monitor that scales the
        image up to fill the screen. This is a technique to improve rendering performance at
        the cost of making some details blurry in the scene.

    Self-Driving Car Studio (SDCS)
        The Self-Driving Car Studio is Quanser's autonomous vehicle research and development platform.   

    Spawn
        Creating a new instance of an actor class is called spawning. 

    Texel
        A single pixel of a texture map.

    Texture Map
        A 2D image that has been wrapped onto a 3D object. This is object used to project a greater
        level of detail onto a 3D surface with a lower computational cost that recreating the same
        details with geometry.

    Widget
        Widgets are a special class of highly performant actors. This allows thousands of dynamic 
        widgets can be spawned in the Open World, but they have the restriction that widgets cannot
        be addressed after they have been spawned. Widgets are typically used as objects to be picked
        up, transported, or interacted with.  All widgets simulate physics.

    Workspace
        A workspace in QLabs is a specific virtual environment or lab module.  This environment could either be 
        an open world or a virtual lab space with a more focused purpose.



