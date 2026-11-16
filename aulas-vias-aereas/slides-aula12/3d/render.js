const {chromium}=require('playwright');
const path=require('path');
(async()=>{
  const b=await chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--allow-file-access-from-files']});
  const jobs=(process.argv[2]?JSON.parse(process.argv[2]):[['via',1100,1080],['som',1100,1080],['esteto',1100,900],['lua',900,900],['escudo',900,900]]);
  for(const [k,w,h,ex='',out=k] of jobs){
    const p=await b.newPage({viewport:{width:w,height:h}});
    p.on('console',m=>console.log(k,m.text())); p.on('pageerror',e=>console.log(k,'ERR',e.message));
    await p.goto('file://'+path.resolve(__dirname,'cena.html')+`?k=${k}&w=${w}&h=${h}${ex}`);
    await p.waitForFunction(()=>document.title==='ok',null,{timeout:60000});
    await p.waitForTimeout(500);
    await p.screenshot({path:path.resolve(__dirname,`../img/${out}.png`),omitBackground:true});
    await p.close(); console.log('ok',k);
  }
  await b.close();
})();
