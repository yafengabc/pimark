<head>
<title>the Pimark Result</title>
</head>
<body>
<p>All Result</p>
<table border="1">
    <tr>
        <td>CPU Type<td>
        <td>HW Type<td>
        <td>Kernel Version<td>
        <td>GCC Version and ARCH<td>
        <td>C<td>
        <td>GMP<td>
    <tr>
%for row in rows:
    <tr>
    %for col in row:
        <td>{{col}}</td>
    %end
    </tr>
%end
</table>
</body>
