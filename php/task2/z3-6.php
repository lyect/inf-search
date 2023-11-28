<html>
	<head>
		<title> 2.6 </title>
	</head>
	<body>
		<?php
			print "<p>Ассоциативный массив<p>";
			$cust = array(
				"cnum"   => 2001,
				"cname"  => "Hoffman",
				"city"   => "London",
				"snum"   => 1001,
				"rating" => 100
			);

			foreach ($cust as $key => $value) {
				print "$key = $value<br>";
			}

			print "<p>Сортировка по значениям<p>";
			asort($cust);

			foreach ($cust as $key => $value) {
				print "$key = $value<br>";
			}

			print "<p>Сортировка по ключу<p>";
			ksort($cust);
			
			foreach ($cust as $key => $value) {
				print "$key = $value<br>";
			}

			print "<p>Сортировка с помощью sort()<p>";
			sort($cust);
			
			foreach ($cust as $key => $value) {
				print "$key = $value<br>";
			}
		?>
	</body>
</html>