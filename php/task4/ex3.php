<html>
	<head>
		<title> 4.2.3 </title>
	</head>
	<body>
		<?php

			$user = "lyect";
			$password = "12345678";

			$connection = mysqli_connect("localhost", $user, $password);

			if (!$connection) {
				die(mysqli_connect_error());
			}

			$database = "InfSearchPHPDatabase";

			if (!mysqli_select_db($connection, $database)) {
				die("Невозможно открыть базу данных \"$database\": ".mysqli_error($connection));
			}

			$tableName = "notebook";

			$getContentQuery = "
				SELECT *
				FROM notebook;
			";

			$queryResult = mysqli_query($connection, $getContentQuery);
			if (!$queryResult) {
				die("Невозможно получить данные с таблицы \"$tableName\": ".mysqli_error($connection));
			}

			if (mysqli_num_rows($queryResult) == 0) {
				print "Таблица пустая!<br>\n";
				print "<a href=ex.php>Меню</a>\n";
				mysqli_close($connection);
				return;
			}

			print "\t\t<table border=1 cellpadding=5>\n";
			print "\t\t\t<tr>\n";
			print "\t\t\t\t<td style='text-align: center;'><b>Уникальный номер</b><br>id</td>\n";
			print "\t\t\t\t<td style='text-align: center;'><b>Имя</b><br>name</td>\n";
			print "\t\t\t\t<td style='text-align: center;'><b>Город</b><br>city</td>\n";
			print "\t\t\t\t<td style='text-align: center;'><b>Адрес</b><br>address</td>\n";
			print "\t\t\t\t<td style='text-align: center;'><b>Дата рождения</b><br>birthday</td>\n";
			print "\t\t\t\t<td style='text-align: center;'><b>Почта</b><br>mail</td>\n";
			print "\t\t\t</tr>\n";

			while ($tableRow = mysqli_fetch_array($queryResult)) {
				print "\t\t\t<tr>\n";
				print "\t\t\t\t<td>".$tableRow["id"]."</td>\n";
				print "\t\t\t\t<td>".$tableRow["name"]."</td>\n";
				print "\t\t\t\t<td>".$tableRow["city"]."</td>\n";
				print "\t\t\t\t<td>".$tableRow["address"]."</td>\n";
				print "\t\t\t\t<td>".$tableRow["birthday"]."</td>\n";
				print "\t\t\t\t<td>".$tableRow["mail"]."</td>\n";
				print "\t\t\t</tr>\n";
			}

			print "\t\t</table><br>\n";
			print "<a href=ex.php>Меню</a>\n";

			mysqli_close($connection);
		?>
	</body>
</html> 