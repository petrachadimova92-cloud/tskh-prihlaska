import os
import ssl
import smtplib
from email.message import EmailMessage
from typing import Dict, Any, Optional, List

def _csv(items: Optional[List[str]]) -> str:
    return ", ".join(items or []) if items else "-"

def _format_form_body(data: Dict[str, Any]) -> str:
    # Required
    jmeno = data.get("jmeno", "")
    prijmeni = data.get("prijmeni", "")
    vek = data.get("vek", "")
    tel = data.get("telefoni_cislo", "")
    email = data.get("email", "")
    bydliste = data.get("bydliste", "")
    hobby = _csv(data.get("vybrane_hobby_skupiny"))
    poloprofi = _csv(data.get("vybarane_poloprofi_skupiny"))  # (typo preserved if your form uses it)
    profi = _csv(data.get("vybrane_profi_skupiny"))

    # Optional guardian
    zjmeno = data.get("jmeno_zakonneho_zastupce")
    zprijmeni = data.get("prijmeni_zakonneho_zastupce")
    ztel = data.get("telefoni_cislo_zakonneho_zastupce")
    zemail = data.get("email_zakonneho_zastupce")

    lines = [
        "Nová odpověď z formuláře:",
        "",
        f"Jméno: {jmeno}",
        f"Příjmení: {prijmeni}",
        f"Věk: {vek}",
        f"Telefonní číslo: {tel}",
        f"E-mail: {email}",
        f"Bydliště: {bydliste}",
        "",
        f"Vybrané hobby skupiny: {hobby}",
        f"Vybrané poloprofi skupiny: {poloprofi}",
        f"Vybrané profi skupiny: {profi}",
    ]

    if any([zjmeno, zprijmeni, ztel, zemail]):
        lines += [
            "",
            "Zákonný zástupce:",
            f"Jméno: {zjmeno or '-'}",
            f"Příjmení: {zprijmeni or '-'}",
            f"Telefonní číslo: {ztel or '-'}",
            f"E-mail: {zemail or '-'}",
        ]

    return "\n".join(lines)

def send_form_email_smtp(
    data: Dict[str, Any],
    to_email: str,
    subject: str = "Nová odpověď z formuláře",
    gmail_user: Optional[str] = None,
    gmail_app_password: Optional[str] = None,
    from_alias: Optional[str] = None,
) -> None:
    """
    Uses Gmail SMTP with an App Password (NOT your normal password).
    """
    gmail_user = gmail_user or os.environ.get("GMAIL_USER")
    gmail_app_password = gmail_app_password or os.environ.get("GMAIL_APP_PASSWORD")
    assert gmail_user and gmail_app_password, "Missing Gmail credentials."

    msg = EmailMessage()
    msg["From"] = f"{from_alias} <{gmail_user}>" if from_alias else gmail_user
    msg["To"] = to_email
    msg["Subject"] = subject
    # So you can reply directly to the submitter:
    if data.get("email"):
        msg["Reply-To"] = data["email"]

    msg.set_content(_format_form_body(data))  # UTF-8 by default

    context = ssl.create_default_context()
    # STARTTLS on port 587 (recommended)
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(gmail_user, gmail_app_password)
        server.send_message(msg)