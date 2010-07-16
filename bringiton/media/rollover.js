function mm_swapImgRestore() { //v3.0
  var i,x,a=document.mm_sr; for(i=0;a&&i<a.length&&(x=a[i])&&x.oSrc;i++) x.src=x.oSrc;
}

function mm_preloadImages() { //v3.0
  var d=document; if(d.images){ if(!d.mm_p) d.mm_p=new Array();
    var i,j=d.mm_p.length,a=mm_preloadImages.arguments; for(i=0; i<a.length; i++)
    if (a[i].indexOf("#")!=0){ d.mm_p[j]=new Image; d.mm_p[j++].src=a[i];}}
}

function mm_findObj(n, d) { //v4.01
  var p,i,x;  if(!d) d=document; if((p=n.indexOf("?"))>0&&parent.frames.length) {
    d=parent.frames[n.substring(p+1)].document; n=n.substring(0,p);}
  if(!(x=d[n])&&d.all) x=d.all[n]; for (i=0;!x&&i<d.forms.length;i++) x=d.forms[i][n];
  for(i=0;!x&&d.layers&&i<d.layers.length;i++) x=mm_findObj(n,d.layers[i].document);
  if(!x && d.getElementById) x=d.getElementById(n); return x;
}

function mm_swapImage() { //v3.0
  var i,j=0,x,a=mm_swapImage.arguments; document.mm_sr=new Array; for(i=0;i<(a.length-2);i+=3)
   if ((x=mm_findObj(a[i]))!=null){document.mm_sr[j++]=x; if(!x.oSrc) x.oSrc=x.src; x.src=a[i+2];}
}