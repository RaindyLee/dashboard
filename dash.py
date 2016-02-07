<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <link rel="stylesheet" type="text/css" href="style.css">
    <title>Dashboard Control Panel</title>
</head>

<body>
    <script type="text/javascript" src="/webiopi.js"></script>
    <script type="text/javascript">
    function relayOff_1() {
        webiopi().callMacro("relayOff_1");
    }

    function relayOn_1() {
        webiopi().callMacro("relayOn_1");
    }

    function relayOff_2() {
        webiopi().callMacro("relayOff_2");
    }

    function relayOn_2() {
        webiopi().callMacro("relayOn_2");
    }

    function relayOff_3() {
        webiopi().callMacro("relayOff_3");
    }

    function relayOn_3() {
        webiopi().callMacro("relayOn_3");
    }

    function relayOff_4() {
        webiopi().callMacro("relayOff_4");
    }

    function relayOn_4() {
        webiopi().callMacro("relayOn_4");
    }

    function relayOff_n() {
        webiopi().callMacro("relayOff_n");
    }

    function easterEgg() {
        webiopi().callMacro("easterEgg");
    }

    </script>

    <div id="controls" align="center"></div>
    <center><h1>Your Dashboard</h1></center>
    <!-- Relay_1 -->
    <h3>Relay 1</h3>
    <button class="myButton" onclick="relayOff_1()">Turn Off Relay_1</button>
    <button class="myButtonOn" onclick="relayOn_1()">Turn On Relay_1</button>
    <!-- Relay_2 -->
    <h3>Relay 2</h3>
    <button class="myButton" onclick="relayOff_2()">Turn Off Relay_2</button>
    <button class="myButtonOn" onclick="relayOn_2()">Turn On Relay_2</button>
    <!-- Relay_3 -->
    <h3>Relay 3</h3>
    <button class="myButton" onclick="relayOff_3()">Turn Off Relay_3</button>
    <button class="myButtonOn" onclick="relayOn_3()">Turn On Relay_3</button>
    <!-- Relay_4 -->
    <h3>Relay 4</h3>
    <button class="myButton" onclick="relayOff_4()">Turn Off Relay_4</button>
    <button class="myButtonOn" onclick="relayOn_4()">Turn On Relay_4</button>
    <!-- All -->
    <!-- <h3>All Relays</h3> -->
    <!-- <button class="myButton" onclick="relayOff_n()">Turn Off all Relays</button> -->
    <!-- <button class="myButton" onclick="relayOn_n()">Turn On all Relays</button> -->

</body>
</html>
