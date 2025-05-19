@echo off
SETLOCAL EnableDelayedExpansion

REM URL del instalador oficial Python 3.11.4 (64-bit)
set "PYTHON_INSTALLER=python-3.11.4-amd64.exe"
set "PYTHON_URL=https://www.python.org/ftp/python/3.11.4/%PYTHON_INSTALLER%"

echo Verificando instalación de Python...

where python >nul 2>nul
IF %ERRORLEVEL% EQU 0 (
    echo Python ya está instalado.
    goto InstallDeps
) ELSE (
    echo Python no está instalado. Se procederá a descargar e instalar.
)

REM Descargar instalador si no existe
if not exist "%PYTHON_INSTALLER%" (
    echo Descargando instalador de Python...
    powershell -Command "Invoke-WebRequest -Uri '%PYTHON_URL%' -OutFile '%PYTHON_INSTALLER%'"
    IF %ERRORLEVEL% NEQ 0 (
        echo [ERROR] No se pudo descargar el instalador de Python.
        pause
        exit /b 1
    )
) ELSE (
    echo Instalador ya descargado.
)

REM Ejecutar instalador en modo silencioso
echo Ejecutando instalador de Python en modo silencioso...
"%CD%\%PYTHON_INSTALLER%" /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] La instalación de Python falló. Asegúrate de ejecutar este script con permisos de administrador.
    pause
    exit /b 1
)

echo Instalación completada.

REM Verificar de nuevo python
where python >nul 2>nul
IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Python sigue sin estar disponible en el PATH tras la instalación.
    echo Intenta reiniciar la consola o añadir Python manualmente al PATH.
    pause
    exit /b 1
)

:InstallDeps

echo.
echo Verificando instalación de pip...

python -m pip --version >nul 2>nul
IF %ERRORLEVEL% NEQ 0 (
    echo pip no encontrado. Intentando instalar pip...
    python -m ensurepip --default-pip
    IF %ERRORLEVEL% NEQ 0 (
        echo [ERROR] No se pudo instalar pip automáticamente.
        echo Por favor, instala pip manualmente e intenta de nuevo.
        pause
        exit /b 1
    )
) ELSE (
    echo pip está instalado.
)

echo.
echo Actualizando pip a la última versión...
python -m pip install --upgrade pip
IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] No se pudo actualizar pip.
    pause
    exit /b 1
)

echo.
echo === Creando entorno virtual ===
python -m venv venv

IF NOT EXIST venv (
    echo [ERROR] No se pudo crear el entorno virtual.
    pause
    exit /b 1
)

echo.
echo === Activando entorno virtual ===
CALL venv\Scripts\activate.bat

echo.
echo Instalando dependencias desde requirements.txt...
python -m pip install -r requirements.txt

IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Falló la instalación de paquetes.
    pause
    exit /b 1
)

echo.
echo ✅ Todo listo. El entorno está preparado.
echo Para activarlo manualmente en el futuro, ejecuta:
echo     venv\Scripts\activate.bat
echo.

pause
ENDLOCAL