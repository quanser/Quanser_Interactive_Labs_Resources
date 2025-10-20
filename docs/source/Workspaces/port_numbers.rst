.. _Workspaces:

**********
Workspaces
**********


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
    color: rgb(121, 16, 16);
    }

    .fa-question {
    color: black;
    }

    </style>

    </head>
    <body>

    <div style="height:700px; overflow: auto;">
    <table>
        <colgroup>
           <col style="width:130px">
           <col style="width:145px">
           <col style="width:110px">
           <col style="width:80px">
           <col style="width:80px">
           <col style="width:90px">
           <col style="width:90px">
       </colgroup>


    <thead>
        <tr>
            <th>Product</th>
            <th>HIL Port</th>
            <th>Video2D Port</th>
            <th>Video3D Port</th>
            <th>Lidar Port</th>
            <th>Location (GPS/ OptiTrack)</th>
            <th>Other</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>QArm</td>
            <td>18900</td>
            <td><i class="fa fa-remove"></i></td>
            <td>18901</td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
        </tr>
        <tr>
            <td>QBot 2e</td>
            <td>18910</td>
            <td><i class="fa fa-remove"></i></td>
            <td>18911</td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
        </tr>
        <tr>
            <td>QBot 3</td>
            <td>18910</td>
            <td><i class="fa fa-remove"></i></td>
            <td>18911</td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
        </tr>
        <tr>
            <td>QBot Platform</td>
            <td>18914</td>
            <td>18915</td>
            <td>18917</td>
            <td>18918</td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
        </tr>
        <tr>
            <td>Coupled Tanks</td>
            <td>18950</td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
        </tr>
        <tr>
            <td>Rotary Servo (SRV02) Base</td>
            <td>
                <strong>Base:</strong> 18940<br>
                <strong>Flexible Link:</strong> 18941<br>
                <strong>Ball &amp; Beam:</strong> 18942<br>
                <strong>Pendulum:</strong> 18943
            </td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
        </tr>
        <tr>
            <td>QUBE-Servo 2</td>
            <td>
                <strong>Disc:</strong> 18920<br>
                <strong>Pendulum:</strong> 18921
            </td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
        </tr>
        <tr>
            <td>Qube-Servo 3</td>
            <td>
                <strong>Disc:</strong> 18922<br>
                <strong>Pendulum:</strong> 18923
            </td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
        </tr>
        <tr>
            <td>Aero</td>
            <td>18930</td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
        </tr>
        <tr>
            <td>Aero 2</td>
            <td>18950</td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
            <td><i class="fa fa-remove"></i></td>
        </tr>
        <tr>
            <td>QCar & QCar 2</td>
            <td>18960</td>
            <td>
                <strong>Right:</strong> 18940<br>
                <strong>Back:</strong> 18941<br>
                <strong>Front:</strong> 18942<br>
                <strong>Left:</strong> 18943
            </td>
            <td>18965</td>
            <td>18966</td>
            <td><strong>GPS:</strong> 18967</td>
            <td><strong>QCar 2 LED Strip:</strong> 18969</td>
        </tr>
        <tr>
            <td>QDrone 2</td>
            <td>18981</td>
            <td>
                <strong>Right:</strong>18982<br>
                <strong>Back:</strong> 18983<br>
                <strong>Front:</strong> 18984<br>
                <strong>Left:</strong> 18985
            </td>
            <td>18986</td>
            <td><i class="fa fa-remove"></i></td>
            <td><strong>OptiTrack:</strong> 18967</td>
            <td><i class="fa fa-remove"></i></td>
        </tr>
    </tbody>
    </table>
    </div>

    <br>
    <br>
    <br>

    </body>
    </html>


