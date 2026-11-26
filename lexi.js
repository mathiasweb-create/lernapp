/* Lexi, das Maskottchen (Fuchs): Figur, Sprechblasen und Sprüche. © 2026 Mathias Blanck. Alle Rechte vorbehalten. */
(function(){
'use strict';
var $=function(s){return document.querySelector(s)};
var esc=function(s){return String(s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})};
  var INK='#14213D';
  function eyes(mood){
    var y=112,dx=32,r=19,pr=9.5,L=120-dx,R=120+dx,s='';
    if(mood==='happy') return '<path d="M'+(L-r*.8)+' '+(y+4)+'q'+(r*.8)+' '+(-r*1.2)+' '+(r*1.6)+' 0M'+(R-r*.8)+' '+(y+4)+'q'+(r*.8)+' '+(-r*1.2)+' '+(r*1.6)+' 0" fill="none" stroke="'+INK+'" stroke-width="6" stroke-linecap="round"/>';
    if(mood==='angry'){[L,R].forEach(function(cx,i){s+='<g class="eye'+(i?' r':'')+'"><circle cx="'+cx+'" cy="'+(y+2)+'" r="'+r+'" fill="#fff" stroke="rgba(20,33,61,.35)" stroke-width="2"/><circle cx="'+(cx+(i?-3:3))+'" cy="'+(y+4)+'" r="7.5" fill="'+INK+'"/></g>'});
      s+='<path d="M'+(L-r-2)+' '+(y-r-6)+'L'+(L+r)+' '+(y-r+8)+'M'+(R+r+2)+' '+(y-r-6)+'L'+(R-r)+' '+(y-r+8)+'" fill="none" stroke="'+INK+'" stroke-width="6" stroke-linecap="round"/>';return s}
    var ox=mood==='think'?6:0,oy=mood==='think'?-5:(mood==='sad'?3:0);
    [L,R].forEach(function(cx,i){s+='<g class="eye'+(i?' r':'')+'"><circle cx="'+cx+'" cy="'+y+'" r="'+r+'" fill="#fff" stroke="rgba(20,33,61,.35)" stroke-width="2"/><circle cx="'+(cx+ox)+'" cy="'+(y+oy)+'" r="'+pr+'" fill="'+INK+'"/><circle cx="'+(cx+ox+3.3)+'" cy="'+(y+oy-3.3)+'" r="3.6" fill="#fff"/></g>'});
    if(mood==='sad') s+='<path d="M'+(L-r)+' '+(y-r-3)+'q'+r+' 0 '+(r*1.5)+' '+(r*.7)+'M'+(R+r)+' '+(y-r-3)+'q'+(-r)+' 0 '+(-r*1.5)+' '+(r*.7)+'" fill="none" stroke="'+INK+'" stroke-width="4.5" stroke-linecap="round"/>';
    return s;
  }
  function mouth(mood){
    if(mood==='happy') return '<path d="M109 152q11 17 22 0z" fill="#C8433A" stroke="'+INK+'" stroke-width="2.5" stroke-linejoin="round"/>';
    if(mood==='angry') return '<path d="M108 160q12 -12 24 0" fill="none" stroke="'+INK+'" stroke-width="4" stroke-linecap="round"/>';
    if(mood==='sad') return '<path d="M112 158q8 -9 16 0" fill="none" stroke="'+INK+'" stroke-width="3.5" stroke-linecap="round"/>';
    if(mood==='think') return '<path d="M114 155h12" fill="none" stroke="'+INK+'" stroke-width="3.5" stroke-linecap="round"/>';
    return '<path d="M111 152q9 9 18 0" fill="none" stroke="'+INK+'" stroke-width="3.5" stroke-linecap="round"/>';
  }
  function extras(mood){
    if(mood==='think') return '<circle cx="204" cy="52" r="6" fill="#B9C9F2"/><circle cx="216" cy="30" r="11" fill="#B9C9F2"/><text x="216" y="36" text-anchor="middle" font-family="Georgia,serif" font-weight="700" font-size="16" fill="#2457D6">?</text>';
    if(mood==='angry'){var m='',c=['#8A8F9C','#3E4350','#C9CDD6','#6B7080','#A5AAB7'],k=0;for(var yy=0;yy<4;yy++)for(var xx=0;xx<4;xx++){m+='<rect x="'+(196+xx*9)+'" y="'+(46+yy*9)+'" width="9" height="9" fill="'+c[(xx*3+yy*2+k++)%5]+'"/>'}
      return '<path d="M158 176Q216 160 214 108" fill="none" stroke="#E8782A" stroke-width="28" stroke-linecap="round"/><circle cx="214" cy="100" r="19" fill="#E8782A"/><path d="M188 36l-6 -14M206 32l0 -16M224 36l6 -14" stroke="#C0362C" stroke-width="4" stroke-linecap="round" fill="none"/>'+m;}
    if(mood==='happy') return '<path d="M26 46l4 9 9 1-7 6 2 9-8-5-8 5 2-9-7-6 9-1zM208 70l3 7 7 1-5 5 1 7-6-4-6 4 1-7-5-5 7-1z" fill="#F2A93B"/>';
    return '';
  }
  function lexi(mood,cls){
    cls=cls||'';mood=mood||'normal';
    var wy=cls.indexOf('windy')>=0,jail='';
    if(cls.indexOf('bars')>=0){jail='<g class="jail" fill="#4A4F5C" opacity=".8">';for(var bi=0;bi<9;bi++)jail+='<rect x="'+(24+bi*24)+'" y="18" width="4" height="228" rx="2"/>';jail+='</g>'}
    var wind='';
    var front=wy?'<g class="wnd" stroke-width="2.6" stroke-linecap="round"><g class="wf"><path d="M24 200h28c9 0 9 -12 2 -12c-6 0 -6 7 -1 8"/></g><g class="wf b"><path d="M128 228h26c9 0 9 -12 2 -12c-6 0 -6 7 -1 8"/></g><g class="wf c"><path d="M150 178h24c8 0 8 -11 2 -11c-6 0 -6 7 -1 7"/></g></g><g class="leaf"><g transform="scale(1.15)"><path d="M0 -12C9 -8 11 4 0 14C-11 4 -9 -8 0 -12z" fill="#C2410C"/><path d="M0 -10V16" stroke="#7C2A08" stroke-width="1.6" stroke-linecap="round" fill="none"/><path d="M0 2l5 -5M0 8l-5 -5" stroke="#7C2A08" stroke-width="1.2" stroke-linecap="round" fill="none"/></g></g>':'';
    return '<svg class="m '+cls+'" viewBox="0 0 240 260" role="img" aria-label="Lexi, der Fuchs">'+wind
     +'<ellipse cx="120" cy="250" rx="64" ry="7" fill="#14213D" opacity=".12"/>'
     +'<g class="fx"><g class="tail"><path d="M168 214C240 214 250 140 214 104C212 150 196 170 164 180z" fill="#E8782A"/><path d="M214 104C230 128 232 150 226 168C214 150 210 126 214 104z" fill="#FFF1DC"/></g>'
     +'<path d="M54 76L46 22L96 58zM186 76L194 22L144 58z" fill="#E8782A"/><path d="M60 64L56 38L82 58zM180 64L184 38L158 58z" fill="#5A2E14"/>'
     +'<ellipse cx="120" cy="192" rx="52" ry="54" fill="#E8782A"/><ellipse cx="120" cy="204" rx="32" ry="38" fill="#FFF1DC"/>'
     +'<ellipse cx="96" cy="242" rx="17" ry="8" fill="#5A2E14"/><ellipse cx="144" cy="242" rx="17" ry="8" fill="#5A2E14"/>'
     +'<g class="s1"><path d="M148 184Q168 174 190 186L188 206Q168 196 148 204z" fill="#2457D6"/><g class="s2"><path d="M188 186Q210 176 232 188L228 208Q208 198 188 206z" fill="#3D6FE8"/><g class="s3"><path d="M230 188Q250 180 270 190L264 208Q248 200 228 208z" fill="#2457D6"/><path d="M252 184l-3 24M262 188l-3 22" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".85"/></g></g></g>'
     +'<path d="M38 122Q38 60 120 60Q202 60 202 122Q202 152 172 162Q120 178 68 162Q38 152 38 122z" fill="#E8782A"/>'
     +'<path d="M38 122Q64 168 120 154Q176 168 202 122Q186 166 120 176Q54 166 38 122z" fill="#FFF1DC"/>'
     +'<g class="nk"><path d="M78 172Q120 192 162 172L166 190Q120 210 74 190z" fill="#2457D6"/></g>'
     +eyes(mood)+'<ellipse cx="120" cy="142" rx="8" ry="6" fill="#2B1B14"/>'+mouth(mood)
     +'<ellipse cx="58" cy="144" rx="9" ry="6" fill="#FF8FA3" opacity=".65"/><ellipse cx="182" cy="144" rx="9" ry="6" fill="#FF8FA3" opacity=".65"/></g>'
     +extras(mood)+front+jail+'</svg>';
  }


  var NS='http://www.w3.org/2000/svg';
  function paint(el){
    var o=el.querySelector(':scope > .bs');if(o)o.remove();
    var w=el.offsetWidth,h=el.offsetHeight;if(!w||!h)return;
    var rx=w/2-2,ry=h/2-2,cx=w/2,cy=h/2,mode=el.dataset.t||'l',rad=Math.PI/180;
    var P=function(th,k){k=k||0;return [cx+(rx-k)*Math.cos(th),cy+(ry-k*.7)*Math.sin(th)]};
    var th,dl,tip,tx;
    if(mode==='l'){var fb=el.parentNode&&el.parentNode.querySelector('.mb'),my=h*.62;if(fb){var fh=fb.offsetHeight;my=(h-fh)/2+fh*(152/260)}
      my=Math.max(h*.25,Math.min(h*.88,my));var ry0=Math.max(1,ry),rootY=Math.max(h*.22,Math.min(h*.85,my-6));th=Math.PI-Math.asin(Math.max(-.95,Math.min(.95,(rootY-cy)/ry0)));dl=.2;tip=[-30,my]}
    else if(mode==='h'){var ty=h/2+Math.max(3,h*.12),ry1=Math.max(1,ry);th=Math.asin(Math.max(-.9,Math.min(.9,(ty-4-cy)/ry1)));dl=.22;tip=[w+13,ty]}
    else{tx=mode==='s'?+el.dataset.tx:cx;tx=Math.max(cx-rx*.8,Math.min(cx+rx*.8,tx));th=-Math.acos((tx-cx)/rx);dl=.13;var R2=P(th);tip=[tx,R2[1]-21]}
    var p1=P(th-dl),p2=P(th+dl),f=function(p){return p[0].toFixed(1)+' '+p[1].toFixed(1)};
    var c1=[(p1[0]+tip[0])/2+(p2[0]-p1[0])*.35,(p1[1]+tip[1])/2+(p2[1]-p1[1])*.35],c2=[(p2[0]+tip[0])/2+(p1[0]-p2[0])*.35,(p2[1]+tip[1])/2+(p1[1]-p2[1])*.35];
    var d='M'+f(p2)+' A'+rx.toFixed(1)+' '+ry.toFixed(1)+' 0 1 1 '+f(p1)+' Q'+f(c1)+' '+f(tip)+' Q'+f(c2)+' '+f(p2)+'Z';
    var hs='';if(h>34){for(var k=0;k<11;k++){var a=(152+k*7)*rad,A=P(a,3),B=P(a+.1,12);hs+='M'+f(A)+'L'+f(B)}}
    var s=document.createElementNS(NS,'svg');s.setAttribute('class','bs');s.setAttribute('aria-hidden','true');
    s.innerHTML='<path d="'+d+'" fill="#fff" stroke="#111" stroke-width="1.8" stroke-linejoin="round" filter="url(#rough)"/><path d="'+hs+'" fill="none" stroke="#B5B5B5" stroke-width="1" stroke-linecap="round"/>';
    el.insertBefore(s,el.firstChild);
  }
  function paintAll(){document.querySelectorAll('.bub').forEach(paint)}

var SAYS=['Huggi Guggi','Den Truthahn würgen','Kollege Lenz','Willkommen im Kurs, Kollege Zorn','Maschinengewehr Gottes','Diesen Hier!','Hundsviech-Paragraf','Dann gehn ma sitzen','Meine Damen und Herren'],ANGRY=5,BARS=7;
if(document.fonts&&document.fonts.load){try{document.fonts.load('700 12px "Comic Neue"')}catch(e){}}
var sayT=null,idleT=null,lastSay=0,sayN=0,blocked=false,enabled=true;
function hide(){var e=$('#say');if(e)e.classList.remove('show');var a=$('#app');if(a)a.classList.remove('hush')}
function say(t,mood){
  var e=$('#say'),mn=$('#app .lmini svg');if(!e||!mn||blocked||!enabled)return;
  var lm=mn.parentNode;
  e.innerHTML='<span>'+esc(t)+'</span>';
  e.classList.remove('show');e.style.left='0px';e.style.top='0px';e.dataset.t='h';
  var r=mn.getBoundingClientRect(),w=e.offsetWidth,h=e.offsetHeight;
  e.style.left=Math.max(6,r.left-w-16)+'px';e.style.top=Math.round(r.top+r.height/2-h/2)+'px';
  paint(e);void e.offsetWidth;e.classList.add('show');$('#app').classList.add('hush');
  if(mood==='angry'){lm.innerHTML=lexi('angry');setTimeout(function(){if(lm.isConnected)lm.innerHTML=lexi('normal')},2800)}
  lastSay=Date.now();clearTimeout(sayT);sayT=setTimeout(hide,mood?3400:3000);
}
function sayIdx(i){if(i===ANGRY)say(SAYS[i],'angry');else if(i===BARS)say(SAYS[i],'normal','bars');else say(SAYS[i])}
var SHORT=['Huggi Guggi','Den Truthahn würgen','Kollege Lenz','Diesen Hier!'];
function sayShort(i){say(SHORT[i],i===3?'angry':null)}
function idle(on,minMs,maxMs){
  clearTimeout(idleT);if(!on||blocked||!enabled)return;
  idleT=setTimeout(function(){if(blocked||!enabled||Date.now()-lastSay<60000||!$('#app .lmini svg'))return;sayShort(Math.floor(Math.random()*SHORT.length))},minMs+Math.random()*(maxMs-minMs));
}
window.Lexi={svg:lexi,paint:paint,paintAll:paintAll,say:say,sayIdx:sayIdx,sayShort:sayShort,SHORT:SHORT,idle:idle,hide:hide,SAYS:SAYS,ANGRY:ANGRY,BARS:BARS,
  next:function(){sayShort(sayN++%SHORT.length)},
  block:function(b){blocked=!!b;if(b){hide();clearTimeout(idleT)}},
  enable:function(b){enabled=!!b;if(!b){hide();clearTimeout(idleT)}}};
})();
