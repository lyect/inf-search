<html>
	<head>
		<title> 3.3b </title>
	</head>
	<body>
		<?php
			$user = $_POST["user"];
			$results  = array(0, 0, 0, 0, 0, 0, 0, 0, 0);
			$results[0] = (int)($_POST["monument0city"] == "6");
			$results[1] = (int)($_POST["monument1city"] == "9");
			$results[2] = (int)($_POST["monument2city"] == "4");
			$results[3] = (int)($_POST["monument3city"] == "1");
			$results[4] = (int)($_POST["monument4city"] == "3");
			$results[5] = (int)($_POST["monument5city"] == "2");
			$results[6] = (int)($_POST["monument6city"] == "5");
			$results[7] = (int)($_POST["monument7city"] == "8");
			$results[8] = (int)($_POST["monument8city"] == "7");

			$result = array_sum($results);

			switch ($result) {
				case  9: $skillRatingText = "великолепно знаете географию"; break;
				case  8: $skillRatingText = "отлично знаете географию"; break;
				case  7: $skillRatingText = "очень хорошо знаете географию";  break;
				case  6: $skillRatingText = "хорошо знаете географию";  break;
				case  5: $skillRatingText = "удовлетворительно знаете географию"; break;
				case  4: $skillRatingText = "терпимо знаете географию"; break;
				case  3: $skillRatingText = "плохо знаете географию"; break;
				case  2: $skillRatingText = "очень плохо знаете географию"; break;
				default: $skillRatingText = "вообще не знаете географию"; break;
			}

			if ($user != "") {
				print "<p>$user, в";
			}
			else {
				print "<p>В";
			}
			print "ы $skillRatingText ($result/9)";
		?>
		<p style='text-align: center'><a href='z4-3a.php'>Назад</a>
	</body>
</html> 