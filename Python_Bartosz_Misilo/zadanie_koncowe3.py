def change(text:str):
    newText = text.replace("a","!");
    newText = newText.replace("A","!");
    return newText
print(change(input("Wprowadz wyraz")));