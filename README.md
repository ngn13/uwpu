# uwpu - useless windows privesc util
uwpu is a simple tool that you can use to
download actualy useful windows privesc tools
on the target.

## using uwpu.py
```
Usage: python3 uwpu.py <function>
```
You can use the `download` function to
download all the tools into `downloads`
folder, then you can use the `serve`
function to startup a python web server to 
serve all the downloaded files and download
them on your target.

This will only work if you can access
your machine on the target tho, like
in a CTF enviroment.

## using uwpu.exe
You can compile the uwpu using
```
make
```
this will create an executable file in
the `build` directory. Or you can download
the precompiled executable from the releases
tab.

Here is how you can use this executable:
```
Usage: uwpu.exe <tool-to-download>
```