import html
import pytest
from datetime import datetime
import os
import allure # ¡NUEVO! Necesario para adjuntar archivos al reporte Allure

# NOTA: Este hook es parte de la API de Pytest. Se ejecuta automáticamente 
# después de cada test de la suite.

# conftest.py
import pytest
import allure
from allure_commons.types import AttachmentType

# Asume que 'driver' es un fixture disponible para el test.
# Si estás usando Pytest-Selenium, esto ya está configurado.
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    # 1. Chequea que la prueba haya fallado durante la llamada (call)
    if report.when == 'call' and report.failed:
        # 2. Intenta obtener el fixture 'driver'
        driver = item.funcargs.get('driver') 
        
        if driver is not None:
            try:
                # 3. Toma la captura y la adjunta como PNG
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name=f"Falla de {item.nodeid}",
                    attachment_type=AttachmentType.PNG
                )
                # Opcional: Para confirmar en consola que se adjuntó
                print(f"\n[ALLURE] Captura adjuntada para: {item.nodeid}")
            except Exception as e:
                print(f"\n[ALLURE ERROR] Fallo al adjuntar la captura: {e}")
        else:
            print("\n[ALLURE INFO] Fixture 'driver' no encontrado o no inicializado.")

# NOTA: La lógica de adjunto a pytest-html ha sido eliminada.
# Ahora la lógica se centra en el adjunto de alta fidelidad de Allure.
#@pytest.hookimpl(hookwrapper=True)
#def pytest_runtest_makereport(item, call):
#    outcome = yield
#    report = outcome.get_result()
#    extra = getattr(report, 'extra', [])
#    if report.when == 'call' and report.failed:
#        # Assumes 'driver' is a fixture providing the WebDriver instance
#        if 'driver' in item.fixturenames:
#            driver = item.funcargs['driver']
#            screenshot_path = f"screenshots/{item.name}.png"
#            driver.save_screenshot(screenshot_path)
#            extra.append(html.img(src=screenshot_path, width="300px", height="200px"))
#        report.extra = extra