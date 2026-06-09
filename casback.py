        "└ Máximo 80€ por transacción\n\n"
        "ℹ️ <i>Activa el cashback ANTES de tu primera compra. "
        "Usa el mismo navegador y dispositivo con el que te registraste en Temu. "
        "Si TopCashback detecta que ya tienes cuenta, se aplica la tarifa de cliente recurrente (5%).</i>\n\n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        "🛒 <b>MIRAVIA</b> — Cashback por categoría\n\n"
        "  👗 Moda y belleza ········ <b>12%</b>\n"
        "  🏥 Salud ·················· <b>9%</b>\n"
        "  🏠 Hogar ················· <b>7%</b>\n"
        "  👶 Madre y bebé ········ <b>7%</b>\n"
        "  🐾 Mascotas ············· <b>6%</b>\n"
        "  💻 Informática ·········· <b>3%</b>\n"
        "  🛍️ Resto de compras ··· <b>3%</b>\n"
        "  📈 Máximo ················ <b>hasta 50%</b>\n\n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        f"👉 <a href=\"{LINK_TOPCASH}\">Activar cashback en TopCashback</a>\n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        "💡 <i>Regístrate gratis y activa el cashback antes de comprar. "
        "Es dinero real que te devuelven por compras que harías de todas formas.</i>"
    )

def mensaje_igraal():
    return (
        "⚡ <b>CASHBACK DEL DÍA — iGraal</b>\n"
        "━━━━━━━━━━━━━━━━━━━━━\n\n"
        "💡 <b>IBERDROLA</b>\n"
        "┌ 🔥 <b>Entre 80€ y 160€ de cashback</b>\n"
        "└ Por contratar el plan online de luz\n\n"
        "ℹ️ <i>Reembolso por contratar el plan online. "
        "Si estás pensando en cambiar de compañía, este es el momento. "
        "El cashback se abona una vez confirmada la activación del contrato.</i>\n\n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        "🏦 <b>N26</b>\n"
        "┌ 💸 <b>Entre 30€ y 60€ de cashback</b>\n"
        "└ Por abrir y activar una cuenta bancaria\n\n"
        "ℹ️ <i>N26 es un banco 100% online sin comisiones. "
        "El cashback se acredita al activar la cuenta y completar la verificación. "
        "Solo para cuentas nuevas.</i>\n\n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        f"👉 <a href=\"{LINK_IGRAAL}\">Activar cashback en iGraal</a>\n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        "💡 <i>Estos son cashbacks de alto valor. "
        "Una sola contratación puede darte más de 100€ de vuelta.</i>"
    )

def mensaje_letyshops():
    return (
        "🛒 <b>CASHBACK DEL DÍA — Letyshops</b>\n"
        "━━━━━━━━━━━━━━━━━━━━━\n\n"
        "📦 <b>ALIEXPRESS</b>\n"
        "┌ 🔥 <b>Del 20% al 40% de cashback</b>\n"
        "└ En artículos seleccionados\n\n"
        "ℹ️ <i>No todos los productos tienen el mismo porcentaje. "
        "El cashback más alto aplica a artículos de vendedores con promoción activa. "
        "Comprueba siempre que el cashback está activado antes de añadir al carrito — "
        "verás el porcentaje confirmado en Letyshops antes de que te redirija a AliExpress.</i>\n\n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        f"👉 <a href=\"{LINK_LETY}\">Activar cashback en Letyshops</a>\n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        "💡 <i>El truco está en los artículos de vendedores en promoción. "
        "Activa el cashback desde Letyshops antes de buscar el producto "
        "para asegurarte el porcentaje más alto.</i>"
    )

def mensaje_explicacion():
    return (
        "❓ <b>¿QUÉ ES EL CASHBACK?</b>\n"
        "━━━━━━━━━━━━━━━━━━━━━\n\n"
        "El cashback es dinero real que te devuelven por compras que ya ibas a hacer.\n\n"
        "<b>¿Cómo funciona?</b>\n"
        "1️⃣ Te registras gratis en iGraal, TopCashback o Letyshops\n"
        "2️⃣ Antes de comprar, entras a la tienda desde esa plataforma\n"
        "3️⃣ Compras como siempre\n"
        "4️⃣ La plataforma recibe una comisión de la tienda y te devuelve parte a ti\n\n"
        "<b>¿Es seguro?</b>\n"
        "✅ Sí. Son plataformas legales con millones de usuarios en Europa.\n\n"
        "<b>¿Cuándo cobro?</b>\n"
        "⏳ Entre 30 y 90 días según la tienda, una vez confirmada la compra.\n\n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        f"🟢 <a href=\"{LINK_IGRAAL}\">Registrarse en iGraal</a>\n"
        f"🔵 <a href=\"{LINK_TOPCASH}\">Registrarse en TopCashback</a>\n"
        f"🟡 <a href=\"{LINK_LETY}\">Registrarse en Letyshops</a>\n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        "💡 <i>Regístrate en las tres. Son gratis y se complementan — "
        "cada una tiene mejores ofertas en tiendas distintas.</i>"
    )

def main():
    hoy = datetime.date.today().weekday()  # 0=lunes … 6=domingo

    if hoy in (0, 3):      # Lunes y jueves
        enviar(mensaje_topcashback())
    elif hoy in (1, 4):    # Martes y viernes
        enviar(mensaje_igraal())
    elif hoy in (2, 5):    # Miércoles y sábado
        enviar(mensaje_letyshops())
    else:                  # Domingo — resumen completo
        import time
        enviar(mensaje_topcashback())
        time.sleep(3)
        enviar(mensaje_igraal())
        time.sleep(3)
        enviar(mensaje_letyshops())
        time.sleep(3)
        enviar(mensaje_explicacion())

if __name__ == "__main__":
    main()
