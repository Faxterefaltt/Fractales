class TrianguloSierpinsky:
    def __init__(self, puntos, color):
        self.puntos = puntos
        self.color = color

    def obtener_medio(self, p1, p2):
        return ((p1[0]+p2[0]) / 2, (p1[1]+p2[1]) / 2)

    def dibujar(self, canvas, prof):
        if prof > 0:
            s1 = TrianguloSierpinsky([self.puntos[0],
                                      self.obtener_medio(self.puntos[0], self.puntos[1]),
                                      self.obtener_medio(self.puntos[0], self.puntos[2])], self.color)
            s1.dibujar(canvas, prof-1)

            s2 = TrianguloSierpinsky([self.puntos[1],
                                      self.obtener_medio(self.puntos[0], self.puntos[1]),
                                      self.obtener_medio(self.puntos[1], self.puntos[2])], self.color)
            s2.dibujar(canvas, prof-1)

            s3 = TrianguloSierpinsky([self.puntos[2],
                                      self.obtener_medio(self.puntos[2], self.puntos[1]),
                                      self.obtener_medio(self.puntos[0], self.puntos[2])], self.color)
            s3.dibujar(canvas, prof-1)

            #no hay nada cuando prof > 0
        else:
            canvas.create_polygon(self.puntos, fill=self.color)