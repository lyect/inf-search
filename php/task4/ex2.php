<html>
	<head>
		<title> 4.2.2 </title>
	</head>
	<body>
		<?php
			
			function getPOSTorEmpty($variable) {
				return isset($_POST[$variable]) ? $_POST[$variable] : '';
			}

			function initialHeader() {
				/* Nothing */
			}

			function noRequiredParametersHeader() {
				print "Должны быть указаны имя и почта!<br>";
			}

			function successfullyInsertedDataHeader() {
				$user = "lyect";
				$password = "12345678";

				$connection = mysqli_connect("localhost", $user, $password);

				if (!$connection) {
					print mysqli_connect_error() . "<br>";
				}

				$database = "InfSearchPHPDatabase";

				if (!mysqli_select_db($connection, $database)) {
					print "Невозможно открыть базу данных \"$database\": " . mysqli_error($connection) . "<br>";
				}

				$tableName = "notebook";

				$name = getPOSTorEmpty("name");
				$city = getPOSTorEmpty("city");
				$address = getPOSTorEmpty("address");
				$birthday = getPOSTorEmpty("birthday");
				$mail = getPOSTorEmpty("mail");

				$insertContentQuery = "";

				if ($birthday == "") {
					$insertContentQuery = "
						INSERT INTO $tableName
							(name, city, address, mail)
						VALUES
							('$name', '$city', '$address', '$mail');
					";
				}
				else {
					$insertContentQuery = "
						INSERT INTO $tableName
							(name, city, address, birthday, mail)
						VALUES
							('$name', '$city', '$address', STR_TO_DATE('$birthday', '%d-%m-%Y'), '$mail');
					";
				}

				$queryResult = mysqli_query($connection, $insertContentQuery);
				if (!$queryResult) {
					print "Невозможно вставить данные в таблицу \"$tableName\": " . mysqli_error($connection) . "<br>";
				}
				else {
					print "Запись успешно внесена!<br>";
				}
				
				mysqli_close($connection);
			}

			if ($_SERVER["REQUEST_METHOD"] == "POST") {
				if (getPOSTorEmpty("name") != "" && getPOSTorEmpty("mail") != "") {
					successfullyInsertedDataHeader();
				}
				else {
					noRequiredParametersHeader();
				}
			}
			else {
				initialHeader();
			}

			print "\t\t<form action='{$_SERVER['PHP_SELF']}' method='POST'>\n";
		?>
		
			<label for='name'>Имя[*]:</label>
			<input type='text' name='name' value="<?php echo getPOSTorEmpty('name'); ?>"/><br>

			<label for='city'>Город:</label>
			<input type='text' name='city' value="<?php echo getPOSTorEmpty('city'); ?>"/><br>

			<label for='address'>Адрес:</label>
			<input type='text' name='address' value="<?php echo getPOSTorEmpty('address'); ?>"/><br>

			<label for='birthday'>Дата рождения:</label>
			<input type='text' name='birthday' value="<?php echo getPOSTorEmpty('birthday'); ?>"/><br>

			<label for='mail'>Почта[*]:</label>
			<input type='text' name='mail' value="<?php echo getPOSTorEmpty('mail'); ?>"/><br>

			<input type='submit' value='Внести запись'/>
		</form>
		
		<a href='ex.php'>Меню</a>
	</body>
</html> 