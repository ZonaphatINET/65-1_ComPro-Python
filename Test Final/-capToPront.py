def capToPront (s):
    s = str(s)
    a=[]
    b=[]
    for i in range(len(s)):
        if i == s.isupper():
            i += a
        else :
            i += b
    return (a + b)

print(capToPront("hApPy"))
print(capToPront("moveMENT"))
print(capToPront("shOrtCAKE"))

'''
function capToFront(s) {
    var sp = s.split("");
    var caps = []; 
    var lower = []
    for (var i = 0; i < sp.length; i++)
        {
            if (sp[i] == sp[i].toUpperCase()){              
                caps.push(sp[i]);
           **//How can i remove the capital letter in "sp" array as I've pushed them into the caps Array**

            }
            if (sp[i] == sp[i].toLowerCase()){
                lower.push(sp[i]);
            }
        }
    return caps.join("").concat(lower.join(""));
}
'''