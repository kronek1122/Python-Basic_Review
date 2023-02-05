import tkinter as tk
from tkinter.filedialog import asksaveasfilename
import random


def save_file():
    filepath = asksaveasfilename(
        defaultextension='txt',
        filetypes=[('Text Files','*.txt'),('All Files',"*.*")]
    )
    if not filepath:
        return
    
    with open(filepath,'w') as output_file:
        output_file.writelines(lbl_poem['text'])

def generate_poem():

    noun = ent_nouns.get().split(',')
    verb = ent_verbs.get().split(',')
    adjective = ent_adjectives.get().split(',')
    adverb = ent_adverbs.get().split(',')
    preposition = ent_prepositions.get().split(',')

    if (
        len(noun) < 3
        or len(verb) < 3
        or len(adjective) < 3
        or len(preposition) < 2
        or len(adverb) < 1
    ):
        lbl_poem['text'] = (
            "There was a problem with your input!\n"
            "Enter at least three nouns, three verbs, three adjectives, "
            "two prepositions and an adverb!"
        )
        return

    noun1 = random.choice(noun)
    noun.remove(noun1)
    noun2 = random.choice(noun)
    noun.remove(noun2)
    noun3 = random.choice(noun)

    verb1 = random.choice(verb)
    verb.remove(verb1)
    verb2 = random.choice(verb)
    verb.remove(verb2)
    verb3 = random.choice(verb)


    adj1 = random.choice(adjective)
    adjective.remove(adj1)
    adj2 = random.choice(adjective)
    adjective.remove(adj2)
    adj3 = random.choice(adjective)


    prep1 = random.choice(preposition)
    preposition.remove(prep1)
    prep2 = random.choice(preposition)

    adverb1 = random.choice(adverb)

    if adj1[0] in 'aeiou':
        A = 'An'
    else:
        A = 'A'

    poem = f'{A} {adj1} {noun1}\n\n'
    poem = poem + f'A {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}\n'
    poem = poem + f'{adverb1}, the {noun1} {verb2}\n'
    poem = poem + f' the {noun2} {verb3} {prep2} a {adj3} {noun3}'

    lbl_poem['text'] = poem

window = tk.Tk()
window.title('Make your own poem!')

frm_enter = tk.Frame(window)
lbl_instruction = tk.Label(frm_enter, text = 'Enter your favorite words, separated by commas.')
lbl_nouns = tk.Label(frm_enter, text = 'Nouns:')
lbl_verbs = tk.Label(frm_enter, text = 'Verbs:')
lbl_adjectives = tk.Label(frm_enter, text = 'Adjectives:')
lbl_prepositions = tk.Label(frm_enter, text = 'Prepositions:')
lbl_adverbs = tk.Label(frm_enter, text = 'Adverbs:')

ent_nouns = tk.Entry(frm_enter)
ent_verbs = tk.Entry(frm_enter)
ent_adjectives = tk.Entry(frm_enter)
ent_prepositions = tk.Entry(frm_enter)
ent_adverbs = tk.Entry(frm_enter)

btn_generate = tk.Button(text = 'Generate', command=generate_poem)

lbl_instruction.grid(row=0, column =1)

lbl_nouns.grid(row=1, column = 0, sticky='e')
lbl_verbs.grid(row=2, column = 0, sticky='e')
lbl_adjectives.grid(row=3, column = 0, sticky='e')
lbl_prepositions.grid(row=4, column = 0, sticky='e')
lbl_adverbs.grid(row=5, column = 0, sticky='e')

ent_nouns.grid(row=1, column = 1, sticky='we')
ent_verbs.grid(row=2, column = 1, sticky='we')
ent_adjectives.grid(row=3, column = 1, sticky='we')
ent_prepositions.grid(row=4, column = 1, sticky='we')
ent_adverbs.grid(row=5, column = 1, sticky='we')

frm_enter.pack(pady=10)

btn_generate.pack()

frm_poem = tk.Frame(window, relief='groove', borderwidth=5,)

lbl_title = tk.Label(frm_poem, text = 'Your poem:')
lbl_title.pack(pady=10)

lbl_poem = tk.Label(frm_poem, text = 'Press "Generate" button to dispaly poem')
lbl_poem.pack(padx=5)

btn_save = tk.Button(frm_poem, text = 'Save file', command=save_file)
btn_save.pack(pady=10)
frm_poem.pack(fill=tk.X, padx=5, pady = 5)

window.mainloop()
