@echo off
title Contador de numeros telefonicos

echo.
echo ================================================
echo       CONTADOR DE NUMEROS TELEFONICOS
echo ================================================
echo.

if "%~1"=="" (
    echo Arraste um arquivo XML para cima deste arquivo .BAT.
    echo.
    pause
    exit /b
)

where py >nul 2>&1
if %errorlevel%==0 (
    py "%~dp0contar_numeros.py" "%~1"
    exit /b
)

where python >nul 2>&1
if %errorlevel%==0 (
    python "%~dp0contar_numeros.py" "%~1"
    exit /b
)

echo ERRO: Python nao foi encontrado neste computador.
echo Instale o Python e tente novamente.
echo.
pause
