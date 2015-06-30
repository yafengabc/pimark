<head>
<title>The Pimark Result</title>
</head>
<body>
<p><h1>This is the All Result asc by C<h1></p>
<table border="1">
    <tr>
        <td>Top</td>
        <td>CPU Type</td>
        <td>HW Type</td>
        <td>Kernel Version</td>
        <td>GCC Version and ARCH</td>
        <td>C</td>
        <td>GMP</td>
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
