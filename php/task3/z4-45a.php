<html>
    <head>
        <title> 3.4.1a </title>
    </head>
    <body>
        <form action="z4-45b.php" method="POST">
            <p>Введите ваше имя
            <p><input type="text" name="user">
            <p>Что вы любите делать в свободное время <br>
               (можно выбрать несколько вариантов)
            <p><input type="checkbox" name="hobby[]"
                value="слушать музыку">слушать музыку
            <p><input type="checkbox" name="hobby[]"
                value="читать книгу">читать книгу
            <p><input type="checkbox" name="hobby[]"
                value="смотреть телевизор">смотреть телевизор
            <p><input type="checkbox" name="hobby[]"
                value="гулять на улице">гулять на улице
            <p><input type="submit" value="Выбор сделан">
        </form>
    </body>
</html>