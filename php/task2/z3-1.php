<html>
	<head>
		<title> 2.3 </title>
	</head>
	<body> 
		<?php
			print "<table cellpadding=5 border=1>\n";
			$y=1;
			while ($y <= 10) {
				$x = 1;
				print "<tr>\n";
				while ($x <= 10) {
					if ($x == $y) {
						print "\t<td bgcolor=silver>";
					}
					else {
						print "\t<td>";
					}
					print ($x*$y);
					print "</td>\n";
					$x++;
				}
				print "</tr>\n";
				$y++;
			}
			print "</table>";
		?>
	</body>
</html>