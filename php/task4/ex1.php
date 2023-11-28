<html>
	<head>
		<title> 4.2.1 </title>
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
			$dropTableQuery = "
				DROP TABLE IF EXISTS $tableName;
			";

			$queryResult = mysqli_query($connection, $dropTableQuery);
			if (!$queryResult) {
				die("Невозможно удалить таблицу \"$tableName\": ".mysqli_error($connection));
			}

			$createTableQuery = "
				CREATE TABLE $tableName (
					id       int         NOT NULL AUTO_INCREMENT PRIMARY KEY,
					name     varchar(50),
					city     varchar(50),
					address  varchar(50),
					birthday date,
					mail     varchar(20));
			";

			$queryResult = mysqli_query($connection, $createTableQuery);
			if (!$queryResult) {
				die("Невозможно создать таблицу \"$tableName\": ".mysqli_error($connection));
			}

			printf("Таблица \"%s\" успешно создана!<br>\n", $tableName);

			mysqli_close($connection);

			print "<a href=ex.php>Меню</a>\n";
		?>
	</body>
</html> 