<?php
			function type2str($typeNumber) {
				static $types;

				if (!isset($types)) {
					$types = array();
					$constants = get_defined_constants(true);
					foreach ($constants['mysqli'] as $constantName => $constantValue) {
						if (preg_match('/^MYSQLI_TYPE_(.*)/', $constantName, $match)) {
							$types[$constantValue] = $match[1];
						}
					}
				}

				return array_key_exists($typeNumber, $types) ? $types[$typeNumber] : "Unknown";
			}

			function flags2str($flagsAsNumber) {

				$flags = array();
				$constants = get_defined_constants(true);
				foreach ($constants['mysqli'] as $constantName => $constantValue) {
					if (preg_match('/MYSQLI_(.*)_FLAG$/', $constantName, $match)) {
						if (!array_key_exists($constantValue, $flags)) {
							$flags[$constantValue] = $match[1];
						}
					}
				}

				$result = array();
				foreach ($flags as $flagValue => $flagName) {
					if ($flagsAsNumber & $flagValue) {
						$result[] = $flagName;
					}
				}
				return implode(' ', $result);
			}

			function printStructure($requestedTableName, $connection) {
				$queryResult = mysqli_query($connection, "SELECT * FROM $requestedTableName");

				printf("\t\t<h4>Структура таблицы $requestedTableName</h4>");

				if (!$queryResult) {
					printf("\t\t<i>Невозможно получить доступ к структуре таблицы</i><br>");
					return;
				}

				printf("\t\t<dl>");
				$numFields = mysqli_num_fields($queryResult);
				for ($x=0; $x<$numFields; $x++) {
			    	
			        $properties = mysqli_fetch_field_direct($queryResult, $x);
			        
			        printf("\t\t\t<dd>\n");
					printf("\t\t\t\t<i>%s</i>\n", type2str($properties->type));
					printf("\t\t\t\t<i>%d</i>\n", $properties->length);
					printf("\t\t\t\t<i><b>%s</b></i>\n", $properties->name);
					printf("\t\t\t\t<i>%s</i>\n", flags2str($properties->flags));
					printf("\t\t\t</dd><br>\n");
			    }
			    printf("\t\t</dl>");
			}

			function printContent($requestedTableName, $connection) {
				$queryResult = mysqli_query($connection, "SELECT * FROM $requestedTableName");

				printf("\t\t<h4>Содержание таблицы $requestedTableName</h4>");

				if (!$queryResult) {
					printf("\t\t<i>Невозможно получить доступ к содержанию таблицы</i><br>");
					return;
				}

				$rusName = array(
					"snum"   => "Номер продавца",
					"sname"  => "Имя продавца",
					"city"   => "Город",
					"comm"   => "Комиссионные",
					"cnum"   => "Номер покупателя",
					"cname"  => "Имя покупателя",
					"rating" => "Рейтинг",
					"onum"   => "Номер заказа",
					"amt"    => "Цена",
					"odate"  => "Дата заказа"
				);

				$numFields = mysqli_num_fields($queryResult);

				printf("\t\t<table cellpadding=5 border=1>\n");

				printf("\t\t\t<tr>\n");
				for ($x = 0; $x < $numFields; $x++) {
					$name = mysqli_fetch_field_direct($queryResult, $x)->name;
					printf("\t\t\t\t<th>%s<br>%s</th>\n", $rusName[$name], $name);
				}
				printf("\t\t\t</tr>\n");

				while ($requestedTableRow = mysqli_fetch_row($queryResult)) {
					printf("\t\t\t<tr>\n");
					foreach ($requestedTableRow as $field) {
						printf("\t\t\t\t<td>%s</td>\n", $field);
					}
					printf("\t\t\t</tr>\n");
				}
				printf("\t\t</table><br>\n");
			}

			$sal_table = "sal";
			$cust_table = "cust";
			$ord_table = "ord";

			if (isset($_GET["sal_structure"])) {
				printStructure($sal_table, $connection);
			}

			if (isset($_GET["sal_content"])) {
				printContent($sal_table, $connection);
			}

			if (isset($_GET["cust_structure"])) {
				printStructure($cust_table, $connection);
			}

			if (isset($_GET["cust_content"])) {
				printContent($cust_table, $connection);
			}

			if (isset($_GET["ord_structure"])) {
				printStructure($ord_table, $connection);
			}

			if (isset($_GET["ord_content"])) {
				printContent($ord_table, $connection);
			}

			printf("\t\t<a href=z10-1.html>Вернуться к выбору таблиц</a>\n");
?>