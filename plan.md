**Stack**

Shoes.rb

Bettertouch para llamar al script

**Core features**

Se abre con un shortcut 

La ventana se ajusta al tamaño de la foto y no tiene bordes

Se puede cerrar como cualquier otra ventana

Se abre "on top"

**Nice to haves**

Se puede redimensionar la ventana

Se cierra con un click en la imagen

**Pseudocódigo**

```ruby
Ventana do
   on_top true
   closable true

   on_open do
    if clipboard image
      load_image
    end
   end
end
```


