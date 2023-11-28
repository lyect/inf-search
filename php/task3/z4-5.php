<?php
	if (isset($_POST["site"])) {
		$site = $_POST["site"];
		header("Location: $site");
		exit;
	}
?>
<html>
	<head>
		<title> 3.5 </title>
	</head>
	<body>
		<?php
			print "<form action='{$_SERVER['PHP_SELF']}' method='POST'>";
		?>
			<select name="site">
				<option value = "">Поисковые системы:
				<?php
					$list_sites = array(
						array("Google", "https://www.google.com/"),
						array("Yandex", "https://yandex.ru/"),
						array("Rambler", "https://www.rambler.ru/"),
						array("Mail.ru", "https://mail.ru/"),
						array("DuckDuckGo", "https://duckduckgo.com/")
					);

					$i = 0;
					while ($i < count($list_sites)) {
						$siteName = $list_sites[$i][0];
						$siteAddress = $list_sites[$i][1];
						print "<option value=$siteAddress>$siteName</option>";
						$i++;
					}
				?>
			</select>
			<input type="submit" value="Перейти">
		</form>
	</body>
</html>