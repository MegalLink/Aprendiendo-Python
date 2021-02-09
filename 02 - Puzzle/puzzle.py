import random
import tkinter as tk
from PIL import Image, ImageTk
class Application(tk.Frame):

    def __init__(self, image, ncortes,dimension_tablero):
        tk.Frame.__init__(self)
        self.grid()
        self.ncortes = ncortes 
        self.cargar_imagen(image,dimension_tablero)
        self.crear_widgets()
        self.crear_eventos()
        self.crear_tablero()
        self.mostrar_random()

    def cargar_imagen(self, image,dimension_tablero):
        image = Image.open(image)
        dim_tablero = dimension_tablero
        image = image.resize((dim_tablero, dim_tablero), Image.ANTIALIAS)
        self.image = image
        self.dim_tablero = dim_tablero
        self.dim_pieza= self.dim_tablero / self.ncortes

    def crear_widgets(self):
        self.canvas = tk.Canvas(self, width=self.dim_tablero, height=self.dim_tablero)
        self.canvas.grid()

    def crear_eventos(self):
        self.canvas.bind_all('<KeyPress-Up>', self.slide)
        self.canvas.bind_all('<KeyPress-Down>', self.slide)
        self.canvas.bind_all('<KeyPress-Left>', self.slide)
        self.canvas.bind_all('<KeyPress-Right>', self.slide)

    def slide(self, event):
        piezas = self.piezas_alrededor()
        if event.keysym in ('Up') and piezas['abajo']:
            self._mover(piezas['abajo'], piezas['centro'], 
                        (0, -self.dim_pieza))
        if event.keysym in ('Down') and piezas['arriba']:
            self._mover(piezas['arriba'], piezas['centro'],
                        (0, self.dim_pieza))
        if event.keysym in ('Left') and piezas['derecha']:
            self._mover(piezas['derecha'], piezas['centro'],
                        (-self.dim_pieza, 0))
        if event.keysym in ('Right') and piezas['inzquierda']:
            self._mover(piezas['inzquierda'], piezas['centro'],
                        (self.dim_pieza, 0))
        

    def _mover(self, desde, hasta, coord):
        self.canvas.move(desde['id'], *coord)
        hasta['pos_a'], desde['pos_a'] = desde['pos_a'], hasta['pos_a']
        

    def piezas_alrededor(self):
        piezas = {'centro': None,
                  'derecha' : None,
                  'inzquierda'  : None,
                  'arriba'   : None,
                  'abajo': None}
        for pieza in self.board:
            if not pieza['visible']:
                piezas['centro'] = pieza
                break
        x0, y0 = piezas['centro']['pos_a']
        for pieza in self.board:
            x1, y1 = pieza['pos_a']
            if y0 == y1 and x1 == x0 + 1:
                piezas['derecha'] = pieza
            if y0 == y1 and x1 == x0 - 1:
                piezas['inzquierda'] = pieza
            if x0 == x1 and y1 == y0 - 1:
                piezas['arriba'] = pieza
            if x0 == x1 and y1 == y0 + 1:
                piezas['abajo'] = pieza
        return piezas

    def crear_tablero(self):
        self.board = []
        for x in range(self.ncortes):
            for y in range(self.ncortes):
                x0 = x * self.dim_pieza
                y0 = y * self.dim_pieza
                x1 = x0 + self.dim_pieza
                y1 = y0 + self.dim_pieza
                image = ImageTk.PhotoImage(
                        self.image.crop((x0, y0, x1, y1)))
                pieza = {'id'     : None,
                         'image'  : image,
                         'pos_o'  : (x, y),
                         'pos_a'  : None,
                         'visible': True}
                self.board.append(pieza)
        self.board[-1]['visible'] = False
      
    def mostrar_random(self):
        random.shuffle(self.board)
        index = 0
        for x in range(self.ncortes):
            for y in range(self.ncortes):
                self.board[index]['pos_a'] = (x, y)
                if self.board[index]['visible']:
                    x1 = x * self.dim_pieza
                    y1 = y * self.dim_pieza
                    image = self.board[index]['image']
                    id = self.canvas.create_image(
                            x1, y1, image=image, anchor=tk.NW)
                    self.board[index]['id'] = id
                index += 1

if __name__ == '__main__':
    app = Application('dota2.jpg',4,600)
    app.master.title('Puzzle')
    app.mainloop()




