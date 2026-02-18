$ve="$HOME\.virtualenvs\colorultra"
$bin="$ve\Scripts"

# Upload to PyPI.
& $bin\twine.exe upload dist\colorultra-*.tar.gz dist\colorultra-*.whl
