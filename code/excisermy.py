import bubbles
p=bubbles.Pipeline()
p.source(bubbles.data_object('csv_source','infile\zoo.csv',infer_fields=True))
p.aggregate('animal','hush')
p.pretty_print()