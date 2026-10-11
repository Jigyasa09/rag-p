import os

def load_document(folder):
    result = {}
    for filename in os.listdir(folder):
        path = os.path.join(folder,filename)
        with open(path, "r", encoding="utf-8") as f:
            result[filename] = f.read()
    
    return result

if __name__ == "__main__":
    documents = load_document("docs")
    for name, text in documents.items():
        print(name, len(text))
    

