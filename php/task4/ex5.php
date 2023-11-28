<html>
	<head>
		<title> 4.2.5 </title>
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

			$insertContentQuery = "
				INSERT INTO $tableName
					(name, city, address, birthday, mail)
				VALUES
					('Вася Пупкин', 'Москва', 'Улица Пушкина, дом Колотушкина', STR_TO_DATE('01-11-98', '%d-%m-%Y'), 'v.pupkin@email.ru'),
					('Joe Average', 'Edinburgh', '19 W Register St', STR_TO_DATE('19-03-2002', '%d-%m-%Y'), 'j.average@email.uk'),
					('Otto Normal', 'Berlin', 'Platz der Republik 1', STR_TO_DATE('31-08-95', '%d-%m-%Y'), 'o.normal@email.de');
			";

			$queryResult = mysqli_query($connection, $insertContentQuery);
			if (!$queryResult) {
				die("Невозможно вставить данные в таблицу \"$tableName\": ".mysqli_error($connection));
			}

			print "Данные успешно вставлены!<br>";
			print "<a href=ex.php>Меню</a>";

			mysqli_close($connection);
		?>
	</body>
</html> 