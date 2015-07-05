<head>
<title>The Pimark Result</title>
</head>
<body>
<p><h1>This is the All Result Order by {{pi}}</h1></p>
<p><a href="pimark.htm">Order by C</a>
	&nbsp&nbsp&nbsp<a href="gmpimark.htm">Order by GMP</a>
	&nbsp&nbsp&nbsp<a href="mtgmpimark.htm">Order by MP GMP</a>
</p>
<table border="1">
    <tr>
        <td>Top</td>
        <td>CPU Type</td>
        <td>HW Type</td>
        <td>Kernel Version</td>
        <td>GCC Version and ARCH</td>
        <td>C</td>
        <td>GMP</td>
        <td>MtGMP</td>
        <td>USER</td>
    <tr>
%top=1
%for row in rows:
    <tr>
    <td>{{top}}</td>
    %for col in row:
        <td>{{col}}</td>
    %end
    </tr>
    %top+=1
%end
</table>
</body>
