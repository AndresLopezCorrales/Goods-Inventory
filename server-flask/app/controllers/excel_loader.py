import pandas as pd
from app.models.responsible import Responsible
from app.models.location import Location
from app.models.items import Items
from app.database import db

def load_excel_data(area_excel, articulos_excel):
    # ================== EXCEL DE ÁREAS ==================
    df_area = pd.read_excel(area_excel, header=4)  # salta encabezados irrelevantes

    df_area.columns = df_area.columns.str.strip()  # limpiar espacios
    # eliminar filas con NaN en las columnas importantes
    df_area = df_area.dropna(subset=['Responsable(s)', 'Ubicación', 'Descripción'])
    
    for _, row in df_area.iterrows():
        responsable_name = str(row['Responsable(s)']).strip()
        ubicacion_num = int(row['Ubicación'])
        descripcion = str(row['Descripción']).strip()

        # Buscar o crear responsable
        responsable = Responsible.query.filter_by(name=responsable_name).first()
        if not responsable:
            responsable = Responsible(name=responsable_name)
            db.session.add(responsable)
            db.session.commit()

        # Buscar o crear ubicación
        location = Location.query.filter_by(number_location=ubicacion_num).first()
        if not location:
            location = Location(
                id_responsible=responsable.id_responsible,
                number_location=ubicacion_num,
                description=descripcion
            )
            db.session.add(location)
        else:
            # si ya existe, actualizamos responsable o descripción si cambió
            location.id_responsible = responsable.id_responsible
            location.description = descripcion

    db.session.commit()

    # ================== EXCEL DE ARTÍCULOS ==================
    df_articulos = pd.read_excel(articulos_excel, header=6)  # salta encabezados irrelevantes

    df_articulos.columns = df_articulos.columns.str.strip()  # limpiar espacios
    # eliminar filas con NaN en las columnas importantes
    df_articulos = df_articulos.dropna(subset=['NO.CUENTA', 'UBICA', 'DESCRIPCION'])

    for _, row in df_articulos.iterrows():
        no_cuenta = str(row['NO.CUENTA']).split('.')[0] 
        ubicacion = int(row['UBICA'])
        descripcion = str(row['DESCRIPCION']).strip()

        # buscar ubicación
        location = Location.query.filter_by(number_location=ubicacion).first()
        if not location:
            # si no existe la ubicación, se ignora o puedes decidir crearla vacía
            continue

        # buscar o crear item
        item = Items.query.filter_by(account_name=no_cuenta).first()
        if not item:
            item = Items(
                id_location=location.id_location,
                account_name=no_cuenta,
                description=descripcion
            )
            db.session.add(item)
        else:
            # si ya existe, actualizamos descripción
            item.description = descripcion

    db.session.commit()
