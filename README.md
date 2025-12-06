# 🔒 VulnLogin Lab - Laboratorio de Hacking Ético

![Hacking Ético](https://img.shields.io/badge/Hacking-Ético-green)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Flask](https://img.shields.io/badge/Flask-2.0+-lightgrey)
![License](https://img.shields.io/badge/License-Educational-yellow)

## 📋 Descripción del Proyecto

**VulnLogin Lab** es un laboratorio educativo de ciberseguridad que simula vulnerabilidades comunes en sistemas de autenticación web. Este proyecto fue diseñado específicamente para **fines educativos** y demostraciones académicas de hacking ético.

> ⚠️ **ADVERTENCIA**: Esta aplicación contiene vulnerabilidades **INTENCIONALES**. NUNCA debe usarse en producción ni para atacar sistemas reales sin autorización.

## 🎯 Objetivo

Demostrar las vulnerabilidades más comunes en aplicaciones web siguiendo el **OWASP Top 10**, y enseñar cómo explotarlas éticamente y cómo prevenirlas mediante código seguro.

## 🚀 Instalación Rápida

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git (opcional)

### Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/Reyes-30/Hacking-tico.git
cd Hacking-tico

# 2. Instalar dependencias
pip install flask requests

# 3. Ejecutar la aplicación vulnerable
python app_vulnerable.py

# 4. Abrir en navegador
# http://localhost:5000
```

### Inicio Rápido con Script (Windows)
```powershell
.\inicio.ps1
```

## 🎭 Vulnerabilidades Implementadas

### 1. 🔴 SQL Injection (Crítica)
- **Ubicación**: Formulario de login
- **Exploit**: `' OR '1'='1' --`
- **Impacto**: Bypass completo de autenticación
- **Script**: `exploits/1_sql_injection.py`

### 2. 🟠 Brute Force Attack (Alta)
- **Ubicación**: Endpoint de login
- **Exploit**: Ataque de diccionario
- **Impacto**: Descubrimiento de credenciales débiles
- **Script**: `exploits/2_brute_force.py`

### 3. 🟡 Session Hijacking (Alta)
- **Ubicación**: Cookies de sesión
- **Exploit**: Robo de cookies
- **Impacto**: Acceso no autorizado a cuentas
- **Script**: `exploits/3_session_hijack.py`

### 4. 🟢 Information Disclosure (Media)
- **Ubicación**: Mensajes de error y endpoints
- **Exploit**: Enumeración de usuarios
- **Impacto**: Filtración de información sensible
- **Script**: `exploits/4_info_disclosure.py`

### 5. 🔵 Weak Password Policy (Media)
- **Ubicación**: Registro de usuarios
- **Exploit**: Contraseñas débiles permitidas
- **Impacto**: Cuentas fácilmente comprometibles

## 📂 Estructura del Proyecto

```
Hacking-tico/
├── app_vulnerable.py          # Aplicación con vulnerabilidades
├── app_secure.py              # Versión segura (comparación)
├── exploits/                  # Scripts de explotación
│   ├── 1_sql_injection.py
│   ├── 2_brute_force.py
│   ├── 3_session_hijack.py
│   ├── 4_info_disclosure.py
│   └── README.md
├── templates/                 # Templates HTML
│   ├── login.html
│   ├── dashboard.html
│   └── register.html
├── static/                    # CSS y recursos
│   └── style.css
├── inicio.ps1                 # Script de inicio rápido
├── .gitignore
└── README.md
```

## 🎓 Uso Educativo

### Para Demostraciones en Vivo

#### Opción 1: Exploits Manuales
```bash
# Iniciar aplicación
python app_vulnerable.py

# En navegador:
# - Usuario: ' OR '1'='1' --
# - Password: cualquiercosa
```

#### Opción 2: Scripts Automatizados
```bash
# Terminal 1: Ejecutar servidor
python app_vulnerable.py

# Terminal 2: Ejecutar exploits
python exploits/1_sql_injection.py
python exploits/2_brute_force.py
python exploits/3_session_hijack.py
python exploits/4_info_disclosure.py
```

### Comparación con Versión Segura
```bash
# Puerto 5000: Versión vulnerable
python app_vulnerable.py

# Puerto 5001: Versión segura
python app_secure.py
```

## 👤 Credenciales de Prueba

### Aplicación Vulnerable
```
admin:123456          (Administrador)
usuario1:password     (Usuario normal)
jose:qwerty          (Usuario normal)
maria:12345          (Usuario normal)
```

### Aplicación Segura
```
admin:Admin123!       (Contraseña fuerte requerida)
usuario1:Password123! (Contraseña fuerte requerida)
```

## 🛡️ Protecciones Implementadas (Versión Segura)

- ✅ **Prepared Statements**: Previene SQL Injection
- ✅ **Rate Limiting**: 5 intentos por minuto
- ✅ **Contraseñas Hasheadas**: SHA-256 con salt
- ✅ **Política de Contraseñas Fuertes**: 8+ caracteres, mayúsculas, números, especiales
- ✅ **Cookies Seguras**: HttpOnly, Secure, SameSite
- ✅ **Mensajes Genéricos**: No revela información
- ✅ **Autenticación en Endpoints**: Decorators de protección
- ✅ **Autorización por Roles**: RBAC implementado

## 📊 Comparación: Vulnerable vs Seguro

| Aspecto | ❌ Vulnerable | ✅ Seguro |
|---------|--------------|-----------|
| SQL Queries | Concatenación directa | Prepared statements |
| Rate Limiting | Sin límites | 5 intentos/5 min |
| Contraseñas | Texto plano | Hash SHA-256 + salt |
| Cookies | Sin flags | HttpOnly, Secure, SameSite |
| Mensajes Error | Verbosos | Genéricos |
| Endpoints | Sin protección | Autenticación requerida |

## ⚖️ Aspectos Legales y Éticos

### ⚠️ IMPORTANTE - LEE ESTO PRIMERO

Este proyecto es **EXCLUSIVAMENTE** para fines educativos.

#### ✅ USO PERMITIDO:
- Aprendizaje personal en tu propio sistema
- Demostraciones académicas
- Entornos de prueba controlados
- Pentesting autorizado

#### ❌ USO PROHIBIDO:
- Atacar sistemas sin autorización
- Uso en producción
- Beneficio personal ilícito
- Cualquier actividad ilegal

**El hacking no autorizado es ILEGAL** y puede resultar en:
- Cargos criminales
- Multas significativas
- Tiempo en prisión
- Antecedentes penales

### Código de Conducta
Al usar este proyecto, te comprometes a:
1. Usar el conocimiento adquirido de forma ética
2. No atacar sistemas sin autorización explícita
3. Reportar vulnerabilidades de forma responsable
4. Respetar la privacidad y seguridad de otros

## 📚 Recursos de Aprendizaje

### Documentación
- [OWASP Top 10](https://owasp.org/Top10/)
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [PortSwigger Web Security Academy](https://portswigger.net/web-security)

### Plataformas de Práctica
- [HackTheBox](https://www.hackthebox.com/)
- [TryHackMe](https://tryhackme.com/)
- [DVWA - Damn Vulnerable Web App](http://www.dvwa.co.uk/)
- [WebGoat (OWASP)](https://owasp.org/www-project-webgoat/)

### Certificaciones
- CEH (Certified Ethical Hacker)
- OSCP (Offensive Security Certified Professional)
- CompTIA Security+
- GIAC GPEN

### Herramientas Profesionales
- Burp Suite
- OWASP ZAP
- Metasploit
- Nmap
- Wireshark

## 🤝 Contribuciones

Las contribuciones son bienvenidas siempre que mantengan el propósito educativo del proyecto.

### Cómo Contribuir
1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add: AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está destinado únicamente para **uso educativo**. No se otorga ninguna garantía.

## 👨‍💻 Autor

**Josué Reyes**
- GitHub: [@Reyes-30](https://github.com/Reyes-30)
- Proyecto: [Hacking-tico](https://github.com/Reyes-30/Hacking-tico)

## 🙏 Agradecimientos

- OWASP por sus recursos educativos
- Comunidad de seguridad informática
- Todos los que contribuyen a la educación en ciberseguridad

## 📞 Contacto y Soporte

Si tienes preguntas sobre el uso educativo de este proyecto:
- Abre un [Issue](https://github.com/Reyes-30/Hacking-tico/issues)
- Consulta la documentación en la carpeta `docs/`

---

## ⭐ Si te fue útil

Si este proyecto te ayudó a aprender sobre seguridad web, considera:
- ⭐ Darle una estrella al repositorio
- 🔄 Compartirlo con otros estudiantes
- 📝 Contribuir con mejoras

---

**Creado con fines educativos - Diciembre 2025**

```
╔═══════════════════════════════════════════════════════════╗
║  "El mejor hacker es aquel que usa su conocimiento        ║
║   para construir y proteger, no para destruir."           ║
╚═══════════════════════════════════════════════════════════╝
```

**Recuerda**: Con gran poder viene gran responsabilidad. Usa este conocimiento éticamente.
