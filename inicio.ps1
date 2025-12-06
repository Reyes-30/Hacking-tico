# INICIO RAPIDO - VulnLogin Lab

Write-Host "=============================================================" -ForegroundColor Cyan
Write-Host " VulnLogin Lab - Laboratorio de Hacking Etico" -ForegroundColor Cyan
Write-Host "=============================================================" -ForegroundColor Cyan
Write-Host ""

# Verificar Python
Write-Host "[1/4] Verificando Python..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "    OK: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "    ERROR: Python no esta instalado" -ForegroundColor Red
    Write-Host "    Descarga Python desde: https://www.python.org/downloads/" -ForegroundColor Yellow
    exit 1
}

# Instalar dependencias
Write-Host ""
Write-Host "[2/4] Instalando dependencias..." -ForegroundColor Yellow
Write-Host "    Instalando Flask y requests..." -ForegroundColor Gray
pip install flask requests -q
if ($LASTEXITCODE -eq 0) {
    Write-Host "    OK: Dependencias instaladas" -ForegroundColor Green
} else {
    Write-Host "    ADVERTENCIA: Error al instalar dependencias" -ForegroundColor Yellow
}

# Verificar estructura de archivos
Write-Host ""
Write-Host "[3/4] Verificando archivos del proyecto..." -ForegroundColor Yellow
$archivos_requeridos = @(
    "app_vulnerable.py",
    "app_secure.py",
    "README.md",
    "GUIA_EXPOSICION.md",
    "templates\login.html",
    "templates\dashboard.html",
    "templates\register.html",
    "static\style.css",
    "exploits\1_sql_injection.py",
    "exploits\2_brute_force.py",
    "exploits\3_session_hijack.py",
    "exploits\4_info_disclosure.py"
)

$archivos_ok = 0
foreach ($archivo in $archivos_requeridos) {
    if (Test-Path $archivo) {
        $archivos_ok++
    } else {
        Write-Host "    Falta: $archivo" -ForegroundColor Yellow
    }
}

Write-Host "    OK: $archivos_ok/$($archivos_requeridos.Count) archivos encontrados" -ForegroundColor Green

# Mostrar opciones
Write-Host ""
Write-Host "[4/4] Proyecto listo" -ForegroundColor Yellow
Write-Host "=============================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "OPCIONES DISPONIBLES:" -ForegroundColor Cyan
Write-Host ""
Write-Host "1 - Iniciar aplicacion VULNERABLE (puerto 5000)" -ForegroundColor Red
Write-Host "    python app_vulnerable.py" -ForegroundColor Gray
Write-Host ""
Write-Host "2 - Iniciar aplicacion SEGURA (puerto 5001)" -ForegroundColor Green
Write-Host "    python app_secure.py" -ForegroundColor Gray
Write-Host ""
Write-Host "3 - Ejecutar exploits (despues de iniciar app vulnerable)" -ForegroundColor Yellow
Write-Host "    python exploits\1_sql_injection.py" -ForegroundColor Gray
Write-Host "    python exploits\2_brute_force.py" -ForegroundColor Gray
Write-Host "    python exploits\3_session_hijack.py" -ForegroundColor Gray
Write-Host "    python exploits\4_info_disclosure.py" -ForegroundColor Gray
Write-Host ""
Write-Host "4 - Leer guia de exposicion" -ForegroundColor Cyan
Write-Host "    Abrir GUIA_EXPOSICION.md" -ForegroundColor Gray
Write-Host ""
Write-Host "=============================================================" -ForegroundColor Cyan
Write-Host ""

Write-Host ""
Write-Host "Que deseas hacer?" -ForegroundColor White
Write-Host "[1] Iniciar app VULNERABLE" -ForegroundColor Red
Write-Host "[2] Iniciar app SEGURA" -ForegroundColor Green
Write-Host "[3] Ver documentacion" -ForegroundColor Cyan
Write-Host "[4] Salir" -ForegroundColor Gray
Write-Host ""

$opcion = Read-Host "Selecciona una opcion (1-4)"

switch ($opcion) {
    "1" {
        Write-Host ""
        Write-Host "Iniciando aplicacion VULNERABLE..." -ForegroundColor Red
        Write-Host "ADVERTENCIA: Esta aplicacion contiene vulnerabilidades intencionales" -ForegroundColor Yellow
        Write-Host "URL: http://localhost:5000" -ForegroundColor Cyan
        Write-Host ""
        Write-Host "Presiona Ctrl+C para detener el servidor" -ForegroundColor Gray
        Write-Host ""
        Start-Sleep -Seconds 2
        python app_vulnerable.py
    }
    "2" {
        Write-Host ""
        Write-Host "Iniciando aplicacion SEGURA..." -ForegroundColor Green
        Write-Host "Esta version implementa todas las mejores practicas" -ForegroundColor Green
        Write-Host "URL: http://localhost:5001" -ForegroundColor Cyan
        Write-Host ""
        Write-Host "Presiona Ctrl+C para detener el servidor" -ForegroundColor Gray
        Write-Host ""
        Start-Sleep -Seconds 2
        python app_secure.py
    }
    "3" {
        Write-Host ""
        Write-Host "Abriendo documentacion..." -ForegroundColor Cyan
        Start-Process "GUIA_EXPOSICION.md"
        Start-Process "README.md"
        Write-Host "Documentos abiertos" -ForegroundColor Green
    }
    "4" {
        Write-Host ""
        Write-Host "Hasta luego!" -ForegroundColor Cyan
        exit 0
    }
    default {
        Write-Host ""
        Write-Host "Opcion invalida" -ForegroundColor Red
        Write-Host "Ejecuta nuevamente el script: .\inicio.ps1" -ForegroundColor Yellow
    }
}
