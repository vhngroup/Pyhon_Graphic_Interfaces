import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora Mejorada")
        self.geometry("400x600")
        self.config(bg='#2c3e50')

        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Entry(self, font=("Arial", 30), justify="right", bd=2, relief="solid")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=15, sticky="nsew")

        buttons = [
            '7','8','9','/',
            '4','5','6','*',
            '1','2','3','-',
            '0','C','=','+',
        ]

        row_val=1
        col_val=0

        for button_text in buttons:
            button = tk.Button(self, text=button_text, font=('Arial', 24), width=5, height=5, bg='#2980B9', fg='FFFFFF',
                               activebackground='#3498DB', activeforeground='#FFFFFF', command=lambda txt=button_text: self.on_button_click(txt)
                               )
            button.grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
            col_val +=1
            if col_val>3:
                col_val =0
                row_val +=1
        
        #Ajustamos el tamaño de los botonos, de acuerdo al tañano de la ventana
        for i in range(4):
            self.grid_columnconfigure(i,weight=1)
        for i in range(1,5):
            self.grid_rowconfigure(i, weight=1)
    
    def on_button_click(self, char):
        if char == 'C':
            self.display.delete(0, tk.END)
        elif char == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END )
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        else:
            current_text = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, current_text + char)
if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
    