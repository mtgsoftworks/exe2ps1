# exe2ps1
A small script that converts any .exe file you want to poweshell script (.ps1) file.

Run the Python file and enter the path to the .exe file. This will save the encrypted base64 data to the output_base64.txt file.

It will then take the contents of the output_base64.txt file and generate the JavaScript code using the convert_exe_to_ps1 function.

The generated JavaScript code is saved in the output_script.ps1 file.

You can now run the Powershell code using the generated output_script.ps1 file. But keep in mind that this code uses ActiveX objects and you need to be careful about security. Therefore, you should only use this code to run .exe files from trusted and well-known sources.

After the process is complete, the temporary generated output_base64.txt file will be deleted.
