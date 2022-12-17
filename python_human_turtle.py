import turtle

# Kaplumbağa nesnesi oluştur
t = turtle.Turtle()

# Baş çiz
t.penup()
t.goto(0, 100)
t.pendown()
t.circle(20)

# Gözler çiz
t.penup()
t.goto(-10, 110)
t.pendown()
t.dot(5)

t.penup()
t.goto(10, 110)
t.pendown()
t.dot(5)

# Burun çiz
t.penup()
t.goto(0, 100)
t.pendown()
t.goto(0, 90)

# Ağız çiz
t.penup()
t.goto(-10, 80)
t.pendown()
t.goto(10, 80)

# Vücut çiz
t.penup()
t.goto(0, 60)
t.pendown()
t.goto(0, 0)

# Kol çiz
t.penup()
t.goto(-20, 40)
t.pendown()
t.goto(-60, 0)

t.penup()
t.goto(20, 40)
t.pendown()
t.goto(60, 0)

# Bacak çiz
t.penup()
t.goto(-30, 0)
t.pendown()
t.goto(-30, -60)

t.penup()
t.goto(30, 0)
t.pendown()
t.goto(30, -60)

# Çizimi tamamla
turtle.done()
