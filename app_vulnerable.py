"""
VulnLogin Lab - Aplicación Vulnerable para Hacking Ético
⚠️ SOLO PARA FINES EDUCATIVOS - NO USAR EN PRODUCCIÓN
"""

from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import hashlib
import os

app = Flask(__name__)
app.secret_key = 'clave_super_secreta_123'  # ⚠️ VULNERABILIDAD: Clave hardcodeada

# Configuración
DATABASE = 'database.db'

def init_db():
    """Inicializar base de datos con usuarios de prueba"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # ⚠️ VULNERABILIDAD: Query sin prepared statements
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT,
            role TEXT DEFAULT 'user'
        )
    ''')
    
    # Usuarios de prueba
    usuarios_prueba = [
        ('admin', '123456', 'admin@vulnlab.com', 'admin'),
        ('usuario1', 'password', 'user1@vulnlab.com', 'user'),
        ('jose', 'qwerty', 'jose@vulnlab.com', 'user'),
        ('maria', '12345', 'maria@vulnlab.com', 'user'),
    ]
    
    for username, password, email, role in usuarios_prueba:
        try:
            # ⚠️ VULNERABILIDAD: Contraseñas en texto plano (sin hash)
            cursor.execute(
                "INSERT INTO users (username, password, email, role) VALUES (?, ?, ?, ?)",
                (username, password, email, role)
            )
        except sqlite3.IntegrityError:
            pass  # Usuario ya existe
    
    conn.commit()
    conn.close()

@app.route('/')
def index():
    """Página principal - redirige al login"""
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Página de login con múltiples vulnerabilidades
    ⚠️ VULNERABILIDADES:
    - SQL Injection
    - Information Disclosure
    - No rate limiting (Brute Force)
    """
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # ⚠️ VULNERABILIDAD CRÍTICA: SQL Injection
        # La query es vulnerable porque concatena directamente la entrada del usuario
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        
        # QUERY VULNERABLE - NO hacer esto en producción
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        print(f"[DEBUG] Query ejecutado: {query}")  # ⚠️ Information Disclosure
        
        try:
            cursor.execute(query)
            user = cursor.fetchone()
            
            if user:
                # Login exitoso
                session['user_id'] = user[0]
                session['username'] = user[1]
                session['role'] = user[4]
                
                flash(f'¡Bienvenido {user[1]}!', 'success')
                return redirect(url_for('dashboard'))
            else:
                # ⚠️ VULNERABILIDAD: Information Disclosure
                # Revela si el usuario existe o no
                cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
                user_exists = cursor.fetchone()
                
                if user_exists:
                    flash(f'Contraseña incorrecta para el usuario {username}', 'danger')
                else:
                    flash(f'El usuario {username} no existe', 'danger')
                    
        except sqlite3.Error as e:
            # ⚠️ VULNERABILIDAD: Muestra errores de SQL al usuario
            flash(f'Error en la base de datos: {str(e)}', 'danger')
        
        conn.close()
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Registro de usuarios
    ⚠️ VULNERABILIDADES:
    - Weak Password Policy (acepta contraseñas débiles)
    - Sin validación de email
    """
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        
        # ⚠️ VULNERABILIDAD: No valida complejidad de contraseña
        if len(password) < 3:
            flash('La contraseña debe tener al menos 3 caracteres', 'warning')
            return render_template('register.html')
        
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        
        try:
            # ⚠️ VULNERABILIDAD: Contraseña en texto plano
            cursor.execute(
                "INSERT INTO users (username, password, email, role) VALUES (?, ?, ?, 'user')",
                (username, password, email)
            )
            conn.commit()
            flash('¡Usuario registrado exitosamente! Ahora puedes iniciar sesión.', 'success')
            return redirect(url_for('login'))
            
        except sqlite3.IntegrityError:
            flash('El usuario ya existe', 'danger')
        
        conn.close()
    
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    """Panel de control del usuario autenticado"""
    if 'user_id' not in session:
        flash('Debes iniciar sesión primero', 'warning')
        return redirect(url_for('login'))
    
    # Obtener información del usuario
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (session['user_id'],))
    user = cursor.fetchone()
    
    # Obtener todos los usuarios (solo para admin)
    all_users = []
    if session.get('role') == 'admin':
        cursor.execute("SELECT id, username, email, role FROM users")
        all_users = cursor.fetchall()
    
    conn.close()
    
    return render_template('dashboard.html', user=user, all_users=all_users)

@app.route('/logout')
def logout():
    """Cerrar sesión"""
    session.clear()
    flash('Sesión cerrada exitosamente', 'info')
    return redirect(url_for('login'))

@app.route('/users')
def list_users():
    """
    ⚠️ VULNERABILIDAD: Information Disclosure
    Endpoint que lista todos los usuarios sin autenticación
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT username, email, role FROM users")
    users = cursor.fetchall()
    conn.close()
    
    html = "<h1>Usuarios del Sistema</h1><ul>"
    for user in users:
        html += f"<li>{user[0]} - {user[1]} ({user[2]})</li>"
    html += "</ul>"
    
    return html

if __name__ == '__main__':
    # Inicializar base de datos
    if not os.path.exists(DATABASE):
        print("[+] Creando base de datos...")
        init_db()
        print("[+] Base de datos creada con usuarios de prueba")
        print("\n📋 Usuarios de prueba:")
        print("   - admin:123456 (administrador)")
        print("   - usuario1:password")
        print("   - jose:qwerty")
        print("   - maria:12345")
    
    print("\n🚀 Iniciando servidor vulnerable...")
    print("⚠️  ADVERTENCIA: Esta aplicación contiene vulnerabilidades intencionales")
    print("📍 URL: http://localhost:5000")
    print("\n🎯 Vulnerabilidades activas:")
    print("   ✓ SQL Injection en login")
    print("   ✓ Brute Force (sin rate limiting)")
    print("   ✓ Information Disclosure")
    print("   ✓ Weak Password Policy")
    print("   ✓ Session Hijacking (cookies predecibles)")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
