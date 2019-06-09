def setup():
    size(520,525)
    textSize(160)
    textAlign(CENTER)
    frameRate(50)
def draw():
    fill(120,90,79,100)
    #print(mouseX,mouseY)
    #print(hex(get(mouseX,mouseY)))
    print(LEFT)
    if keyPressed:
        print(keyCode)
        if key == 'b':
            text("B",width/2+80, (height/3)*2)
        if key =='a':
            text("A",width/2-80, (height/3)*2)
        
    s = createShape()
    s.beginShape()
    s.fill(5, 10, 60, 9)
    s.noStroke()
    s.vertex(50, (height/4)*3)
    s.vertex(width/2+30, (height/4)*3+50)
    s.vertex(width/2, (height/4)*3)
    s.vertex(width/2+40, (height/4)*3-30)
    s.vertex(width-90, (height/4)*3)
    s.endShape(CLOSE)
    shape(s, 25, 25)
