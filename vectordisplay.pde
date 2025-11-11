void setup(){
  frameRate(40);
  size(500,500);
  background(255,255,255);
}

void draw(){
  //lines
  stroke(1);
  for(int i=0; i<500; i+=10){
    line(i,0,i,500);
    line(0,i,500,i);
  }
  float x=250;
  float y=50;
  circle(x,y,5);
  y-=-13.34272523 ; x+=18.36468577;
  circle(x,y,2);
  y-=-49.6786897  ;x+=-3.473872392;
  circle(x,y,2);
  y-=-55.54356382 ;x+= 24.7295879;
  circle(x,y,2);
  y-=-17.16107775 ; x+=-11.5752931;
  circle(x,y,2);
  y-=2.811296639  ;x+=-20.00341499;
  circle(x,y,2);
  y-=-18.88782168 ; x+=-6.874604881;
  circle(x,y,2);
  y-=5.407797402  ;x+=-16.64348904;
  circle(x,y,2);
  stroke(5);
  line(250,50,x,y);
  println("xdist: "+(x-250)+" ydist: "+(y-50));
  println("dist: "+sqrt(pow(x-250,2)+pow(y-50,2)));
  println("angle: "+theta(x-250,y-50));
}

float theta(float x, float y){
    return X-x>=0?atan((Y-y)/(X-x))+PI:atan((Y-y)/(X-x));
}
