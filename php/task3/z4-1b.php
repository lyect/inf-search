<html>
    <head>
        <title> 3.1b </title>
    </head>
    <body>
    <?php
        $ha = $_GET["ha"];
        $va = $_GET["va"];
        print "<table cellpadding=5 border=1 width=300 height=300>\n";
        print "\t<tr>\n";
        print "\t\t<td style='text-align: $ha; vertical-align: $va'>Aligned Text</td>\n";
        print "\t</tr>\n";
        print "</table>\n";
    ?>
    <p style='text-align: center'><a href='z4-1a.html'>Back</a>
    </body>
</html>