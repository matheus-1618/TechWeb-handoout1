import json
import database

def extract_route(string):
    first = string.find("/")
    end = string.find("HTTP")
    return string[first+1:end-1]

def read_file(path):
    with open(path,"r+b") as file:
        try:
            return file.read()
        except Exception as erro:
            print(erro)

def load_data(db):
    notes = db.get_all()
    #print(notes)
    # with open(f"data/{name}",'r') as file:
    #     out = json.load(file)
    # return out
    return notes

def load_template(template):
     with open(f"templates/{template}",'r') as file:
         return file.read()

def salvar_dados(db,file):
    # in_file = load_data(nomedojson)
    # in_file.append(file)
    # with open("data/notes.json", "w", encoding="utf-8") as dados:
    #     salvando = json.dump(in_file, dados, indent=2, separators=(",", ": "), sort_keys=True)
    db.add(database.Note(content=file["detalhes"], title=file["titulo"]))

def build_response(body='', code=200, reason='OK', headers=''):
    if headers != "":
        return f'HTTP/1.1 {code} {reason}\n{headers}\n\n{body}'.encode()
    return f'HTTP/1.1 {code} {reason}\n\n{body}'.encode()
        
