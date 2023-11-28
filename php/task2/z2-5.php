<html>
	<head>
		<title> 2.2 </title>
	</head>
	<body> 
		<?php 
			$lang = $_GET["lang"];

			if ($lang == "ru") {
				print "Russian";
			}
			elseif ($lang == "en") {
				print "English";
			}
			elseif ($lang == "fr") {
				print "French";
			}
			elseif ($lang == "de") {
				print "Deutsch";
			}
			else {
				print "Unknown Language";
			}
		?>
	</body>
</html>