$syspython="python.exe"
$ve="$HOME\.virtualenvs\colorultra"

remove-item -r -fo * -I build,dist,MANIFEST,colorultra.egg-info,$ve,sandbox
& $syspython -Bc "import pathlib, shutil; [shutil.rmtree(p) for p in pathlib.Path('.').rglob('__pycache__')]"

