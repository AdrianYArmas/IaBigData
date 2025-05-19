@echo off
SETLOCAL

REM Cambiar consola a UTF-8 para mejor soporte de caracteres
chcp 65001 >nul

REM Activar entorno virtual si existe
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
) else (
    echo [WARNING] No se encontró entorno virtual 'venv'. Ejecutando con Python global.
)

REM Ejecutar app/api.py sin mostrar salida
start /b python app\api.py >nul 2>&1

REM Ejecutar Streamlit sin redirigir para que muestre sus logs
start /b streamlit run app.py

REM Mensajes informativos en azul y rojo con PowerShell
echo.

powershell -Command "Write-Host '===============================================' -ForegroundColor Blue"
powershell -Command "Write-Host 'Ambos scripts se están ejecutando en esta ventana.' -ForegroundColor Blue"
powershell -Command "Write-Host 'Puedes acceder a la app Streamlit en:' -ForegroundColor Blue"
powershell -Command "Write-Host '  http://localhost:8501' -ForegroundColor Blue"
powershell -Command "Write-Host 'Y la API Flask en:' -ForegroundColor Blue"
powershell -Command "Write-Host '  http://127.0.0.1:5000' -ForegroundColor Blue"
powershell -Command "Write-Host '===============================================' -ForegroundColor Blue"

echo.

powershell -Command "Write-Host 'Para detenerlos, simplemente cierra esta ventana.' -ForegroundColor Red"

REM No pause para no mostrar mensaje de "presione cualquier tecla..."

ENDLOCAL


