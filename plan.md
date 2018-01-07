Script de python con PyQt que facilita transcribir manualmente el contenido de una imagen copiada en el clipboard.

Diseñada para integrarse en mi flujo de trabajo.

**Stack**

PyQT5

Script de python

Bettertouch para llamar al script

Automator como wrapper del script de python

**Core features**

Se abre con un shortcut 

La ventana se ajusta al tamaño de la foto y no tiene bordes

Se puede cerrar como cualquier otra ventana

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



