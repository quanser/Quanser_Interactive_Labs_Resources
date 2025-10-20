.. _Workspaces:

**********
Workspaces
**********

Workspaces in QLabs are specific virtual environments or lab modules.
This environment could either be an open world or a virtual lab space with a
more focused purpose. An Open World is a virtual world or map where the user
can move freely and create and place objects to create custom scenarios.
There are several different Open Worlds available in QLabs for different types
of products.

Device Communication
========================

For port numbers to communicate with the devices in their respective workspaces, see below:

.. toctree::
   :maxdepth: 1

   port_numbers.rst
     
..

Workspaces
============

.. toctree::
   :maxdepth: 1

   Cityscape.rst
   Cityscape_Lite.rst
   Townscape.rst
   Townscape_Lite.rst
   Open_Road.rst
   Plane.rst
   Studio.rst
   Warehouse.rst
..


.. _openWorkspaceFromCommandLine:

Opening Workspaces from the Command Line
========================================

QLabs and any of the Open Worlds can be opened directly from your scripts by
using the command switch ``-loadmodule`` followed by the module name.  For
example on Windows:

``"%QUARC_DIR%\..\Quanser Interactive Labs\Quanser Interactive Labs.exe" -loadmodule Cityscape``

See the individual workspace pages for the corresponding command line name.

If you have not logged into QLabs previously or you did not save the user
credentials then you will be required to enter this information before the
module is loaded. If you are not licensed for the specified module then
the ``-loadmodule`` command will be ignored.


.. _spawnableactorsWorkspaces:

Workspace Spawnable Actors
==========================


.. raw:: html

    <html>
    <head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>

    thead {
    border-bottom: 2px solid rgb(160 160 160);
    text-align: center;
    background-color: #ffffff;
    color: #000000;
    }

    table {
    table-layout: fixed;
    width: 100%;
    /* This prevents the scrolling up by the default border size before "sticking" */
    border-collapse: separate;
    border-spacing: 0;
    }

    table th {
    /* Apply both top and bottom borders to the <th> */
    border-top: 1px solid #E1E4E5;
    border-bottom: 1px solid #E1E4E5;
    border-right: 1px solid #E1E4E5;
    }

    table td {
    /* For cells, apply the border to one of each side only (right but not left, bottom but not top) */
    border-bottom: 1px solid #E1E4E5;
    border-right: 1px solid #E1E4E5;
    }

    table th:first-child,
    table td:first-child {
    /* Apply a left border on the first <td> or <th> in a row */
    border-left: 1px solid #E1E4E5;
    }


    th, td {
    width: 100px;
    min-width: 100px;
    }

    th {
    position: sticky;
    top: 0;
    background: #FFF;
    
    }

    th, td {
    text-align: left;
    padding: 8px;
    }

    tbody td:first-child {
    position: sticky;
    left: 0;
    background-color: #ffffff; /* Adjust as needed */
    z-index: 2; /* Ensure it's above other content */
    }

    thead th:first-child {
    position: sticky;
    left: 0;
    background-color: #ffffff; /* Adjust as needed */
    z-index: 4; /* Ensure it's above other content */
    }

    tbody tr:nth-child(odd){background-color: #f3f6f6}
    tbody tr:nth-child(even){background-color: #f2f2f2}

    .fa-check {
    color: green;
    }

    .fa-remove {
    color: red;
    }

    .fa-question {
    color: black;
    }
    
    </style>
    
    </head>
    <body>

    <div style="height:500px; overflow: auto;">
    <table>
    <thead>
        <tr>
            <th>Product</th>
            <th>Cityscape</th>
            <th>Cityscape Lite</th>
            <th>Townscape</th>
            <th>Townscape Lite</th>
            <th>Open Road</th>
            <th>Studio</th>
            <th>Plane</th>
            <th>Warehouse</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Cameras</td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
        </tr>
        <tr>
            <td>Widgets</td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
        </tr>
        <tr>
            <td>Animals</td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-remove"></i></td>
        </tr>
        <tr>
            <td>People</td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
        </tr>
        <tr>
            <td>Basic shapes</td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
        </tr>
        <tr>
            <td>Splines</td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
        </tr>
        <tr>
            <td>Reference frames</td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
        </tr>
        <tr>
            <td>Shredder</td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
        </tr>
        <tr>
            <td>Weather</td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
        </tr>
        <tr>
            <td>Time of Day</td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
        </tr>
        <tr>
            <td>QCar</td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
        </tr>
        <tr>
            <td>QCar 2</td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
        </tr>
        <tr>
            <td>QBot Platform</td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-check"></i></td>
        </tr>
        <tr>
            <td>QArm</td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
        </tr>
        <tr>
            <td>Product walls</td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
        </tr>
        <tr>
            <td>Product flooring</td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
        </tr>
        <tr>
            <td>Traffic light</td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-remove"></i></td>
        </tr>
        <tr>
            <td>Traffic cones</td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-remove"></i></td>
        </tr>
        <tr>
            <td>Crosswalks</td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-remove"></i></td>
        </tr>
        <tr>
            <td>Stop sign</td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-remove"></i></td>
        </tr>
        <tr>
            <td>Yield sign</td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-remove"></i></td>
        </tr>
        <tr>
            <td>Roundabout sign</td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-check"></i></td>
            <td><i class="fa fa-remove"></i></td>
        </tr>
    </tbody>
    </table>
    </div>

    <br>
    Quanser Products are licensed and require an applicable product license as part of your QLabs subscription to spawn. <br>

    * Custom solutions are available, please contact Quanser (https://www.quanser.com/contact-us/) for more information.

    <br>
    <br>
    <br>

    </body>
    </html>


