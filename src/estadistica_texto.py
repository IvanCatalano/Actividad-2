def estadistica_texto() :
    text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""
    cant_lineas = len(text.split('.'))
    print(f'El numero total de lineas es de : {cant_lineas}')
    palabras = len(text.split())
    print(f'La cantidad total de palabras es de : {palabras}')
    print(f'El promedio de palabras por linea es de : {round(palabras / cant_lineas , 2)}')
    list = []
    for linea in text.split('.') :
        if  len(linea.split()) > palabras / cant_lineas :
            list.append( linea )
    print(f'Las lineas con mas palabras que el promedio son las siguientes : ')
    for linea in list :
        print(linea)
    
        
