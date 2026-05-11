import os
import hashlib
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


def encriptar_contrasena(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()


def crear_usuario(usuario, contrasena):
    password_hash = encriptar_contrasena(contrasena)

    usuario_existente = supabase.table("usuarios").select("*").eq("usuario", usuario).execute()

    if usuario_existente.data:
        return None

    nuevo_usuario = {
        "usuario": usuario,
        "password_hash": password_hash,
        "fichas": 100
    }

    respuesta = supabase.table("usuarios").insert(nuevo_usuario).execute()

    if respuesta.data:
        return respuesta.data[0]

    return None


def iniciar_usuario(usuario, contrasena):
    password_hash = encriptar_contrasena(contrasena)

    respuesta = supabase.table("usuarios").select("*").eq("usuario", usuario).eq("password_hash", password_hash).execute()

    if respuesta.data:
        return respuesta.data[0]

    return None


def obtener_usuario(usuario):
    respuesta = supabase.table("usuarios").select("*").eq("usuario", usuario).execute()

    if respuesta.data:
        return respuesta.data[0]

    return None


def actualizar_fichas(usuario, fichas):
    respuesta = supabase.table("usuarios").update({"fichas": fichas}).eq("usuario", usuario).execute()

    if respuesta.data:
        return respuesta.data[0]

    return None