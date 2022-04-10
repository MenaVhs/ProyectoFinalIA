# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=[r'C:\Users\Pc\Documents\LANIA CALSES\CUATRI 2\01 INTELIGENCIA ARTIFICIAL 1\ia rata\ProyectoFinalIA\main.py'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

a.datas += [('icono.ico',r'C:\Users\Pc\Documents\LANIA CALSES\CUATRI 2\01 INTELIGENCIA ARTIFICIAL 1\ia rata\ProyectoFinalIA\icono.ico', "DATA"),
            ('scatter.png',r'C:\Users\Pc\Documents\LANIA CALSES\CUATRI 2\01 INTELIGENCIA ARTIFICIAL 1\ia rata\ProyectoFinalIA\scatter.png', "DATA"),
            ('Inter-Regular.ttf',r'C:\Users\Pc\Documents\LANIA CALSES\CUATRI 2\01 INTELIGENCIA ARTIFICIAL 1\ia rata\ProyectoFinalIA\Inter-Regular.ttf',"DATA")]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Rat Tracking',
          debug=False,
          strip=False,
          upx=True,
          console=False)