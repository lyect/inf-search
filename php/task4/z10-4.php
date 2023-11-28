<?php
			$mysqlUser = "lyect";
			$mysqlPass = "12345678";
			$connection = mysqli_connect("localhost", $mysqlUser, $mysqlPass);

			if (!$connection) {
				die(mysqli_connect_error());
			}

			$database = "InfSearchPHPDatabas";

			if (!mysqli_select_db($connection, $database)) {
				die("Невозможно открыть базу данных \"$database\": ".mysqli_error($connection));
			}
?>