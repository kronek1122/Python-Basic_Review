import tkinter as tk

#Exercise 2
window = tk.Tk()
window.title('Adress Entry Form')

frm_form = tk.Frame(relief='sunken', borderwidth=2)
frm_form.pack()

lbl_first_name = tk.Label(master= frm_form, text = 'First Name:' )
ent_first_name = tk.Entry(master= frm_form, width=50)
lbl_first_name.grid(row=0, column=0, sticky='e')
ent_first_name.grid(row=0, column=1)

lbl_last_name = tk.Label(master= frm_form, text = 'Last Name:' )
ent_last_name = tk.Entry(master= frm_form, width=50)
lbl_last_name.grid(row=1, column=0, sticky='e')
ent_last_name.grid(row=1, column=1)

lbl_adress1 = tk.Label(master= frm_form, text = 'Adress Line 1:' )
ent_adress1 = tk.Entry(master= frm_form, width=50)
lbl_adress1.grid(row=2, column=0, sticky='e')
ent_adress1.grid(row=2, column=1)

lbl_adress2 = tk.Label(master= frm_form, text = 'Adress Line 2:' )
ent_adress2 = tk.Entry(master= frm_form, width=50)
lbl_adress2.grid(row=3, column=0, sticky='e')
ent_adress2.grid(row=3, column=1)

lbl_city = tk.Label(master= frm_form, text = 'City:' )
ent_city = tk.Entry(master= frm_form, width=50)
lbl_city.grid(row=4, column=0, sticky='e')
ent_city.grid(row=4, column=1)

lbl_state = tk.Label(master= frm_form, text = 'State/Province:' )
ent_state = tk.Entry(master= frm_form, width=50)
lbl_state.grid(row=5, column=0, sticky='e')
ent_state.grid(row=5, column=1)

lbl_postal_code = tk.Label(master= frm_form, text = 'Postal Code:' )
ent_postal_code = tk.Entry(master= frm_form, width=50)
lbl_postal_code.grid(row=6, column=0, sticky='e')
ent_postal_code.grid(row=6, column=1)

lbl_country = tk.Label(master= frm_form, text = 'Country:' )
ent_country = tk.Entry(master= frm_form, width=50)
lbl_country.grid(row=7, column=0, sticky='e')
ent_country.grid(row=7, column=1)

frm_button = tk.Frame()
frm_button.pack(fill=tk.X, ipadx=5, ipady=5)

btn_clear = tk.Button(master= frm_button, text = 'Clear')
btn_submit = tk.Button(master= frm_button, text = 'Submit')
btn_submit.pack(side = tk.RIGHT, padx=5, ipadx=5)
btn_clear.pack(side = tk.RIGHT, padx=5, ipadx=5)

window.mainloop()
