import subprocess

def run():
    #  pyuic5 -x visual\window.ui -o visual\win.py
    print('Generando archivos necesarios.')
    subprocess.run(['pyuic5', '-x', 'Code\\visual\\window.ui', '-o', 'Code\\visual\\win.py',], capture_output=True, timeout=100) 
    print('Visual Listo.')

if __name__ == "__main__":
    run()