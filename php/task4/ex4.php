<html>
	<head>
		<title> 4.2.4 </title>
	</head>
	<body>
		<?php
			function getGETorEmpty($variable) {
				return isset($_GET[$variable]) ? $_GET[$variable] : '';
			}

			function getPOSTorEmpty($variable) {
				return isset($_POST[$variable]) ? $_POST[$variable] : '';
			}

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

			$id = getGETorEmpty("id_to_update");
			if ($_SERVER["REQUEST_METHOD"] == "GET") {
				if ($id != "") {
					$correspondingRowQuery = "
						SELECT *
						FROM $tableName
						WHERE id = '$id';
					";

					$queryResult = mysqli_query($connection, $correspondingRowQuery);
					if (!$queryResult) {
						die("Невозможно получить данные с таблицы \"$tableName\": ".mysqli_error($connection));
					}

					$row = mysqli_fetch_assoc($queryResult);

					print "\t\t<form action='{$_SERVER['PHP_SELF']}' method='POST'>\n";
					print "\t\t\t<select name='field_name'>\n";
					print "\t\t\t\t<option value='name'>{$row['name']}</option>\n";
					print "\t\t\t\t<option value='city'>{$row['city']}</option>\n";
					print "\t\t\t\t<option value='address'>{$row['address']}</option>\n";
					print "\t\t\t\t<option value='birthday'>{$row['birthday']}</option>\n";
					print "\t\t\t\t<option value='mail'>{$row['mail']}</option>\n";
					print "\t\t\t</select>\n";
					print "\t\t\t<input type='text' name='field_value'/>\n";
					print "\t\t\t<input type='hidden' name='id' value=$id>\n";
					print "\t\t\t<input type='submit' value='Изменить'/>\n";
					print "\t\t<form>\n";

					mysqli_close($connection);

					return;
				}
				else {
					if (isset($_GET["attempted"])) {
						print "Выберите строку, которую хотите изменить!<br>";
					}
				}
			}
			elseif ($_SERVER["REQUEST_METHOD"] == "POST") {
				$updateContentQuery = "
					UPDATE $tableName
					SET {$_POST['field_name']} = '{$_POST['field_value']}'
					WHERE id = {$_POST['id']};
				";

				$queryResult = mysqli_query($connection, $updateContentQuery);
				if (!$queryResult) {
					die("Не удалось обновить данные в таблице \"$tableName\": ".mysqli_error($connection));
				}

				print "Данные успешно обновлены!<br>";
			}

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

			print "\t\t<form action='{$_SERVER['PHP_SELF']}' method='GET'>\n";
			print "\t\t\t<table border=1 cellpadding=5>\n";
			print "\t\t\t\t<tr>\n";
			print "\t\t\t\t\t<td style='text-align: center;'><b>Уникальный номер</b><br>id</td>\n";
			print "\t\t\t\t\t<td style='text-align: center;'><b>Имя</b><br>name</td>\n";
			print "\t\t\t\t\t<td style='text-align: center;'><b>Город</b><br>city</td>\n";
			print "\t\t\t\t\t<td style='text-align: center;'><b>Адрес</b><br>address</td>\n";
			print "\t\t\t\t\t<td style='text-align: center;'><b>Дата рождения</b><br>birthday</td>\n";
			print "\t\t\t\t\t<td style='text-align: center;'><b>Почта</b><br>mail</td>\n";
			print "\t\t\t\t\t<td style='text-align: center;'><b>Изменить</b></td>\n";
			print "\t\t\t</tr>\n";

			while ($tableRow = mysqli_fetch_array($queryResult)) {
				print "\t\t\t<tr>\n";
				print "\t\t\t\t<td>".$tableRow["id"]."</td>\n";
				print "\t\t\t\t<td>".$tableRow["name"]."</td>\n";
				print "\t\t\t\t<td>".$tableRow["city"]."</td>\n";
				print "\t\t\t\t<td>".$tableRow["address"]."</td>\n";
				print "\t\t\t\t<td>".$tableRow["birthday"]."</td>\n";
				print "\t\t\t\t<td>".$tableRow["mail"]."</td>\n";
				print "\t\t\t\t<td><input type='radio' name='id_to_update' value='" . $tableRow["id"] . "'></td>\n";
				print "\t\t\t</tr>\n";
			}

			print "\t\t\t</table>\n";
			print "\t\t\t<input type='hidden' name='attempted' value=1>\n";
			print "\t\t\t<input type='submit' value='Изменить'/>\n";
			print "\t\t</form><br>\n";
			print "<a href=ex.php>Меню</a>\n";

			mysqli_close($connection);
		?>
	</body>
</html> 