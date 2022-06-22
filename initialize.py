import subprocess
from Code.data_process import load_dataset, make_text_list
import json

def save_database(path, files, db):
    with open(f'{path}/{db}_db.json', 'w') as f:
        json.dump(files, f, indent=4)

def run():
    #  pyuic5 -x visual\window.ui -o visual\win.py
    print('Generando archivos necesarios.\n')
    
    print('Cargando Base de Datos Vaswani')
    datasets_vas = make_text_list(load_dataset('vaswani'))
    save_database('.', datasets_vas, 'vaswani')
    print('Base de Datos Vaswani guardada.\n')
    
    print('Cargando Base de Datos Cranfield')
    datasets_cra = make_text_list(load_dataset('cranfield'))
    save_database('.', datasets_cra, 'cranfield')
    print('Base de Datos Cranfield guardada.\n')
    
    subprocess.run(['pyuic5', '-x', 'Code\\visual\\window.ui', '-o', 'Code\\visual\\win.py',], capture_output=True, timeout=100) 
    # subprocess.run(['pyuic5', '-x', 'Code\\visual\\waiting_win.ui', '-o', 'Code\\visual\\wait_win.py',], capture_output=True, timeout=100) 
    print('Visual Listo.')

if __name__ == "__main__":
    run()