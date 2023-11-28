<html>
	<head>
		<title> 2.5 </title>
	</head>
	<body>
		<?php
			function Russian($color) { print "<font color=$color>Здравствуйте!</font>"; }
			function English($color) { print "<font color=$color>Hello!</font>"; }
			function French($color)  { print "<font color=$color>Bonjour!</font>"; }
			function Deutsch($color) { print "<font color=$color>Guten Tag!</font>"; }

			$lang = $_GET["lang"];
			$color = $_GET["color"];
			
			if ($lang == "ru") {
				Russian($color);
			}
			elseif ($lang == "en") {
				English($color);
			}
			elseif ($lang == "fr") {
				French($color);
			}
			elseif ($lang == "de") {
				Deutsch($color);
			}
			else {
				print "Unknown Language";
			}
		?>
	</body>
</html>