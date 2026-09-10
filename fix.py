with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace(r'<div class="text-4xl font-extrabold text-blue-500">? </div>', r'<div class="text-4xl font-extrabold text-blue-500">? ${data.standard.price}</div>')
text = text.replace(r'<div class="text-4xl font-extrabold text-blue-500">? </div>', r'<div class="text-4xl font-extrabold text-blue-500">? ${data.standard.price}</div>')

text = text.replace(r'<div class="text-4xl font-extrabold text-blue-600">? </div>', r'<div class="text-4xl font-extrabold text-blue-600">? ${data.premium.price}</div>')
text = text.replace(r'<div class="text-4xl font-extrabold text-blue-600">? </div>', r'<div class="text-4xl font-extrabold text-blue-600">? ${data.premium.price}</div>')

text = text.replace(r'<div class="text-blue-600 font-bold mb-4">? </div>', r'<div class="text-blue-600 font-bold mb-4">? ${pkg.price}</div>')
text = text.replace(r'<div class="text-blue-600 font-bold mb-4">? </div>', r'<div class="text-blue-600 font-bold mb-4">? ${pkg.price}</div>')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(text)
