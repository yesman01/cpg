import random
import webbrowser
a = random.randint(0,255)
print(a)
b = a-25
fi = open("htmlwithcodes.html", "w")
for x in range(100):
                f = []
                r=random.randint(a-50,a)
                g=random.randint(a-50,a)
                b=random.randint(a-50,a)
                f=[r,",",g,",",b]
                #print(*f)
                htmlcolr='#{:02x}{:02x}{:02x}'.format(r, g, b)
                #print(htmlcolr)
                fi.write('<div style="background-color: '+htmlcolr+' ; padding: 10px;">'+htmlcolr+'</div>')
fi.close()
print("Done!")
webbrowser.open_new_tab("file:///media/fuse/crostini_8fd3d75864759ce0ee50af5e5abb02fd8a2a0e9b_termina_penguin/cpg/htmlwithcodes.html")
