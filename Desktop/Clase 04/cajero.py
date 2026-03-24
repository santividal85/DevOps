import tkinter as tk
from tkinter import font as tkfont
import datetime

users = []

# ── Paleta de colores estilo terminal bancaria ──────────────────────────────
BG        = "#0a0f0a"   # negro verdoso profundo
FG        = "#000000"   # verde fósforo
FG_DIM    = "#007a20"   # verde apagado
FG_ACCENT = "#323937"   # cian-verde para acentos
FG_WARN   = "#ffcc00"   # amarillo advertencia
FG_ERR    = "#ff4444"   # rojo error
BTN_BG    = "#0d1f0d"
BTN_HOV   = "#1a3d1a"
BORDER    = "#00ff41"
SEPARATOR = "#003810"

class Usuario:
    def __init__(self, nombre, NIP):
        self.nombre = nombre
        self.NIP = NIP
        self.saldo = 0.0
        self.historial = []

    def agregarSaldo(self, saldoNuevo):
        self.saldo += saldoNuevo
        self.historial.append(("DEP", saldoNuevo, self.saldo))

    def retirarSaldo(self, saldoRestado):
        if saldoRestado > self.saldo:
            return False
        self.saldo -= saldoRestado
        self.historial.append(("RET", saldoRestado, self.saldo))
        return True

    def ingresar(self, nom, np):
        return nom == self.nombre and np == self.NIP


class CajeroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BANCO TECMILENIO — ATM v2.1")
        self.root.resizable(False, False)
        self.root.configure(bg=BG)
        self.root.geometry("440x580")

        # Fuentes monoespaciadas
        self.font_title  = tkfont.Font(family="Courier", size=13, weight="bold")
        self.font_mono   = tkfont.Font(family="Courier", size=10)
        self.font_small  = tkfont.Font(family="Courier", size=9)
        self.font_big    = tkfont.Font(family="Courier", size=15, weight="bold")
        self.font_header = tkfont.Font(family="Courier", size=11, weight="bold")

        self.usuario_actual = None
        self._build_chrome()
        self.mostrar_menu_principal()

    def _build_chrome(self):
        """Marco superior fijo con logo y reloj."""
        top = tk.Frame(self.root, bg=BG, pady=6)
        top.pack(fill="x")

        tk.Label(top, text="█ BANCO TECMILENIO █",
                 font=self.font_title, fg=FG_ACCENT, bg=BG).pack()
        tk.Label(top, text="CAJERO AUTOMÁTICO / ATM",
                 font=self.font_small, fg=FG_DIM, bg=BG).pack()

        # Línea separadora
        tk.Frame(self.root, bg=BORDER, height=1).pack(fill="x", padx=10)

        # Reloj
        self.lbl_clock = tk.Label(self.root, text="", font=self.font_small,
                                  fg=FG_DIM, bg=BG)
        self.lbl_clock.pack(anchor="e", padx=14)
        self._tick()

        # Área de contenido dinámico
        self.content = tk.Frame(self.root, bg=BG)
        self.content.pack(fill="both", expand=True, padx=20, pady=4)

        # Pie de página
        tk.Frame(self.root, bg=BORDER, height=1).pack(fill="x", padx=10)
        tk.Label(self.root,
                 text="[  INTRODUZCA TARJETA  ]   [  CANCELAR  ]   [  ACEPTAR  ]",
                 font=self.font_small, fg=FG_DIM, bg=BG, pady=5).pack()

    def _tick(self):
        now = datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
        self.lbl_clock.config(text=now)
        self.root.after(1000, self._tick)

    def limpiar(self):
        for w in self.content.winfo_children():
            w.destroy()

    # ── helpers de UI ────────────────────────────────────────────────────────

    def _sep(self, parent=None):
        p = parent or self.content
        tk.Label(p, text="─" * 46, font=self.font_small,
                 fg=SEPARATOR, bg=BG).pack()

    def _label(self, text, color=None, size=None, parent=None):
        p = parent or self.content
        f = self.font_mono if size is None else tkfont.Font(family="Courier",
                                                            size=size)
        tk.Label(p, text=text, font=f,
                 fg=color or FG, bg=BG).pack(pady=1)

    def _button(self, parent, text, cmd, accent=False):
        color  = FG_ACCENT if accent else FG
        border = FG_ACCENT if accent else FG_DIM
        btn = tk.Button(
            parent, text=text, command=cmd,
            font=self.font_mono, fg=color, bg=BTN_BG,
            activeforeground=BG, activebackground=color,
            relief="flat", bd=0, cursor="hand2",
            width=28, pady=5,
            highlightthickness=1, highlightbackground=border,
        )
        btn.pack(pady=3)
        btn.bind("<Enter>", lambda _e: btn.config(bg=BTN_HOV))
        btn.bind("<Leave>", lambda _e: btn.config(bg=BTN_BG))
        return btn

    def _entry(self, parent, show=None):
        e = tk.Entry(
            parent, font=self.font_mono,
            fg=FG, bg="#050f05", insertbackground=FG,
            relief="flat", bd=0,
            highlightthickness=1, highlightbackground=FG_DIM,
            width=28,
        )
        if show:
            e.config(show=show)
        e.pack(pady=4, ipady=4)
        return e

    def _field_label(self, text, parent=None):
        p = parent or self.content
        tk.Label(p, text=f"  {text}", font=self.font_small,
                 fg=FG_DIM, bg=BG, anchor="w").pack(fill="x")

    def _status_msg(self, text, color=FG_WARN):
        lbl = tk.Label(self.content, text=text, font=self.font_small,
                       fg=color, bg=BG, wraplength=380, justify="center")
        lbl.pack(pady=6)
        return lbl

    # ── Pantallas ────────────────────────────────────────────────────────────

    def mostrar_menu_principal(self):
        self.limpiar()
        self.usuario_actual = None

        self._sep()
        self._label("  BIENVENIDO / WELCOME", color=FG_ACCENT, size=12)
        self._label("  Seleccione una opción:", color=FG_DIM)
        self._sep()

        tk.Frame(self.content, bg=BG, height=8).pack()

        self._button(self.content, "[ 1 ]  CREAR CUENTA",
                     self.pantalla_crear_usuario, accent=True)
        self._button(self.content, "[ 2 ]  INGRESAR A CUENTA",
                     self.pantalla_login)
        tk.Frame(self.content, bg=BG, height=6).pack()
        self._button(self.content, "[ 0 ]  SALIR",
                     self.root.quit)

        self._sep()
        self._label("  Inserte su tarjeta para comenzar.", color=FG_DIM)

    def pantalla_crear_usuario(self):
        self.limpiar()
        self._sep()
        self._label("  NUEVA CUENTA / NEW ACCOUNT", color=FG_ACCENT, size=11)
        self._sep()

        self._field_label("NOMBRE DE USUARIO:")
        entry_nombre = self._entry(self.content)

        self._field_label("NIP (4–6 dígitos):")
        entry_nip = self._entry(self.content, show="●")

        self.msg_var = tk.StringVar()
        lbl_msg = tk.Label(self.content, textvariable=self.msg_var,
                           font=self.font_small, fg=FG_ERR, bg=BG)
        lbl_msg.pack()

        def crear():
            nombre = entry_nombre.get().strip()
            nip    = entry_nip.get().strip()
            if not nombre or not nip:
                self.msg_var.set("  ⚠  Completa todos los campos.")
                return
            nuevo = Usuario(nombre, nip)
            users.append(nuevo)
            self.usuario_actual = nuevo
            self.pantalla_menu_usuario()

        tk.Frame(self.content, bg=BG, height=4).pack()
        self._button(self.content, "[ CREAR CUENTA ]", crear, accent=True)
        self._button(self.content, "[ CANCELAR / VOLVER ]",
                     self.mostrar_menu_principal)

    def pantalla_login(self):
        self.limpiar()
        self._sep()
        self._label("  IDENTIFICACIÓN / LOGIN", color=FG_ACCENT, size=11)
        self._sep()

        self._field_label("NOMBRE DE USUARIO:")
        entry_nombre = self._entry(self.content)

        self._field_label("NIP:")
        entry_nip = self._entry(self.content, show="●")

        self.msg_var = tk.StringVar()
        lbl_msg = tk.Label(self.content, textvariable=self.msg_var,
                           font=self.font_small, fg=FG_ERR, bg=BG)
        lbl_msg.pack()

        attempt = [0]

        def ingresar():
            nombre = entry_nombre.get().strip()
            nip    = entry_nip.get().strip()
            for user in users:
                if user.ingresar(nombre, nip):
                    self.usuario_actual = user
                    self.pantalla_menu_usuario()
                    return
            attempt[0] += 1
            entry_nip.delete(0, tk.END)
            self.msg_var.set(
                f"  ✖  NIP incorrecto. Intento {attempt[0]}/3."
                if attempt[0] < 3 else
                "  ✖  Cuenta bloqueada temporalmente."
            )

        tk.Frame(self.content, bg=BG, height=4).pack()
        self._button(self.content, "[ ACEPTAR ]", ingresar, accent=True)
        self._button(self.content, "[ CANCELAR / VOLVER ]",
                     self.mostrar_menu_principal)

    def pantalla_menu_usuario(self):
        self.limpiar()
        user = self.usuario_actual

        self._sep()
        self._label(f"  BIENVENIDO,  {user.nombre.upper()}", color=FG_ACCENT)
        self._sep()

        # Saldo
        saldo_frame = tk.Frame(self.content, bg=BG)
        saldo_frame.pack(fill="x", pady=6)
        tk.Label(saldo_frame, text="  SALDO DISPONIBLE:",
                 font=self.font_small, fg=FG_DIM, bg=BG).pack(anchor="w")
        self.lbl_saldo = tk.Label(
            saldo_frame,
            text=f"  $ {user.saldo:,.2f} MXN",
            font=self.font_big, fg=FG_ACCENT, bg=BG
        )
        self.lbl_saldo.pack(anchor="w")

        self._sep()
        self._field_label("CANTIDAD (MXN):")
        self.entry_cantidad = self._entry(self.content)

        self.msg_var = tk.StringVar()
        tk.Label(self.content, textvariable=self.msg_var,
                 font=self.font_small, fg=FG_WARN, bg=BG).pack()

        self._button(self.content, "[ 1 ]  DEPOSITAR",
                     self.depositar, accent=True)
        self._button(self.content, "[ 2 ]  RETIRAR", self.retirar)
        tk.Frame(self.content, bg=BG, height=4).pack()
        self._button(self.content, "[ 0 ]  CERRAR SESIÓN",
                     self.mostrar_menu_principal)

    # ── Operaciones ──────────────────────────────────────────────────────────

    def _obtener_cantidad(self):
        try:
            valor = float(self.entry_cantidad.get().replace(",", ""))
            if valor <= 0:
                raise ValueError
            return valor
        except ValueError:
            self.msg_var.set("  ⚠  Ingresa una cantidad válida.")
            return None

    def depositar(self):
        cantidad = self._obtener_cantidad()
        if cantidad is None:
            return
        self.usuario_actual.agregarSaldo(cantidad)
        self.entry_cantidad.delete(0, tk.END)
        self.lbl_saldo.config(
            text=f"  $ {self.usuario_actual.saldo:,.2f} MXN")
        self.msg_var.set(
            f"  ✔  Depósito exitoso: + ${cantidad:,.2f}")

    def retirar(self):
        cantidad = self._obtener_cantidad()
        if cantidad is None:
            return
        if self.usuario_actual.retirarSaldo(cantidad):
            self.entry_cantidad.delete(0, tk.END)
            self.lbl_saldo.config(
                text=f"  $ {self.usuario_actual.saldo:,.2f} MXN")
            self.msg_var.set(
                f"  ✔  Retiro exitoso: - ${cantidad:,.2f}")
        else:
            self.msg_var.set("  ✖  Saldo insuficiente.")


if __name__ == "__main__":
    root = tk.Tk()
    app = CajeroApp(root)
    root.mainloop()
