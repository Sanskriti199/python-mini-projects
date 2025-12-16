import tkinter as tk
from tkinter import ttk, messagebox

class UnitConverterApp:
    def __init__(self, master):
        self.master = master
        master.title("Multi-Unit Converter")
        master.resizable(False, False)

        self.conversion_type = tk.StringVar(master)
        self.input_value = tk.DoubleVar()
        self.result_text = tk.StringVar(master)
        self.result_text.set("Result: 0.00")

        self.conversion_options = {
            "Kilometers (km) to Meters (m)": ("km", "m"),
            "Kilograms (kg) to Grams (g)": ("kg", "g"),
            "Fahrenheit (F) to Celsius (C)": ("F", "C")
        }
        
        self.conversion_names = list(self.conversion_options.keys())
        self.conversion_type.set(self.conversion_names[0])
        self.conversion_type.trace_add("write", self.update_labels)

        main_frame = ttk.Frame(master, padding="20")
        main_frame.grid(row=0, column=0)

        ttk.Label(main_frame, text="Simple Unit Converter", font=('Helvetica', 12, 'bold')).grid(row=0, column=0, columnspan=3, pady=10)

        ttk.Label(main_frame, text="Select Conversion:").grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.type_menu = ttk.OptionMenu(main_frame, self.conversion_type, self.conversion_names[0], *self.conversion_names)
        self.type_menu.grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky='ew')

        self.input_label = ttk.Label(main_frame, text="Input (km):")
        self.input_label.grid(row=2, column=0, padx=5, pady=5, sticky='w')

        self.input_entry = ttk.Entry(main_frame, width=15, textvariable=self.input_value)
        self.input_entry.grid(row=2, column=1, padx=5, pady=5)
        self.input_entry.focus()

        convert_button = ttk.Button(main_frame, text="CONVERT", command=self.perform_conversion)
        convert_button.grid(row=3, column=0, columnspan=3, pady=15)

        self.result_label = ttk.Label(main_frame, textvariable=self.result_text, font=('Helvetica', 10, 'bold'))
        self.result_label.grid(row=4, column=0, columnspan=3, pady=5)

        self.input_entry.bind('<Return>', lambda event: self.perform_conversion())
        self.update_labels()

    def update_labels(self, *args):
        current_selection = self.conversion_type.get()
        unit_from, unit_to = self.conversion_options[current_selection]
        
        self.input_label.config(text=f"Input ({unit_from}):")
        self.result_text.set(f"Result: 0.00 {unit_to}")

    def perform_conversion(self):
        try:
            input_val = self.input_value.get()
            conversion = self.conversion_type.get()
            
            unit_from, unit_to = self.conversion_options[conversion]
            
            if conversion == "Kilometers (km) to Meters (m)":
                result = input_val * 1000
            
            elif conversion == "Kilograms (kg) to Grams (g)":
                result = input_val * 1000
                
            elif conversion == "Fahrenheit (F) to Celsius (C)":
                result = (input_val - 32) * 5/9
            
            self.result_text.set(f"Result: {result:.2f} {unit_to}")

        except tk.TclError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            self.input_value.set(0.0)
            self.result_text.set(f"Result: 0.00 {unit_to}")

if __name__ == "__main__":
    root = tk.Tk()
    app = UnitConverterApp(root)
    root.mainloop()