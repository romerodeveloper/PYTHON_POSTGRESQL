import imp
from logger_base import log
from usuario_dao import UsuarioDao
from usuario import Usuario


opcion = None
while opcion != 5:
    print('opciones:')
    print('1. Listar Usuarios')
    print('2. Agregar Usuario')
    print('3. Modificar Usuario')
    print('4. Eliminar Usuario')
    print('5. Salir')
    opcion = int(input('Escribe una opcion (1-5): '))
    if opcion == 1:
        usuarios = UsuarioDao.seleccionar()
        for usuario in usuarios:
            log.info(usuario)
    elif opcion == 2:
        Username = input('Ingresa un nombre de usuario: ')
        Password = input('Ingresa una contraseña: ')
        dato = Usuario(username=Username, password=Password)
        registro = UsuarioDao.insertar(dato)
        log.info(f'Datos insertados {registro}')
    elif opcion == 3:
        id_usuario = int(input('Ingresa el id del usuario: '))
        Username = input('Ingresa un nombre de usuario: ')
        Password = input('Ingresa una contraseña: ')
        dato = Usuario(id_usuario=id_usuario,username=Username, password=Password)
        registro = UsuarioDao.actualizar(dato)
        log.info(f'Datos actualizados {registro}')
    elif opcion == 4:
        id_usuario = int(input('Ingresa el id del usuario: '))
        dato = Usuario(id_usuario=id_usuario)
        registro = UsuarioDao.eliminar(dato)
        log.info(f'Datos actualizados {registro}')
    else:
        log.info("finalizacion del aplicativo")