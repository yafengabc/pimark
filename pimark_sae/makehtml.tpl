<!DOCTYPE html>
<html><head>
    <!--
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
    -->
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>The Pimark Result </title>
    <!-- Bootstrap -->
    <script src="//cdn.bootcss.com/jquery/1.11.3/jquery.min.js"></script>
    <script src="//cdn.bootcss.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="//cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap-theme.min.css">
    <link href="//cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap.min.css" rel="stylesheet">
    <link rel="shortcut icon" href="favicon.ico" >
    <link rel="icon" type="image/gif" href="favicon.gif" >
    <style>
        body{
            padding:0px;
            margin:0px;
            border:1px solid black;
            }
        div{
            margin:0px;
            }
        #footer{
            text-align:center
        }
        
    </style>
  </head>
  <body>
    <nav class="navbar navbar-inverse navbar-fixed-top">
        <div class="container">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="index.htm">PiMark Home</a>
            </div>
            <div id="navbar" class="navbar-collapse collapse">
                <ul class="nav navbar-nav">
                    <!-- <li><a href="#">Home</a></li> -->
                    <li><a href="pimark.htm">Order By C</a></li>
                    <li><a href="gmpimark.htm">Order By GMP</a></li>
                    <li><a href="mtgmpimark.htm">Order By MtGMP</a></li>
                </ul>
            </div><!--/.nav-collapse -->
        </div>
    </nav>
    
    <div class="jumbotron">
        <div class="container">
            <div class="page-header">
                <p><h3>Result Order by {{pi}}</h3></p>
                <table class="table table-bordered">
                    <tr class="danger">
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
        	        %li="success"
                    %for row in rows:
        	        %if li=="success":
        	    	%li="warning"
        	        %else:
        	    	%li="success"
        	        %end
                    <tr class="{{li}}">
                        <td>{{top}}</td>
                        %for col in row:
                            <td>{{col}}</td>
                        %end
                    </tr>
                    %top+=1
                    %end
                </table>
            </div>
     <div id="footer">
        <script async src="//dn-lbstatics.qbox.me/busuanzi/2.3/busuanzi.pure.mini.js"></script>
        <span>Powered by Yafeng,2015-2016</span>
        <span id="busuanzi_container_site_pv">本站总访问IP:<span id="busuanzi_value_site_uv"></span>次</span>
        <span id="busuanzi_container_site_pv">本站总点击:<span id="busuanzi_value_site_pv"></span>次</span>
        <span id="busuanzi_container_page_pv">本文阅读量:<span id="busuanzi_value_page_pv"></span>次</span>
    </div>


        </div>
    </div>
    
</body></html>
