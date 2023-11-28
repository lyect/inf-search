<html>
	<head>
		<title> 3.2 </title>
	</head>
	<body>
	<?php
		if (!isset ($_GET["ha"])) {
			$ha = "left";
		} else {
			$ha = $_GET["ha"];
		}

		if (!isset ($_GET["va"])) {
			$va = "top";
		} else {
			$va = $_GET["va"];
		}

		print "<table cellpadding=5 border=1 width=300 height=300>\n";
		print "\t<tr>\n";
		print "\t\t<td style='text-align: $ha; vertical-align: $va'>Aligned Text</td>\n";
		print "\t</tr>\n";
		print "</table>\n";
		print "<form action='{$_SERVER['PHP_SELF']}' method='GET'>";
	?>
		<p><b>Horizontal align</b></p>
		<p><input type="radio" name="ha" value="left">Left</p>
		<p><input type="radio" name="ha" value="center">Center</p>
		<p><input type="radio" name="ha" value="right">Right</p>
		<p><b>Vertical align</b></p>
		<p><input type="checkbox" name="va" value="top">Top</p>
		<p><input type="checkbox" name="va" value="middle">Middle</p>
		<p><input type="checkbox" name="va" value="bottom">Bottom</p>
		<p><input type="submit" value="Execute"></p>
	</form>
	</body>
</html>