<html>
	<head>
		<title> 2.6 </title>
	</head>
	<body>
		<?php

			print "<p>Массив treug<p>";
			$treug = array();
			for ($n = 1; $n <= 10; $n++) {
				$treug[$n] = $n * ($n + 1) / 2;
			}

			foreach ($treug as $number) {
				print "$number  ";
			}

			print "<p>Массив kvd<p>";
			$kvd = array();
			for ($n = 1; $n <= 10; $n++) {
				$kvd[$n] = $n * $n;
			}
			
			foreach ($kvd as $number) {
				print "$number  ";
			}

			print "<p>Объединённый массив<p>";
			$rez = array_merge($treug, $kvd);
			
			foreach ($rez as $number) {
				print "$number  ";
			}

			print "<p>Отсортированный объединённый массив<p>";
			sort($rez);

			foreach ($rez as $number) {
				print "$number  ";
			}

			print "<p>Удалили первый элемент<p>";
			array_shift($rez);

			foreach ($rez as $number) {
				print "$number  ";
			}

			print "<p>Применили array_unique()<p>";
			$rez1 = array_unique($rez);

			foreach ($rez1 as $number) {
				print "$number  ";
			}
		?>
	</body>
</html>