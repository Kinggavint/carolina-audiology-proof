(function(){
  var d=document.documentElement; d.classList.add('js');
  var reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
  // staggered entrance for the parts of every section
  document.querySelectorAll('[data-stagger]').forEach(function(group){
    Array.prototype.forEach.call(group.querySelectorAll('[data-rise]'),function(el,i){el.style.setProperty('--d',(i*75)+'ms');});
  });
  var els=document.querySelectorAll('[data-rise]');
  if(!('IntersectionObserver' in window)||reduce){els.forEach(function(e){e.classList.add('in');});}
  else{
    var io=new IntersectionObserver(function(entries){entries.forEach(function(en){if(en.isIntersecting){en.target.classList.add('in');io.unobserve(en.target);}});},{rootMargin:'0px 0px -8% 0px',threshold:0.08});
    els.forEach(function(e){io.observe(e);});
    setTimeout(function(){els.forEach(function(e){var r=e.getBoundingClientRect();if(r.top<innerHeight&&r.bottom>0)e.classList.add('in');});},60);
  }
  // first visit diagram: dots gather as the section scrolls in
  var dg=document.querySelector('.diagram');
  if(dg&&!reduce&&'IntersectionObserver' in window){
    var dots=dg.querySelectorAll('circle[data-x]');
    dots.forEach(function(c){c.style.transform='translate('+c.dataset.x+'px,'+c.dataset.y+'px)';});
    new IntersectionObserver(function(en,o){if(en[0].isIntersecting){dots.forEach(function(c,i){c.style.transitionDelay=(i%40)*12+'ms';c.style.transform='none';});o.disconnect();}},{threshold:.25}).observe(dg);
  }
  // appointment form: prefill reason from ?reason=, preview-only submit
  var f=document.getElementById('request-form');
  if(f){
    var q=new URLSearchParams(location.search).get('reason');
    if(q&&f.reason){Array.prototype.forEach.call(f.reason.options,function(o){if(o.value===q)o.selected=true;});}
    f.addEventListener('submit',function(e){
      e.preventDefault();
      var done=document.getElementById('form-done');
      var name=(f.name.value||'').trim();
      done.querySelector('[data-name]').textContent=name?(', '+name.split(' ')[0]):'';
      done.classList.add('show'); done.setAttribute('tabindex','-1'); done.focus();
    });
  }
})();
