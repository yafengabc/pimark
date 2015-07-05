<!DOCTYPE html>
<html><head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <title>The Pimark Result </title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Bootstrap -->
    <link href="//cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap.min.css" rel="stylesheet">
  </head>
  <body>
    
<div class="navbar navbar-inverse" role="navigation">
    <div class="container">
        <div class="navbar-header">
            <a class="navbar-brand" href="pimark.htm">Order by C</a>
            <a class="navbar-brand" href="gmpimark.htm">Order by GMP</a>
            <a class="navbar-brand" href="mtgmpimark.htm">Order by MT-GMP</a>
        </div>   
    </div>
</div>

    
<div class="container">
    <div class="page-header">
        <p><h1>This is the all Result Order by {{pi}}</h1></p>
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
        
    </div>
</div>


    
<script src="//cdn.bootcss.com/jquery/1.11.3/jquery.min.js"></script>
<script src="//cdn.bootcss.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>

</body></html>
