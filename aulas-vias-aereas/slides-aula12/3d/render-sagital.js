const {chromium}=require('playwright'); const path=require('path');
// uso: node render-sagital.js saida.png largura altura [x0,y0,x1,y1]
(async()=>{
  const [out,w,h,crop]=process.argv.slice(2);
  const b=await chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--allow-file-access-from-files']});
  const p=await b.newPage({viewport:{width:+w,height:+h}});
  await p.addInitScript(t=>{window.SVGTXT=t}, require('fs').readFileSync(path.resolve(__dirname,'sagital.svg'),'utf8'));
  p.on('console',m=>console.log(m.text())); p.on('pageerror',e=>console.log('ERR',e.message));
  await p.goto('file://'+path.resolve(__dirname,'cena-sagital.html')+`?w=${w}&h=${h}`+(crop?`&crop=${crop}`:''));
  await p.waitForFunction(()=>document.title==='ok',null,{timeout:90000});
  await p.waitForTimeout(400);
  await p.screenshot({path:path.resolve(out),omitBackground:true}); await b.close(); console.log('ok',out);
})();
