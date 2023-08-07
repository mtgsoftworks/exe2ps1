import base64
import os

def encode_exe_to_base64(input_file):
    try:
        with open(input_file, "rb") as file:
            exe_data = file.read()
            base64_encoded_data = base64.b64encode(exe_data).decode("utf-8")

        return base64_encoded_data
    except FileNotFoundError:
        print("Error: Input file not found.")
        return None
    except Exception as e:
        print("An error occurred:", str(e))
        return None

def convert_exe_to_ps1(base64_data):
    ps1_code = '''
$base64Data = '{}'
$exeBytes = [System.Convert]::FromBase64String($base64Data)
$exePath = Join-Path $PSScriptRoot "output.exe"
Set-Content -Path $exePath -Value $exeBytes -Encoding Byte
Start-Process -FilePath $exePath
    '''.format(base64_data)

    return ps1_code

if __name__ == "__main__":
    exefile = input("Enter file (.exe): ")

    base64_data = encode_exe_to_base64(exefile)

    if base64_data:
        ps1_code = convert_exe_to_ps1(base64_data)

        current_dir = os.getcwd()
        output_ps1_file = os.path.join(current_dir, "output_script.ps1")

        with open(output_ps1_file, "w") as file:
            file.write(ps1_code)

        print("Exe to Ps1 conversion successful. PowerShell script saved to:", output_ps1_file)
