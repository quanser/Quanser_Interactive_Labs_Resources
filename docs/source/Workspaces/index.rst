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

.. _spawnableactorsWorkspaces:

Workspace Spawnable Actors
==========================

.. table::
    :widths: 11, 11, 11, 11, 11, 11, 11, 11, 11
    :align: center

    ================== ========= ============== ========= ============== ========= ======= ======= =========
    Product            Cityscape Cityscape Lite Townscape Townscape Lite Open Road Studio  Plane   Warehouse
    ================== ========= ============== ========= ============== ========= ======= ======= =========
    Cameras            Yes       Yes            Yes       Yes            Yes       Yes     Yes     Yes
    Widgets            Yes       Yes            Yes       Yes            Yes       Yes     Yes     Yes
    Animals            Yes       Yes            Yes       Yes            Yes       No      Yes     No
    People             Yes       Yes            Yes       Yes            Yes       Yes     Yes     Yes
    Basic shapes       Yes       Yes            Yes       Yes            Yes       Yes     Yes     Yes
    Splines            Yes       Yes            Yes       Yes            Yes       Yes     Yes     Yes
    Reference frames   Yes       Yes            Yes       Yes            Yes       Yes     Yes     Yes
    Shredder           No        No             No        No             No        Yes     Yes     Yes
    Weather            Yes       No             Yes       No             Yes       No      No      No
    Time of Day        Yes       No             Yes       No             Yes       No      No      No
    QCar               License   License        License   License        License   License License License
    QCar 2             License   License        License   License        License   License License License
    QBot 2e            No        No             No        No             No        License License License
    QBot 3             No        No             No        No             No        License License License
    QBot Platform      No        No             No        No             No        License License License
    QArm               No        No             No        No             No        License License License
    SRV02              No        No             No        No             No        License License License
    Product walls      No        No             No        No             No        License License License
    Product flooring   No        No             No        No             No        License License License
    Traffic light      License   License        License   License        License   License License License
    Traffic cones      License   License        License   License        License   License License License
    Crosswalks         License   License        License   License        License   License License License
    Stop sign          License   License        License   License        License   License License License
    Yield sign         License   License        License   License        License   License License License
    Roundabout sign    License   License        License   License        License   License License License
    Conveyors straight No        No             No        No             No        License License License
    ================== ========= ============== ========= ============== ========= ======= ======= =========
    
Licensed actors require an applicable product license as part of your QLabs subscription to spawn.



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
    /* the prevents the th scrolling up by the default border size before "sticking" */
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

    <h2>Responsive Table</h2>
    <p>If you have a table that is too wide, you can add a container element with overflow-x:auto around the table, and it will display a horizontal scroll bar when needed.</p>
    <p>Resize the browser window to see the effect. Try to remove the div element and see what happens to the table.</p>

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
                <td>Yes</td>
                <td>Yes</td>
                <td>Yes</td>
                <td>Yes</td>
                <td>Yes</td>
                <td>Yes</td>
                <td>Yes</td>
                <td>Yes</td>
            </tr>
            <tr>
                <td>Widgets</td>
                <td>Yes</td>
                <td>Yes</td>
                <td>Yes</td>
                <td>Yes</td>
                <td>Yes</td>
                <td>Yes</td>
                <td>Yes</td>
                <td>Yes</td>
            </tr>
            <tr>
                <td>Animals</td>
                <td>Yes</td>
                <td>Yes</td>
                <td>Yes</td>
                <td>Yes</td>
                <td>Yes</td>
                <td>No</td>
                <td>Yes</td>
                <td>No</td>
            </tr>
            <tr>
                <td>People</td>
                <td>Yes</td>
                <td>Yes</td>
                <td>Yes</td>
                <td>Yes</td>
                <td>Yes</td>
                <td>Yes</td>
                <td>Yes</td>
                <td>Yes</td>
            </tr>
            <tr>
                <td>Basic shapes</td>
                <td>Yes</td>
                <td>Yes</td>
                <td>Yes</td>
                <td>Yes</td>
                <td>Yes</td>
                <td>Yes</td>
                <td>Yes</td>
                <td>Yes</td>
            </tr>
            <tr>
                <td>Splines</td>
                <td>Yes</td>
                <td>Yes</td>
                <td>Yes</td>
                <td>Yes</td>
                <td>Yes</td>
                <td>Yes</td>
                <td>Yes</td>
                <td>Yes</td>
            </tr>
            <tr>
                <td>Reference frames</td>
                <td>Yes</td>
                <td>Yes</td>
                <td>Yes</td>
                <td>Yes</td>
                <td>Yes</td>
                <td>Yes</td>
                <td>Yes</td>
                <td>Yes</td>
            </tr>
            <tr>
                <td>Shredder</td>
                <td>No</td>
                <td>No</td>
                <td>No</td>
                <td>No</td>
                <td>No</td>
                <td>Yes</td>
                <td>Yes</td>
                <td>Yes</td>
            </tr>
            <tr>
                <td>Weather</td>
                <td>Yes</td>
                <td>No</td>
                <td>Yes</td>
                <td>No</td>
                <td>Yes</td>
                <td>No</td>
                <td>No</td>
                <td>No</td>
            </tr>
            <tr>
                <td>Time of Day</td>
                <td>Yes</td>
                <td>No</td>
                <td>Yes</td>
                <td>No</td>
                <td>Yes</td>
                <td>No</td>
                <td>No</td>
                <td>No</td>
            </tr>
            <tr>
                <td>QCar</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
            </tr>
            <tr>
                <td>QCar 2</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
            </tr>
            <tr>
                <td>QBot 2e</td>
                <td>No</td>
                <td>No</td>
                <td>No</td>
                <td>No</td>
                <td>No</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
            </tr>
            <tr>
                <td>QBot 3</td>
                <td>No</td>
                <td>No</td>
                <td>No</td>
                <td>No</td>
                <td>No</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
            </tr>
            <tr>
                <td>QBot Platform</td>
                <td>No</td>
                <td>No</td>
                <td>No</td>
                <td>No</td>
                <td>No</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
            </tr>
            <tr>
                <td>QArm</td>
                <td>No</td>
                <td>No</td>
                <td>No</td>
                <td>No</td>
                <td>No</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
            </tr>
            <tr>
                <td>SRV02</td>
                <td>No</td>
                <td>No</td>
                <td>No</td>
                <td>No</td>
                <td>No</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
            </tr>
            <tr>
                <td>Product walls</td>
                <td>No</td>
                <td>No</td>
                <td>No</td>
                <td>No</td>
                <td>No</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
            </tr>
            <tr>
                <td>Product flooring</td>
                <td>No</td>
                <td>No</td>
                <td>No</td>
                <td>No</td>
                <td>No</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
            </tr>
            <tr>
                <td>Traffic light</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
            </tr>
            <tr>
                <td>Traffic cones</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
            </tr>
            <tr>
                <td>Crosswalks</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
            </tr>
            <tr>
                <td>Stop sign</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
            </tr>
            <tr>
                <td>Yield sign</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
            </tr>
            <tr>
                <td>Roundabout sign</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
            </tr>
            <tr>
                <td>Conveyors straight</td>
                <td>No</td>
                <td>No</td>
                <td>No</td>
                <td>No</td>
                <td>No</td>
                <td>License</td>
                <td>License</td>
                <td>License</td>
            </tr>
        </tbody>
    </table>
    </div>


    <h2>SUPER TABLE 2</h2>
    <p>If you have a table that is too wide, you can add a container element with overflow-x:auto around the table, and it will display a horizontal scroll bar when needed.</p>
    <p>Resize the browser window to see the effect. Try to remove the div element and see what happens to the table.</p>

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
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
        </tr>
        <tr>
            <td>QCar 2</td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
        </tr>
        <tr>
            <td>QBot 2e</td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
        </tr>
        <tr>
            <td>QBot 3</td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
        </tr>
        <tr>
            <td>QBot Platform</td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
        </tr>
        <tr>
            <td>QArm</td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
        </tr>
        <tr>
            <td>SRV02</td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
        </tr>
        <tr>
            <td>Product walls</td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
        </tr>
        <tr>
            <td>Product flooring</td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
        </tr>
        <tr>
            <td>Traffic light</td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
        </tr>
        <tr>
            <td>Traffic cones</td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
        </tr>
        <tr>
            <td>Crosswalks</td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
        </tr>
        <tr>
            <td>Stop sign</td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
        </tr>
        <tr>
            <td>Yield sign</td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
        </tr>
        <tr>
            <td>Roundabout sign</td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
        </tr>
        <tr>
            <td>Conveyors straight</td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
            <td><i class="fa fa-asterisk"></i></td>
        </tr>
    </tbody>
    </table>
    </div>

    <br>
    <br>
    <br>

    </body>
    </html>


