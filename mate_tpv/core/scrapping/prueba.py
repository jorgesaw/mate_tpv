#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 10/02/2015

@author: jorgesaw
'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 25/01/2015

@author: jorgesaw
'''
from bs4 import BeautifulSoup
from core.scrapping.ScrapBase import ScrapBase
from core.scrapping.ScrapLotNacional import ScrapLotNacional
from core.util.ManejaFechas import ManejaFechas
import urllib2

html = """
 
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "https://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml"><head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<META content="Portal de Resultados de los Juegos Oficiales de Loteria. Quini 6, Quiniela, Loto, Loto 5, Lotería y Brinco" name=Abstract>
<META  name=description CONTENT="Portal de Resultados de los Juegos Oficiales de Loteria. Quini 6, Quiniela, Loto, Loto 5, Brinco y Lotería Resultados de sorteos anteriores. Loteria Nacional, Provincia Buenos Aires, Santa Fe, Cordoba, Santiago">
<link type="image/x-icon" href="imagenes/design/logos/logo-ico.ico" rel="icon" />
<link type="image/x-icon" href="imagenes/design/logos/logo-ico.ico" rel="shortcut icon" />
<META content=FOLLOW,INDEX name=robots>
<META content="Jugar, Quiniela, Online, On-line, On-line, Quini 6, Loto, Loto 5, Apuestas Argentina, Juegos Oficiales, Apuestas Santa Fe, Apuestas, Quinielas Argentinas, Qunielas Argentinas" name=keywords>
<META content=web name=subject>
<META content=General name=rating>
<META content=entertainment name=category>
<META content="10 days" name=revisit-after>
<meta name="google-site-verification" content="EPUeBaTaj2WKlzyTde9hct0Gmy0V51YYWtNoKa9Szxw" />
<meta name="Revisit" content="10 days" />
<META content=public name=security>
<META content=ES name=language>
<META content=all name=audience>
<META content="AIB" name=copyright>
<META content=document name=resource-type>
<META content="AIB" name=author>
<META content=Document name=VW96.objecttype>
<META content="AIB" name=DC.Title>
<META content="" name=DC.Creator>
<META content=Spanish name=DC.Language>
<META http-equiv=Content-language content=es>
<META http-equiv=Content-Type content="text/html; charset=utf8">
<META http-equiv=pragma content=no-cache>
<title>Quinielas Argentinas :: Quiniela OnLine :: Apostar Quiniela Argentina :: Quiniela Santa Fe :: Resultados</title>
<script type="text/javascript">/* refrescar pagina cada 5 minutos*/ /*Begin*/

function reFresh() {  location.reload(true)}

/* Set the number below to the amount of delay, in milliseconds,you want between page reloads: 1 minute = 60000 milliseconds. */

window.setInterval("reFresh()",300000); 

// End --></script>


<SCRIPT LANGUAGE="JavaScript">
  var timerID = null
  var timerRunning = false

  var anio = 2015; 
  var mes = 01; 
  var dia = 19;
  var h = 18; 
  var m = 16;
  var s=27;//<php echo date("s"); ?>;
  var day = 1;

 

  function MakeArray(size) 
  {
  this.length = size;
  for(var i = 1; i <= size; i++)
  {
  this[i] = "";
  }
  return this;
  }
  
  function stopclock ()
  {
  if(timerRunning)
  clearTimeout(timerID);
  timerRunning = false;
  }
  
  function showtime () 
  {
 
      var now = new Date(anio, mes, dia, h, m, s);
      var year = now.getYear();
      var month = now.getMonth() ;
      var date = now.getDate();
      var hours = now.getHours();
      var minutes = now.getMinutes();
      var seconds = now.getSeconds();
//      var day = now.getDay();

  Day = new MakeArray(7);
  Day[0]="Domingo";
  Day[1]="Lunes";
  Day[2]="Martes";
  Day[3]="Miercoles";
  Day[4]="Jueves";
  Day[5]="Viernes";
  Day[6]="Sabado";
  var timeValue = "";

  timeValue += ((hours <= 12) ? hours : hours - 12);
  timeValue += ((minutes < 10) ? ":0" : ":") + minutes;
  timeValue += ((seconds < 10) ? ":0" : ":") + seconds;
  timeValue += (hours < 12) ? " AM" : " PM";

  document.getElementById("hora").innerHTML = timeValue;
  /*document.getElementsByTagName("hora").innerHTML = timeValue;*/
  timerID = setTimeout("showtime()",1000);
  timerRunning = true;
  s=s+1;
  }
  
  function startclock () 
  {
  stopclock();
  showtime()
  }
  // End Hiding -->
function init() {


startclock();
}
window.onload=init;

</SCRIPT>
<script language="JavaScript"> 
function maxLength(e,obj,num) {
    k = (document.all) ? e.keyCode : e.which;
    if (k==8 || k==0){ return true; }
    else{ return obj.value.length<num; }
}
</script> 

<script src="jscripts/AC_RunActiveContent.js" type="text/javascript"></script><style type="text/css">



















/* ***************************************************        Estilos generales de la pagina y 



layout****************************************************** */a img { border: none; }#contenedorContenido {    padding-left: 0px;   /* LC width */    padding-right: 0px;  /* RC width */    overflow: hidden; border:groove; border-color:grey;border-width:thin; border-bottom:none;}#contenedorContenido .column {    position:relative;float:right; width:150px;}#columnaCentral {  width:500px;  background-color:#FFFFFF; padding:0px 0px 0px 0px; margin-left:0px;/*text-align:left;*/}#columnaIzquierda {  width: 200px;          /* LC width */ /*float:right  /*margin-left:300px;   /* LC width */  background-color:#ffffff;}#columnaDerecha { width: 194px; float:left; /*250*/       /* RC width */  /*margin-right: -150px;*/  /* RC width */ }* html body {     overflow: hidden; }* html #footer-wrapper {  float: left;  position: relative;    width:970px;  padding-bottom: 10010px;  margin-bottom: -10000px;    background: #fffFFF;     border-bottom-style:groove; border-left-style:groove; border-right-style:groove; border-width:thin  ;border-color:grey;     /* Same as body background */}.piePagina { padding-top: 5px; width:980px; background-color:#FFFFFF ;color:#000000; border-bottom-style:groove; border-left-style:groove; border-right-style:groove; border-width:thin  ;border-color:grey;}body {    font-family: Verdana, Arial, Helvetica, sans-serif;    font-size: 12px;    color:#333333;    min-width: 650px;      /* 2x LC width + RC width */    margin: 0 5px 0 5px; }input { /*width of text boxes. IE6 does not understand this attribute*/width: 180px;border: 1px solid #999999;font-family:Verdana, Arial, Helvetica, sans-serif;font-size:11px;background-image:url(imagenes/design/frm_bg_input.gif);padding: 0 2px 0 2px;}/* ******************************************************************************                                Estilos de la Columna







 Izquierda********************************************************************************* */ /* |||||||||||||||||||||||||||||||||||||||||||||    Estilos del cuadro de























 



 login|||||||||||||||||||||||||||||||||||||||||||||||| */.cuadroLogin {background-color:#FFFFFF; background-image:url(imagenes//design/fondo_login.gif); color:#FFFFFF; width: 168px;}.loginBoton {background-color:#FFFFFF; color:#000000;background-image:none;border-top: 2px solid #FFFFFF;border-left: 2px solid #FFFFFF;;width:auto}.input{ font:Arial, Helvetica, sans-serif; color:#666666}/* |||||||||||||||||||||||||||||||||||||||||||||    Estilos del Menu Izquierdo|||||||||||||||||||||||||||||||||||||||||||||||| */



 body {background: #FFFFFF;}



 



#menu14 {



        font-family: Verdana, Arial, Helvetica, sans-serif;



        margin: 0;



        font-size: 80%;



        font-weight: bold;



        background: #FFFFFF;



        text-align:left;



        width: 180px;  



        margin: 0px;



        }







#menu14 li a {



        height: 32px;



          voice-family: "\"}\"";



          voice-family: inherit;



          height: 24px;



        text-decoration: none;



        }







#menu14 li a:link, #menu14 li a:visited {



        color: #FFFFFF;



        display: block;



        background:  url(imagenes//menu14.gif) no-repeat;



        padding: 8px 0 0 10px;



        }



#menu14 .subMenu{



margin-left: 13px;



}



#menu14 li a:hover, #menu14 li #current {



        color: #FFF;



        background:  url(imagenes//menu14.gif) 0 -32px no-repeat;



        padding: 8px 0 0 10px;



        }







#menu14 ul {



        list-style: none;  



        margin: 0;



        padding: 0;



        text-align:left;



        }


.Estilo7, .Estilo4
{
color:black;
}

 



 .boxMenuIzq1, .boxMenuIzq3, .boxMenuIzq4 {padding: 2px 0px 2px 10px;border-top:2px solid #FFFFFF;cursor:pointer;background-color:#FFFFFF;background-image:url(imagenes//design/fondo_login.gif);}.boxMenuIzq2, .boxMenuIzq5 {padding: 2px 0px 2px 10px;border-top:2px solid #999999;cursor:pointer;background-color:#2d922c;}.boxMenuIzq3 {background-color:#FFFFFF;}.boxMenuIzq4, .boxMenuIzq5 {padding: 2px 0px 2px 20px;} .txtMenuIzq {color:#FFFFFF;font-size:10px;margin-left: 7px;font-weight:bold;}#menuIzquierdo a:link, #menuIzquierdo a:visited, #menuIzquierdo a:active, #menuIzquierdo a:hover {text-decoration:none;/* color: #333333; */color:#000000;font-size:10px;margin-left: 7px;font-weight:bold;}#menuIzquierdo a:hover {text-decoration:underline;/* color: #333399; */}</style><script>function ocultarMostrar (x) {cacheobj = document.getElementById(x); if (cacheobj.style.display == "none") { cacheobj.style.display = "block"; } else { cacheobj.style.display = "none"; }}</script></head>
<body style="background-color:#FFFFFF; color:#000000" >







<div align="center" >

<style>.top{}.top_fecha {font-size: 9px;font-weight:bold;color:#000000;margin-left:300px;}body {    background-color: #ffffff;    margin-left: 0px;    margin-top: 0px;    margin-right: 0px;    margin-bottom: 0px;}.Estilo1 {font-size: 11px}</style>

<form action="checkLogin.php" method="post" enctype="multipart/form-data">

<table width="981" border="0" cellpadding="0" cellspacing="0">  <tr>    

    <td width="1" height="100" rowspan="2" valign="top"><a href="index.php"></a></td>    <td  height="50" colspan="2" align="left" valign="top" bgcolor="#FFFFFF"> <div onclick="location.href='http://quinielasargentinas.com';" style="cursor:pointer;">      <object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=7,0,19,0" width="980" height="200">        
      <param name="movie" value="../imagenes/design/top.swf" />        <param name="quality" value="high" />        <param name="wmode" value="transparent" />        <embed src="../imagenes/design/top.swf" width="980" height="200" quality="high" pluginspage="http://www.macromedia.com/go/getflashplayer" type="application/x-shockwave-flash" wmode="transparent"></embed>      </object>     </div>       

    </td>

</tr> 

<tr>

    <td width="1010">

    
    <div style="display:block; font-size:11px;vertical-align:bottom;">

    <div style="color:#000000;margin:0;" > Usuario          <input type="text" class="input"name="wLoginUser"  onchange="return validar(event)"  maxlength="12"  style="width:90px;"/>          Clave          <input class="input" type="password" name="wLoginPass" maxlength="12" style="width:90px;"/>          <label>          <input name="submit" type="submit" class="loginBoton" value="Acceder&gt;" />          </label>          <a href="recuperaDatos.php">Olvido su contrase&ntilde;a</a>

                 </div>

              </div>                  

    </td>

   <td ><iframe frameborder="0" src="clima.php" width="480" height="34" scrolling="no"></iframe></td>

    </tr> 

</table> 

</form>









<div id="fechahora" style="overflow:hidden; width=100px">
<B>Lunes,</B> 19 de Enero de 2015 <b> Hora del servidor:  <span id="hora" name="hora"></span> </b>
 
</div>

<table width="980" style="border-bottom-style:none; border-left-style:solid; border-right-style:solid; border-top-style:solid; border-width:thin;border-color:grey;padding:0px;">
<tr>
<td>
<div id="TICKER" STYLE="overflow:hidden; width:990px; background-color:#00AA00;color:#FFFFFF; height:16px;"  onmouseover="TICKER_PAUSED=true" onMouseOut="TICKER_PAUSED=false">
<a style="text-decoration: none; color: #FFFFFF; font-weight:bold;" href="http://www.infobae.com/2015/01/19/1621831-la-asociacion-magistrados-critico-la-extrema-tension-y-hostilidad-del-ejecutivo-nisman" target="_blank">
La Asociación de Magistrados criticó la "extrema tensión y hostilidad" del Ejecutivo hacia Nisman
</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a style="text-decoration: none; color: #FFFFFF; font-weight:bold;" href="http://www.infobae.com/2015/01/19/1621828-por-su-gravedad-la-muerte-del-fiscal-nisman-debe-investigarse-como-lo-fue-el-atentado" target="_blank">
"Por su gravedad, la muerte del fiscal Nisman debe investigarse como lo fue el atentado"
</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a style="text-decoration: none; color: #FFFFFF; font-weight:bold;" href="http://www.infobae.com/2015/01/19/1621821-murio-helenita-la-beba-que-recibio-dos-trasplantes-medula" target="_blank">
Murió Helenita, la beba que recibió dos trasplantes de médula
</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a style="text-decoration: none; color: #FFFFFF; font-weight:bold;" href="http://www.infobae.com/2015/01/19/1621795-encontraron-muerto-alberto-nisman" target="_blank">
Encontraron muerto a Alberto Nisman
</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a style="text-decoration: none; color: #FFFFFF; font-weight:bold;" href="http://www.infobae.com/2015/01/19/1621788-amia-y-daia-aseguraron-que-redoblaran-su-reclamo" target="_blank">
AMIA y DAIA aseguraron que "redoblarán su reclamo"
</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a style="text-decoration: none; color: #FFFFFF; font-weight:bold;" href="http://www.infobae.com/2015/01/19/1621776-sergio-hernandez-vuelve-ser-el-dt-la-seleccion-basquet" target="_blank">
Sergio Hernández vuelve a ser el DT de la selección de básquet
</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a style="text-decoration: none; color: #FFFFFF; font-weight:bold;" href="http://www.infobae.com/2015/01/19/1621775-el-video-que-acredita-el-pacto-di-zeo-y-martin-cada-vez-mas-cerca-recuperar-la-doce" target="_blank">
El video que acredita el pacto entre Di Zeo y Martín, cada vez más cerca de recuperar "La Doce"
</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a style="text-decoration: none; color: #FFFFFF; font-weight:bold;" href="http://www.infobae.com/2015/01/19/1621772-el-dolar-libre-subio-11-centavos-y-se-vendio-1370-la-city" target="_blank">
El dólar libre subió 11 centavos y se vendió a $13,70 en la City
</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a style="text-decoration: none; color: #FFFFFF; font-weight:bold;" href="http://www.infobae.com/2015/01/19/1621773-tinelli-es-un-dia-luto-hay-sensacion-impunidad-y-codigos-mafiosos" target="_blank">
Tinelli: "Es un día de luto, hay sensación de impunidad y de códigos mafiosos"
</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a style="text-decoration: none; color: #FFFFFF; font-weight:bold;" href="http://www.infobae.com/2015/01/19/1621763-macri-si-esta-muerte-termina-mas-impunidad-es-un-desastre-el-futuro-institucional-del-pais" target="_blank">
Macri: "Si esta muerte termina en más impunidad, es un desastre para el futuro institucional del país"
</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a style="text-decoration: none; color: #FFFFFF; font-weight:bold;" href="http://www.infobae.com/2015/01/19/1621750-centurion-la-patada-por-suerte-no-fue-grave-marin-es-un-chico-como-yo-y-puede-pasar" target="_blank">
Centurión, tras la patada: "Por suerte no fue grave, Marín es un chico como yo y puede pasar"
</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a style="text-decoration: none; color: #FFFFFF; font-weight:bold;" href="http://www.infobae.com/2015/01/19/1621741-israel-lamento-la-muerte-del-fiscal-nisman-y-exige-justicia-el-atentado-la-amia" target="_blank">
Israel lamentó la muerte del fiscal Nisman y exige justicia por el atentado a la AMIA
</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a style="text-decoration: none; color: #FFFFFF; font-weight:bold;" href="http://www.infobae.com/2015/01/19/1621737-repercusiones-que-dijeron-los-precandidatos-presidente" target="_blank">
Repercusiones: qué dijeron los precandidatos a presidente
</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a style="text-decoration: none; color: #FFFFFF; font-weight:bold;" href="http://www.infobae.com/2015/01/19/1621732-carrio-esto-era-previsible-no-creo-el-suicidio" target="_blank">
Carrió: "Esto era previsible; no creo en el suicidio"
</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a style="text-decoration: none; color: #FFFFFF; font-weight:bold;" href="http://www.infobae.com/2015/01/19/1621730-muertedenisman-es-tendencia-twitter-nivel-mundial" target="_blank">
#MuerteDeNisman es tendencia en Twitter a nivel mundial
</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a style="text-decoration: none; color: #FFFFFF; font-weight:bold;" href="http://www.infobae.com/2015/01/19/1621725-asi-se-entero-timerman-uno-los-acusados-el-fiscal-nisman" target="_blank">
Así se enteró Timerman, uno de los acusados por el fiscal Nisman
</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a style="text-decoration: none; color: #FFFFFF; font-weight:bold;" href="http://www.infobae.com/2015/01/19/1621702-con-dos-goles-ronaldo-real-madrid-gano-y-se-corono-campeon-invierno" target="_blank">
Con dos goles de Ronaldo, Real Madrid ganó y se coronó campeón de invierno
</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a style="text-decoration: none; color: #FFFFFF; font-weight:bold;" href="http://www.infobae.com/2015/01/19/1621701-tevez-aviso-que-no-renovara-su-contrato-la-juventus" target="_blank">
Tevez avisó que no renovará su contrato con la Juventus
</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a style="text-decoration: none; color: #FFFFFF; font-weight:bold;" href="http://www.infobae.com/2015/01/19/1621697-el-comunicado-del-ministerio-seguridad-hubo-preservacion-la-escena-del-crimen" target="_blank">
El comunicado del Ministerio de Seguridad: "Hubo preservación de la escena del crimen"
</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a style="text-decoration: none; color: #FFFFFF; font-weight:bold;" href="http://www.infobae.com/2015/01/19/1621695-perfil-un-fiscal-carrera-que-habia-sido-elegido-nestor-kirchner-investigar-el-atentado" target="_blank">
Perfil: un fiscal de carrera que había sido elegido por Nestor Kirchner para investigar el atentado
</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a style="text-decoration: none; color: #FFFFFF; font-weight:bold;" href="http://www.infobae.com/2015/01/19/1621693-la-muerte-del-fiscal-alberto-nisman-los-diarios-todo-el-mundo" target="_blank">
La muerte del fiscal Alberto Nisman en los diarios de todo el mundo
</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a style="text-decoration: none; color: #FFFFFF; font-weight:bold;" href="http://www.infobae.com/2015/01/19/1621689-que-habia-dicho-nisman-su-denuncia" target="_blank">
Qué había dicho Nisman tras su denuncia
</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a style="text-decoration: none; color: #FFFFFF; font-weight:bold;" href="http://www.infobae.com/2015/01/19/1621688-el-contenido-las-escuchas-que-complican-al-gobierno" target="_blank">
El contenido de las escuchas que complican al Gobierno
</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a style="text-decoration: none; color: #FFFFFF; font-weight:bold;" href="http://www.infobae.com/2015/01/19/1621241-la-misa-mas-grande-del-mundo" target="_blank">
La misa más grande del mundo
</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a style="text-decoration: none; color: #FFFFFF; font-weight:bold;" href="http://www.infobae.com/2015/01/18/1621676-para-randazzo-las-elecciones-se-juega-el-futuro-la-argentina-el-gran-esfuerzo-que-se-hizo-los-ultimos-anos" target="_blank">
Para Randazzo en las elecciones "se juega el futuro de la Argentina, el gran esfuerzo que se hizo en los últimos años"
</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a style="text-decoration: none; color: #FFFFFF; font-weight:bold;" href="http://www.infobae.com/2015/01/18/1621668-una-pequena-pastilla-se-llevo-mi-hijo-dijo-el-padre-del-joven-que-murio-tomar-extasis" target="_blank">
"Una pequeña pastilla se llevó a mi hijo", dijo el padre del joven que murió tras tomar éxtasis
</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a style="text-decoration: none; color: #FFFFFF; font-weight:bold;" href="http://www.infobae.com/2015/01/18/1621661-la-daia-preocupada-la-desaparicion-del-misil-del-ejercito" target="_blank">
La DAIA, preocupada por la desaparición del misil del Ejército
</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a style="text-decoration: none; color: #FFFFFF; font-weight:bold;" href="http://www.infobae.com/2015/01/18/1621641-river-y-estudiantes-igualaron-goles-mar-del-plata" target="_blank">
River y Estudiantes igualaron sin goles en Mar del Plata
</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a style="text-decoration: none; color: #FFFFFF; font-weight:bold;" href="http://www.infobae.com/2015/01/18/1621638-sub-20-argentina-goleo-peru-gracias-una-rafaga-errores" target="_blank">
Sub 20: Argentina goleó a Perú gracias a una ráfaga de errores 
</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a style="text-decoration: none; color: #FFFFFF; font-weight:bold;" href="http://www.infobae.com/2015/01/18/1621574-las-luminarias-san-anton" target="_blank">
Las Luminarias de San Antón
</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a style="text-decoration: none; color: #FFFFFF; font-weight:bold;" href="http://www.infobae.com/2015/01/17/1621451-argentina-cayo-frente-paraguay-su-segunda-presentacion-el-sudamericano-sub-20" target="_blank">
Argentina cayó frente a Paraguay en su segunda presentación en el Sudamericano Sub 20
</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a style="text-decoration: none; color: #FFFFFF; font-weight:bold;" href="http://www.infobae.com/2015/01/16/1621215-simeone-volvio-quedarse-el-derby-madrid" target="_blank">
Simeone volvió a quedarse con el derby de Madrid
</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</div>

<script type="text/javascript" src="templates/js/webticker_lib.js" language="javascript"></script>




<table width="992" border="0"  align="center" style="border-style:none;">
  <tr>
    <td width="120"  align="left" valign="top" bordercolor="#FFFFFF" style="border-style:hidden">
      <div id="columnaIzquierda" class="column">
        <!--function doBlink() {    var blink = document.all.tags("BLINK")    for (var i=0; i<blink.length; i++)        blink[i].style.visibility = blink[i].style.visibility == "" ? "hidden" : "" }function startBlink() {    if (document.all)        setInterval("doBlink()",250)}window.onload = startBlink;*/// function validar(e) { // 1    tecla = (document.all) ? e.keyCode : e.which; // 2    if (tecla==8)  return true; // 3    //patron =/[A-Za-z-\w\t]/; // 4    patron = /[';?)($·".><!¿]/;    te = String.fromCharCode(tecla); // 5   return !patron.test(te); // 6}-->

<script type="text/javascript">function validar2(e) { tecla = (document.all) ? e.keyCode : e.which;    if (tecla==8)  return true;    patron =/[A-Za-z-\w\t]/;     patron = /[';?)($·".><!¿]/;    te = String.fromCharCode(tecla);    return !patron.test(te);    } </script>
<script src="Scripts/AC_RunActiveContent.js" type="text/javascript"></script><style>.boxMenuIzq66 {} </style>

<div id="menu14">     
    <ul>  
        
            <li><a href="index.php">Página Principal</a></li>    
            <li><a href="verComentarios.php">Dejanos tus comentarios</a></li>   
            <li><a href="http://foro.apuestaexitosa.com/" target="_blank">Ingresar al foro</a> </li>   
            <li><a href="registro.php">Registrate para ganar!</a></li>  

            
        <!-- Menu izquierdo -->     
        
            <li class="subMenu"><a href="jugarQuini6.php">Jugas Quini 6</a></li>  
            <li class="subMenu"><a href="jugarBrinco.php">Jugar Brinco</a></li>  
            <li class="subMenu"><a href="jugarQuiniela.php">Jugar Quiniela</a></li>  
            <li class="subMenu"><a href="jugarLoto.php">Jugar Loto</a></li>  
            <li class="subMenu"><a href="jugarLoto5.php">Jugar Loto 5</a></li> 
            <li><a href="horariosJuegos.php">Horarios de Sorteos</a></li>  
            <li><a href="cuadroPremios.php">¿Cuánto Gano?</a></li>  
            <!--<li><a href="reglamentosJuegos.php">Reglamentos</a></li>-->  
            <li><a href="reglamentos.php">Términos y condiciones</a></li>  
            <li><a href="contacto.php">Contáctenos</a></li>
    </ul>
</div>
<div style="float:left; margin:5px 0 5px 0;">
    <p>  <object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=7,0,19,0" width="200" height="158" align="left">    <param name="movie" value="../imagenes/design/tenesunagencia.swf" />    <param name="quality" value="high" />    <param name="wmode" value="transparent" /><param name="BGCOLOR" value="#CCCCCC" /><param name="SCALE" value="noborder" />    <embed src="../imagenes/design/tenesunagencia.swf" width="200" height="158" align="left" quality="high" pluginspage="http://www.macromedia.com/go/getflashplayer" type="application/x-shockwave-flash" bgcolor="#CCCCCC" wmode="transparent" scale="noborder"></embed>  </object></p>
</div>    
<div style="float:left; margin:5px 0 5px 0;">
        <p><a href="contacto.php"><img src="imagenes/design/contacto.jpg" border="0" /></a>  </p>
</div>      </div>
    </td>
    <td width="520" align="left" valign="top" bordercolor="#FFFFFF" style="border-style:hidden"><div  align="center" style="padding:3px 0px 3px 0px; display:block;  background-color:#FFFFFF; width:500px;  ">
      <div class="frmCaption" align="center"><br />
<br />
</div>

<table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td align="center">Resultado de los sorteos realizados el dia <b>19/01/2015</b></td>
    <td align="center">
Sorteos Anteriores:<br />
<form action="verResultadosQuiniela.php" method="post" enctype="multipart/form-data">
<select name="fecha_sorteo">
<option value="2015-01-19">19-01-2015</option>
<option value="2015-01-17">17-01-2015</option>
<option value="2015-01-16">16-01-2015</option>
<option value="2015-01-15">15-01-2015</option>
<option value="2015-01-14">14-01-2015</option>
<option value="2015-01-13">13-01-2015</option>
<option value="2015-01-12">12-01-2015</option>
<option value="2015-01-10">10-01-2015</option>
<option value="2015-01-09">09-01-2015</option>
<option value="2015-01-08">08-01-2015</option>
<option value="2015-01-07">07-01-2015</option>
<option value="2015-01-06">06-01-2015</option>
<option value="2015-01-05">05-01-2015</option>
<option value="2015-01-03">03-01-2015</option>
<option value="2015-01-02">02-01-2015</option>
</select><br />
<input type="submit" value="Ver Resultados" class="loginBoton" />
</form>
</td>

  </tr>
  
</table>
<div class="frmCaption" align="center" style="margin-bottom:10px"><b>Resultados del Sorteo La Primera</b></div>
<div align="center">
<table width="80%" bgcolor="#FFFFFF" cellspacing="1" cellpadding="5">
<tr bgcolor="#eaeaea">
<td>&nbsp;</td>
<td align="center" style="font-weight:bold;">Loteria Nacional</td>
<td align="center" style="font-weight:bold;">Loteria De Bs. As.</td>
<td align="center" style="font-weight:bold;">Loteria De Santa Fe</td>
<!--<td align="center" style="font-weight:bold;"></td>-->
<td align="center" style="font-weight:bold;">Loteria De Entre Rios</td>
</tr>

<tr bgcolor="#d0d0d0">
<td align="right" style ="font-weight:bold">1</td>
<td align="center" style ="font-weight:bold">5543</td>
<td align="center" style ="font-weight:bold">1656</td>
<td align="center" style ="font-weight:bold">6942</td>
<!--<td align="center" style ="font-weight:bold"></td>-->
<td align="center" style ="font-weight:bold">9034</td>
</tr>
<tr bgcolor="#eaeaea">
<td align="right" style ="font-weight:normal">2</td>
<td align="center" style ="font-weight:normal">2845</td>
<td align="center" style ="font-weight:normal">2670</td>
<td align="center" style ="font-weight:normal">0289</td>
<!--<td align="center" style ="font-weight:normal"></td>-->
<td align="center" style ="font-weight:normal">3457</td>
</tr>
<tr bgcolor="#d0d0d0">
<td align="right" style ="font-weight:normal">3</td>
<td align="center" style ="font-weight:normal">6320</td>
<td align="center" style ="font-weight:normal">6375</td>
<td align="center" style ="font-weight:normal">6940</td>
<!--<td align="center" style ="font-weight:normal"></td>-->
<td align="center" style ="font-weight:normal">9786</td>
</tr>
<tr bgcolor="#eaeaea">
<td align="right" style ="font-weight:normal">4</td>
<td align="center" style ="font-weight:normal">6702</td>
<td align="center" style ="font-weight:normal">1210</td>
<td align="center" style ="font-weight:normal">4438</td>
<!--<td align="center" style ="font-weight:normal"></td>-->
<td align="center" style ="font-weight:normal">2645</td>
</tr>
<tr bgcolor="#d0d0d0">
<td align="right" style ="font-weight:normal">5</td>
<td align="center" style ="font-weight:normal">1690</td>
<td align="center" style ="font-weight:normal">7613</td>
<td align="center" style ="font-weight:normal">2204</td>
<!--<td align="center" style ="font-weight:normal"></td>-->
<td align="center" style ="font-weight:normal">8048</td>
</tr>
<tr bgcolor="#eaeaea">
<td align="right" style ="font-weight:normal">6</td>
<td align="center" style ="font-weight:normal">3558</td>
<td align="center" style ="font-weight:normal">9074</td>
<td align="center" style ="font-weight:normal">7938</td>
<!--<td align="center" style ="font-weight:normal"></td>-->
<td align="center" style ="font-weight:normal">0600</td>
</tr>
<tr bgcolor="#d0d0d0">
<td align="right" style ="font-weight:normal">7</td>
<td align="center" style ="font-weight:normal">5861</td>
<td align="center" style ="font-weight:normal">2199</td>
<td align="center" style ="font-weight:normal">0251</td>
<!--<td align="center" style ="font-weight:normal"></td>-->
<td align="center" style ="font-weight:normal">9343</td>
</tr>
<tr bgcolor="#eaeaea">
<td align="right" style ="font-weight:normal">8</td>
<td align="center" style ="font-weight:normal">3365</td>
<td align="center" style ="font-weight:normal">3465</td>
<td align="center" style ="font-weight:normal">2276</td>
<!--<td align="center" style ="font-weight:normal"></td>-->
<td align="center" style ="font-weight:normal">1870</td>
</tr>
<tr bgcolor="#d0d0d0">
<td align="right" style ="font-weight:normal">9</td>
<td align="center" style ="font-weight:normal">9317</td>
<td align="center" style ="font-weight:normal">7961</td>
<td align="center" style ="font-weight:normal">0381</td>
<!--<td align="center" style ="font-weight:normal"></td>-->
<td align="center" style ="font-weight:normal">6602</td>
</tr>
<tr bgcolor="#eaeaea">
<td align="right" style ="font-weight:normal">10</td>
<td align="center" style ="font-weight:normal">6252</td>
<td align="center" style ="font-weight:normal">3960</td>
<td align="center" style ="font-weight:normal">5780</td>
<!--<td align="center" style ="font-weight:normal"></td>-->
<td align="center" style ="font-weight:normal">2730</td>
</tr>
<tr bgcolor="#d0d0d0">
<td align="right" style ="font-weight:normal">11</td>
<td align="center" style ="font-weight:normal">6676</td>
<td align="center" style ="font-weight:normal">2007</td>
<td align="center" style ="font-weight:normal">0925</td>
<!--<td align="center" style ="font-weight:normal"></td>-->
<td align="center" style ="font-weight:normal">9805</td>
</tr>
<tr bgcolor="#eaeaea">
<td align="right" style ="font-weight:normal">12</td>
<td align="center" style ="font-weight:normal">3563</td>
<td align="center" style ="font-weight:normal">7660</td>
<td align="center" style ="font-weight:normal">6697</td>
<!--<td align="center" style ="font-weight:normal"></td>-->
<td align="center" style ="font-weight:normal">2478</td>
</tr>
<tr bgcolor="#d0d0d0">
<td align="right" style ="font-weight:normal">13</td>
<td align="center" style ="font-weight:normal">0514</td>
<td align="center" style ="font-weight:normal">8884</td>
<td align="center" style ="font-weight:normal">6631</td>
<!--<td align="center" style ="font-weight:normal"></td>-->
<td align="center" style ="font-weight:normal">4395</td>
</tr>
<tr bgcolor="#eaeaea">
<td align="right" style ="font-weight:normal">14</td>
<td align="center" style ="font-weight:normal">5834</td>
<td align="center" style ="font-weight:normal">9782</td>
<td align="center" style ="font-weight:normal">1116</td>
<!--<td align="center" style ="font-weight:normal"></td>-->
<td align="center" style ="font-weight:normal">8996</td>
</tr>
<tr bgcolor="#d0d0d0">
<td align="right" style ="font-weight:normal">15</td>
<td align="center" style ="font-weight:normal">3562</td>
<td align="center" style ="font-weight:normal">4034</td>
<td align="center" style ="font-weight:normal">7957</td>
<!--<td align="center" style ="font-weight:normal"></td>-->
<td align="center" style ="font-weight:normal">7199</td>
</tr>
<tr bgcolor="#eaeaea">
<td align="right" style ="font-weight:normal">16</td>
<td align="center" style ="font-weight:normal">4211</td>
<td align="center" style ="font-weight:normal">1228</td>
<td align="center" style ="font-weight:normal">6921</td>
<!--<td align="center" style ="font-weight:normal"></td>-->
<td align="center" style ="font-weight:normal">9342</td>
</tr>
<tr bgcolor="#d0d0d0">
<td align="right" style ="font-weight:normal">17</td>
<td align="center" style ="font-weight:normal">6325</td>
<td align="center" style ="font-weight:normal">9690</td>
<td align="center" style ="font-weight:normal">9348</td>
<!--<td align="center" style ="font-weight:normal"></td>-->
<td align="center" style ="font-weight:normal">4821</td>
</tr>
<tr bgcolor="#eaeaea">
<td align="right" style ="font-weight:normal">18</td>
<td align="center" style ="font-weight:normal">3417</td>
<td align="center" style ="font-weight:normal">7575</td>
<td align="center" style ="font-weight:normal">5831</td>
<!--<td align="center" style ="font-weight:normal"></td>-->
<td align="center" style ="font-weight:normal">8942</td>
</tr>
<tr bgcolor="#d0d0d0">
<td align="right" style ="font-weight:normal">19</td>
<td align="center" style ="font-weight:normal">6919</td>
<td align="center" style ="font-weight:normal">3511</td>
<td align="center" style ="font-weight:normal">1193</td>
<!--<td align="center" style ="font-weight:normal"></td>-->
<td align="center" style ="font-weight:normal">9185</td>
</tr>
<tr bgcolor="#eaeaea">
<td align="right" style ="font-weight:normal">20</td>
<td align="center" style ="font-weight:normal">7196</td>
<td align="center" style ="font-weight:normal">0040</td>
<td align="center" style ="font-weight:normal">9189</td>
<!--<td align="center" style ="font-weight:normal"></td>-->
<td align="center" style ="font-weight:normal">5482</td>
</tr>
</table>
</div>
<br /><br /><br />
<div class="frmCaption" align="center" style="margin-bottom:10px"><b>Resultados del Sorteo Matutino</b></div>
<div align="center">
<table width="80%" bgcolor="#FFFFFF" cellspacing="1" cellpadding="5">
<tr bgcolor="#d0d0d0">
<td>&nbsp;</td>
<td align="center" style="font-weight:bold;">Loteria Nacional</td>
<td align="center" style="font-weight:bold;">Loteria De Bs. As.</td>
<td align="center" style="font-weight:bold;">Loteria De Santa Fe</td>
<!--<td align="center" style="font-weight:bold;"></td>-->
<td align="center" style="font-weight:bold;">Loteria De Entre Rios</td>
</tr>

<tr bgcolor="#eaeaea">
<td align="right" style ="font-weight:bold">1</td>
<td align="center" style ="font-weight:bold">1628</td>
<td align="center" style ="font-weight:bold">3172</td>
<td align="center" style ="font-weight:bold">8947</td>
<!--<td align="center" style ="font-weight:bold"></td>-->
<td align="center" style ="font-weight:bold">0618</td>
</tr>
<tr bgcolor="#d0d0d0">
<td align="right" style ="font-weight:normal">2</td>
<td align="center" style ="font-weight:normal">4234</td>
<td align="center" style ="font-weight:normal">8705</td>
<td align="center" style ="font-weight:normal">4729</td>
<!--<td align="center" style ="font-weight:normal"></td>-->
<td align="center" style ="font-weight:normal">6888</td>
</tr>
<tr bgcolor="#eaeaea">
<td align="right" style ="font-weight:normal">3</td>
<td align="center" style ="font-weight:normal">9801</td>
<td align="center" style ="font-weight:normal">4428</td>
<td align="center" style ="font-weight:normal">0316</td>
<!--<td align="center" style ="font-weight:normal"></td>-->
<td align="center" style ="font-weight:normal">9379</td>
</tr>
<tr bgcolor="#d0d0d0">
<td align="right" style ="font-weight:normal">4</td>
<td align="center" style ="font-weight:normal">6181</td>
<td align="center" style ="font-weight:normal">4425</td>
<td align="center" style ="font-weight:normal">9127</td>
<!--<td align="center" style ="font-weight:normal"></td>-->
<td align="center" style ="font-weight:normal">7820</td>
</tr>
<tr bgcolor="#eaeaea">
<td align="right" style ="font-weight:normal">5</td>
<td align="center" style ="font-weight:normal">7911</td>
<td align="center" style ="font-weight:normal">0886</td>
<td align="center" style ="font-weight:normal">1517</td>
<!--<td align="center" style ="font-weight:normal"></td>-->
<td align="center" style ="font-weight:normal">6202</td>
</tr>
<tr bgcolor="#d0d0d0">
<td align="right" style ="font-weight:normal">6</td>
<td align="center" style ="font-weight:normal">6933</td>
<td align="center" style ="font-weight:normal">9339</td>
<td align="center" style ="font-weight:normal">7258</td>
<!--<td align="center" style ="font-weight:normal"></td>-->
<td align="center" style ="font-weight:normal">6146</td>
</tr>
<tr bgcolor="#eaeaea">
<td align="right" style ="font-weight:normal">7</td>
<td align="center" style ="font-weight:normal">6411</td>
<td align="center" style ="font-weight:normal">9525</td>
<td align="center" style ="font-weight:normal">1827</td>
<!--<td align="center" style ="font-weight:normal"></td>-->
<td align="center" style ="font-weight:normal">4081</td>
</tr>
<tr bgcolor="#d0d0d0">
<td align="right" style ="font-weight:normal">8</td>
<td align="center" style ="font-weight:normal">1657</td>
<td align="center" style ="font-weight:normal">2201</td>
<td align="center" style ="font-weight:normal">2300</td>
<!--<td align="center" style ="font-weight:normal"></td>-->
<td align="center" style ="font-weight:normal">2022</td>
</tr>
<tr bgcolor="#eaeaea">
<td align="right" style ="font-weight:normal">9</td>
<td align="center" style ="font-weight:normal">1793</td>
<td align="center" style ="font-weight:normal">6683</td>
<td align="center" style ="font-weight:normal">5022</td>
<!--<td align="center" style ="font-weight:normal"></td>-->
<td align="center" style ="font-weight:normal">4062</td>
</tr>
<tr bgcolor="#d0d0d0">
<td align="right" style ="font-weight:normal">10</td>
<td align="center" style ="font-weight:normal">3302</td>
<td align="center" style ="font-weight:normal">4434</td>
<td align="center" style ="font-weight:normal">4863</td>
<!--<td align="center" style ="font-weight:normal"></td>-->
<td align="center" style ="font-weight:normal">0396</td>
</tr>
<tr bgcolor="#eaeaea">
<td align="right" style ="font-weight:normal">11</td>
<td align="center" style ="font-weight:normal">3906</td>
<td align="center" style ="font-weight:normal">1198</td>
<td align="center" style ="font-weight:normal">0338</td>
<!--<td align="center" style ="font-weight:normal"></td>-->
<td align="center" style ="font-weight:normal">3550</td>
</tr>
<tr bgcolor="#d0d0d0">
<td align="right" style ="font-weight:normal">12</td>
<td align="center" style ="font-weight:normal">5043</td>
<td align="center" style ="font-weight:normal">0330</td>
<td align="center" style ="font-weight:normal">2704</td>
<!--<td align="center" style ="font-weight:normal"></td>-->
<td align="center" style ="font-weight:normal">4029</td>
</tr>
<tr bgcolor="#eaeaea">
<td align="right" style ="font-weight:normal">13</td>
<td align="center" style ="font-weight:normal">5193</td>
<td align="center" style ="font-weight:normal">3951</td>
<td align="center" style ="font-weight:normal">9245</td>
<!--<td align="center" style ="font-weight:normal"></td>-->
<td align="center" style ="font-weight:normal">5812</td>
</tr>
<tr bgcolor="#d0d0d0">
<td align="right" style ="font-weight:normal">14</td>
<td align="center" style ="font-weight:normal">0277</td>
<td align="center" style ="font-weight:normal">7443</td>
<td align="center" style ="font-weight:normal">2095</td>
<!--<td align="center" style ="font-weight:normal"></td>-->
<td align="center" style ="font-weight:normal">5830</td>
</tr>
<tr bgcolor="#eaeaea">
<td align="right" style ="font-weight:normal">15</td>
<td align="center" style ="font-weight:normal">1834</td>
<td align="center" style ="font-weight:normal">7388</td>
<td align="center" style ="font-weight:normal">4699</td>
<!--<td align="center" style ="font-weight:normal"></td>-->
<td align="center" style ="font-weight:normal">8215</td>
</tr>
<tr bgcolor="#d0d0d0">
<td align="right" style ="font-weight:normal">16</td>
<td align="center" style ="font-weight:normal">2448</td>
<td align="center" style ="font-weight:normal">9484</td>
<td align="center" style ="font-weight:normal">5688</td>
<!--<td align="center" style ="font-weight:normal"></td>-->
<td align="center" style ="font-weight:normal">0737</td>
</tr>
<tr bgcolor="#eaeaea">
<td align="right" style ="font-weight:normal">17</td>
<td align="center" style ="font-weight:normal">6688</td>
<td align="center" style ="font-weight:normal">1601</td>
<td align="center" style ="font-weight:normal">3944</td>
<!--<td align="center" style ="font-weight:normal"></td>-->
<td align="center" style ="font-weight:normal">7180</td>
</tr>
<tr bgcolor="#d0d0d0">
<td align="right" style ="font-weight:normal">18</td>
<td align="center" style ="font-weight:normal">0537</td>
<td align="center" style ="font-weight:normal">0275</td>
<td align="center" style ="font-weight:normal">5160</td>
<!--<td align="center" style ="font-weight:normal"></td>-->
<td align="center" style ="font-weight:normal">4211</td>
</tr>
<tr bgcolor="#eaeaea">
<td align="right" style ="font-weight:normal">19</td>
<td align="center" style ="font-weight:normal">2561</td>
<td align="center" style ="font-weight:normal">3821</td>
<td align="center" style ="font-weight:normal">7560</td>
<!--<td align="center" style ="font-weight:normal"></td>-->
<td align="center" style ="font-weight:normal">9117</td>
</tr>
<tr bgcolor="#d0d0d0">
<td align="right" style ="font-weight:normal">20</td>
<td align="center" style ="font-weight:normal">9914</td>
<td align="center" style ="font-weight:normal">4696</td>
<td align="center" style ="font-weight:normal">8774</td>
<!--<td align="center" style ="font-weight:normal"></td>-->
<td align="center" style ="font-weight:normal">9950</td>
</tr>
</table>
</div>
<br><br><br>
<div class="frmCaption" align="center" style="margin-bottom:10px"><b>Resultados del Sorteo Vespertino</b></div>
<div align="center">
<table width="80%" bgcolor="#FFFFFF" cellspacing="1" cellpadding="5" align="center">
<tr bgcolor="#eaeaea">
<td>&nbsp;</td>
<td align="center" style="font-weight:bold;">Loteria Nacional</td>
<td align="center" style="font-weight:bold;">Loteria De Bs. As.</td>
<td align="center" style="font-weight:bold;">Loteria De Santa Fe</td>
<td align="center" style="font-weight:bold;">Loteria De Montevideo</td>
<td align="center" style="font-weight:bold;">Loteria De Entre Rios</td>
</tr>

<tr bgcolor="#d0d0d0">
<td align="right" style ="font-weight:bold">1</td>
<td align="center" style ="font-weight:bold">6283</td>
<td align="center" style ="font-weight:bold">0908</td>
<td align="center" style ="font-weight:bold">1591</td>
<td align="center" style ="font-weight:bold">523</td>
<td align="center" style ="font-weight:bold">3664</td>
</tr>
<tr bgcolor="#eaeaea">
<td align="right" style ="font-weight:normal">2</td>
<td align="center" style ="font-weight:normal">2751</td>
<td align="center" style ="font-weight:normal">9219</td>
<td align="center" style ="font-weight:normal">2140</td>
<td align="center" style ="font-weight:normal">334</td>
<td align="center" style ="font-weight:normal">6357</td>
</tr>
<tr bgcolor="#d0d0d0">
<td align="right" style ="font-weight:normal">3</td>
<td align="center" style ="font-weight:normal">4911</td>
<td align="center" style ="font-weight:normal">9795</td>
<td align="center" style ="font-weight:normal">4461</td>
<td align="center" style ="font-weight:normal">253</td>
<td align="center" style ="font-weight:normal">5058</td>
</tr>
<tr bgcolor="#eaeaea">
<td align="right" style ="font-weight:normal">4</td>
<td align="center" style ="font-weight:normal">5565</td>
<td align="center" style ="font-weight:normal">4059</td>
<td align="center" style ="font-weight:normal">7320</td>
<td align="center" style ="font-weight:normal">573</td>
<td align="center" style ="font-weight:normal">8676</td>
</tr>
<tr bgcolor="#d0d0d0">
<td align="right" style ="font-weight:normal">5</td>
<td align="center" style ="font-weight:normal">9534</td>
<td align="center" style ="font-weight:normal">9672</td>
<td align="center" style ="font-weight:normal">3587</td>
<td align="center" style ="font-weight:normal">308</td>
<td align="center" style ="font-weight:normal">4727</td>
</tr>
<tr bgcolor="#eaeaea">
<td align="right" style ="font-weight:normal">6</td>
<td align="center" style ="font-weight:normal">6225</td>
<td align="center" style ="font-weight:normal">5329</td>
<td align="center" style ="font-weight:normal">8133</td>
<td align="center" style ="font-weight:normal">014</td>
<td align="center" style ="font-weight:normal">3651</td>
</tr>
<tr bgcolor="#d0d0d0">
<td align="right" style ="font-weight:normal">7</td>
<td align="center" style ="font-weight:normal">5381</td>
<td align="center" style ="font-weight:normal">9844</td>
<td align="center" style ="font-weight:normal">6593</td>
<td align="center" style ="font-weight:normal">259</td>
<td align="center" style ="font-weight:normal">3467</td>
</tr>
<tr bgcolor="#eaeaea">
<td align="right" style ="font-weight:normal">8</td>
<td align="center" style ="font-weight:normal">9788</td>
<td align="center" style ="font-weight:normal">6210</td>
<td align="center" style ="font-weight:normal">7964</td>
<td align="center" style ="font-weight:normal">594</td>
<td align="center" style ="font-weight:normal">1121</td>
</tr>
<tr bgcolor="#d0d0d0">
<td align="right" style ="font-weight:normal">9</td>
<td align="center" style ="font-weight:normal">7788</td>
<td align="center" style ="font-weight:normal">7389</td>
<td align="center" style ="font-weight:normal">5132</td>
<td align="center" style ="font-weight:normal">208</td>
<td align="center" style ="font-weight:normal">1978</td>
</tr>
<tr bgcolor="#eaeaea">
<td align="right" style ="font-weight:normal">10</td>
<td align="center" style ="font-weight:normal">3937</td>
<td align="center" style ="font-weight:normal">7306</td>
<td align="center" style ="font-weight:normal">5978</td>
<td align="center" style ="font-weight:normal">626</td>
<td align="center" style ="font-weight:normal">8317</td>
</tr>
<tr bgcolor="#d0d0d0">
<td align="right" style ="font-weight:normal">11</td>
<td align="center" style ="font-weight:normal">7146</td>
<td align="center" style ="font-weight:normal">9673</td>
<td align="center" style ="font-weight:normal">4737</td>
<td align="center" style ="font-weight:normal">073</td>
<td align="center" style ="font-weight:normal">0254</td>
</tr>
<tr bgcolor="#eaeaea">
<td align="right" style ="font-weight:normal">12</td>
<td align="center" style ="font-weight:normal">7057</td>
<td align="center" style ="font-weight:normal">4600</td>
<td align="center" style ="font-weight:normal">0616</td>
<td align="center" style ="font-weight:normal">454</td>
<td align="center" style ="font-weight:normal">9859</td>
</tr>
<tr bgcolor="#d0d0d0">
<td align="right" style ="font-weight:normal">13</td>
<td align="center" style ="font-weight:normal">2677</td>
<td align="center" style ="font-weight:normal">5173</td>
<td align="center" style ="font-weight:normal">6432</td>
<td align="center" style ="font-weight:normal">744</td>
<td align="center" style ="font-weight:normal">8109</td>
</tr>
<tr bgcolor="#eaeaea">
<td align="right" style ="font-weight:normal">14</td>
<td align="center" style ="font-weight:normal">0429</td>
<td align="center" style ="font-weight:normal">5194</td>
<td align="center" style ="font-weight:normal">2739</td>
<td align="center" style ="font-weight:normal">227</td>
<td align="center" style ="font-weight:normal">7202</td>
</tr>
<tr bgcolor="#d0d0d0">
<td align="right" style ="font-weight:normal">15</td>
<td align="center" style ="font-weight:normal">8910</td>
<td align="center" style ="font-weight:normal">1838</td>
<td align="center" style ="font-weight:normal">4811</td>
<td align="center" style ="font-weight:normal">652</td>
<td align="center" style ="font-weight:normal">7376</td>
</tr>
<tr bgcolor="#eaeaea">
<td align="right" style ="font-weight:normal">16</td>
<td align="center" style ="font-weight:normal">9152</td>
<td align="center" style ="font-weight:normal">2247</td>
<td align="center" style ="font-weight:normal">9602</td>
<td align="center" style ="font-weight:normal">253</td>
<td align="center" style ="font-weight:normal">2914</td>
</tr>
<tr bgcolor="#d0d0d0">
<td align="right" style ="font-weight:normal">17</td>
<td align="center" style ="font-weight:normal">5364</td>
<td align="center" style ="font-weight:normal">8422</td>
<td align="center" style ="font-weight:normal">9911</td>
<td align="center" style ="font-weight:normal">556</td>
<td align="center" style ="font-weight:normal">2659</td>
</tr>
<tr bgcolor="#eaeaea">
<td align="right" style ="font-weight:normal">18</td>
<td align="center" style ="font-weight:normal">8354</td>
<td align="center" style ="font-weight:normal">5330</td>
<td align="center" style ="font-weight:normal">2094</td>
<td align="center" style ="font-weight:normal">404</td>
<td align="center" style ="font-weight:normal">4419</td>
</tr>
<tr bgcolor="#d0d0d0">
<td align="right" style ="font-weight:normal">19</td>
<td align="center" style ="font-weight:normal">7372</td>
<td align="center" style ="font-weight:normal">7511</td>
<td align="center" style ="font-weight:normal">2947</td>
<td align="center" style ="font-weight:normal">903</td>
<td align="center" style ="font-weight:normal">3698</td>
</tr>
<tr bgcolor="#eaeaea">
<td align="right" style ="font-weight:normal">20</td>
<td align="center" style ="font-weight:normal">8891</td>
<td align="center" style ="font-weight:normal">0456</td>
<td align="center" style ="font-weight:normal">2119</td>
<td align="center" style ="font-weight:normal">137</td>
<td align="center" style ="font-weight:normal">7398</td>
</tr>
</table>
</div>
<br><br><br>
Esperando resultados del sorteo nocturno

    </div></td>
    <td width="65"  valign="top" align="left"    style="bordercolor:#FFFFFF;border-style:none; ">
      <div>
        <style type="text/css">







<!--







body {







    margin-left: 0px;







    margin-top: 0px;







    margin-right: 0px;







    margin-bottom: 0px;







}







.cuadrosoporte{font-family:Tahoma; color:#000000; font-size:10px; margin-bottom:10px;}



.cuadroestadisticas{font-family:Tahoma;color:#000000;font-size:12px;}



-->







</style><!--width="194" height="166"-->







<table width="200" border="0" style="float:right; margin-right:0px; paddign-right:0px;">

 <tr>
    <td height="100" align="center"><object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=7,0,19,0" width="200" height="100">
      <param name="movie" value="imagenes/design/banner_extracto.swf" />
      <param name="quality" value="high" />
      <embed src="imagenes/design/banner_extracto.swf" quality="high" pluginspage="http://www.macromedia.com/go/getflashplayer" type="application/x-shockwave-flash" width="200" height="100"></embed>
    </object></td>
  </tr>
<tr>
 <tr>
    <td height="100" align="center"><object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=7,0,19,0" width="200" height="100">
      <param name="movie" value="imagenes//design/registrate.swf" />
      <param name="quality" value="high" />
      <embed src="imagenes//design/registrate.swf" quality="high" pluginspage="http://www.macromedia.com/go/getflashplayer" type="application/x-shockwave-flash" width="200" height="100"></embed>
    </object></td>
  </tr>
<tr>
<td align="center">
<a href="http://www.ganadineroalaruleta.com.ar" target="_blank"><img src="imagenes/design/gana_ruleta.jpg" width="200"></a><br />
</td>  
</tr>
<tr>
<td height="62" align="center" style="border:solid green;"><img src="imagenes//numero_del_dia.jpeg" width="135" height="135" /><br /><a href="histotial_de_palpito.php" style="color:#000000">Clic aqu&iacute; para ver datos anteriores</a></td>
</tr>

<tr>
<td></td>
</tr>


  <tr>







    <td width="100" height="166" align="left" valign="top" style="background:url(imagenes//support.gif) no-repeat;"><div class="cuadrosoporte" id="cuadrosoporte">







      <div>







        <p>CONTACTO MSN:operador@quinielasargentinas.com</p>







        <div><img src="imagenes//design/msn1.png" alt="" width="52" height="51" align="left" /></div>
      </div>







    </div></td>
  </tr>



  <tr>



    <td height="116" align="left" valign="top" background="imagenes//design/estadisticas.png" style="background-repeat:no-repeat;"><div class="cuadroestadisticas">



      <p align="center">&iquest;Quer&eacute;s saber como viene <br/> 

      saliendo tu n&uacute;mero? </p>



      <p align="center"><a href="http://www.loteriasmundiales.com.ar/index.asp?pagina=E" target="_blank">Vea Estad&iacute;sticas </a></p>



    </div></td>
  </tr>
</table>









<a href="http://www.dolarsi.com" target="_blank"></a>
<p>&nbsp;</p>







      </div>
    </td>
  </tr>
</table>


<div id ="footer-wrapper" >
    <div align="center" style="width:980px;color:black;" >
<table width="390" border="0" align="center" cellpadding="0" cellspacing="0">

      <tr>



        <td width="81" height="54" valign="baseline"><div align="center"><a href="verResultadosQuini6.php"><img src="imagenes/lg-quini6.jpg" width="77" height="50" /></a></div></td>



        <td width="106" valign="baseline"><a href="verResultadosBrinco.php"><img src="imagenes/lg-brinco.jpg" width="77" height="50" border="0" /></a></td>



        <td width="81"><a href="verResultadosQuiniela.php"><img src="imagenes/lg-quiniela.jpg" width="77" height="50" /></a></td>



        <td width="74"><div align="center"><a href="verResultadosLoto.php"><img src="imagenes/lg-loto.jpg" width="77" height="50" border="0" /></a></div></td>



        <td width="109" background="imagenes/design/frm_registro_bg.gif"><a href="verResultadosLoto5.php"><img src="imagenes/lg-loto5.jpg" width="77" height="50" border="0" /></a></td>
      </tr>
      <tr style="color:black;">
        <td height="19" align="center" valign="baseline"><p class="Estilo7" style="color:black;">QUINI 6 </p>        </td>
        <td height="19" align="center" valign="baseline"><span class="Estilo7">BRINCO</span></td>
        <td height="19" align="center" valign="baseline"><span class="Estilo7">QUINIELA</span></td>
        <td height="19" align="center" valign="baseline"><span class="Estilo7">LOTO</span></td>
        <td height="19" align="center" valign="baseline"><span class="Estilo7">LOTO5</span></td>
      </tr>
      <tr style="color:black;">
        <td height="54" colspan="5" align="center"  valign="baseline"><div align="center" class="Estilo4" style="color:green;"> Click en el Juego para ver resultados</div></td>
      </tr>
  </table>






        <span class="txtBottomCaption" style="align:center;">



        <a href="reglamentos.php">T&eacute;rminos y Condiciones de Uso Aceptable</a> | &copy; 2009 Todos los derechos reservados<br> Ante cualquier duda o reclamo contáctese con nosotros por email a contacto@quinielasargentinas.com o por MSN a operador@quinielasargentinas.com</span>    
        </div>


</div>
</td>
</tr>
</table>

<script type="text/javascript">
var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type="text/javascript">
try{
var pageTracker = _gat._getTracker("UA-6687996-2");
pageTracker._trackPageview();
} catch(err) {}
</script>

</body>


</html>

"""

import urllib
from bs4 import BeautifulSoup
from urllib2 import URLError
import sys
import urllib2
sys.path.append('./')

param = urllib.urlencode({'fecha_sorteo': '2015-02-03'})

response = urllib2.urlopen(
            'http://www.quinielasargentinas.com/verResultadosQuiniela.php', 
            param)

soup = BeautifulSoup(response.read())

#print "_______________________"
#print soup.select('td')
#print "_______________________"

#soup = BeautifulSoup(html)

td_tags = soup.select('td')

NAC, BSA, SFE, ERI = range(4)

PRE, MAT, VES, NOC = range(4)

cont = -1
cant_1 = 0
intervalo = 5

horario = NOC
cant_num = 99
lot = SFE
if horario > MAT:# and lot > SFE: #Si la loteria es VES o NOC y se quiere 
    intervalo = 6
    cant_num = 119
    if lot > SFE:
        lot = lot + 1
if horario > VES:
    intervalo = 7
    cant_num = 140
    

for td in td_tags:
    cont = cont + 1
    
    if td.text == '1':
        cant_1 = cant_1 + 1
        if cant_1  == horario + 1:
            break
        
print "CONTADOR: ", cont

#Quiniela de Santa fe
pos = lot + 1
lstNumeros = []
for i in range(cont + pos, cont+pos+cant_num, intervalo):
    lstNumeros.append(td_tags[i].text)
    
print lstNumeros
        
#print len(td_tags)
#print td_tags[14].text
#print td_tags[113].text

#print td_tags[119].text
#print td_tags[218].text

#print td_tags[225].text
#print td_tags[344].text

#print td_tags[351].text
#print td_tags[470].text