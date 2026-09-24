from .tools import create
def create_snake(name):
 html="""<!doctype html><meta name=viewport content='width=device-width'><canvas id=c width=360 height=600></canvas><script>
const x=c.getContext('2d');let s=[[5,5]],a=[10,10],d=[1,0],score=0;
setInterval(()=>{let h=[s[0][0]+d[0],s[0][1]+d[1]];if(h[0]<0||h[1]<0||h[0]>=18||h[1]>=30)return;
s.unshift(h);if(h[0]==a[0]&&h[1]==a[1]){score++;a=[Math.random()*18|0,Math.random()*30|0]}else s.pop();
x.clearRect(0,0,360,600);x.fillText('Score '+score,10,15);s.forEach(p=>x.fillRect(p[0]*20,p[1]*20,18,18));x.fillRect(a[0]*20,a[1]*20,18,18)},120);
onkeydown=e=>{if(e.key=='ArrowUp')d=[0,-1];if(e.key=='ArrowDown')d=[0,1];if(e.key=='ArrowLeft')d=[-1,0];if(e.key=='ArrowRight')d=[1,0]}</script>"""
 return create(name+"/index.html",html)
