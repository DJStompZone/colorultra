$syspython="python.exe"
$ve="$HOME\.virtualenvs\colorultra"
$bin="$ve\Scripts"

# Upload to the test PyPI.
& $bin\twine.exe upload --repository testpypi dist\colorultra-*
if(!$?) {
    write-host "  > Expect a 400 if package was already uploaded"
}

# cd elsewhere so we cannot import from local source.
mkdir -force sandbox | out-null
cd sandbox

# Create a temporary disposable virtualenv.
& $syspython -m venv --clear venv

# TODO: What is the windows/powershell equivalent of this:
#    version=$(grep __version__ colorultra/__init__.py | cut -d' ' -f3 | tr -d "'")

# Install the package we just uploaded.
# (--extra-index-url for this project's requirements)
venv\Scripts\python -m pip --quiet install --index-url https://test.pypi.org/simple --extra-index-url https://pypi.org/simple colorultra==$version
# Import and use colorultra from the temp virtualenv.
venv\Scripts\python.exe -c @"
import colorultra;
colorultra.init();
print(colorultra.Fore.GREEN + ""OK Colorama "" + colorultra.__version__ + "" from test pypi install."")
"@

cd ..
