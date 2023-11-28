<html>
	<head>
		<title> 2.4 </title>
	</head>
	<body> 
		<?php
			print "<table cellpadding=5 border=1>\n";
			for ($y = 1; $y <= 10; $y++) {
				print "<tr>\n";
				for ($x = 1; $x <= 10; $x++) {
					print "\t<td>";
					if ($x == 1 && $y == 1) {
						print "<font color=red>+</font>";
					}
					elseif ($x == 1) {
						print "<font color=blue>$y</font>";
					}
					elseif ($y == 1) {
						print "<font color=blue>$x</font>";
					}
					else {
						print ($x + $y);
					}
					print "</td>\n";
				}
				print "</tr>\n";
			}
			print "</table>";
		?>
	</body>
</html>